#!/usr/bin/env python3
"""Backfill SpecSync 5.1 reopening digest fields in .specsync ledgers.

SpecSync 5.1 added two required fields to the reopening audit records
stored in each change's approvals.json (ReopenRecord):

  - stale_acceptance_input_digest
  - current_acceptance_input_digest

SpecSync 5.0.1 ignores the reopenings array entirely (its ApprovalLedger
only deserializes `approvals`), so adding these fields is backward
compatible. Records written before 5.1 lack the fields and fail to parse
under 5.1; this script backfills them additively:

  stale   := the acceptance_input_digest embedded in the reopening's
             own prior_verification (exactly what `specsync change
             reopen` records natively under 5.1).
  current := the acceptance_input_digest recorded next in the ledger --
             the following reopening's prior_verification digest, or the
             change's verification.json digest for the latest reopening.
             Reopenings recorded while delivery inputs were unchanged
             (evidence-refresh reopens) intentionally get current ==
             stale; 5.1 only parses these fields for accepted changes
             and never compares them.

The script is idempotent: records that already carry both fields are
left untouched. For every reopening (migrated or not) it also verifies
that superseded_approval.digest equals the closing digest of the
embedded prior_verification under the closing-digest algorithm shared
by 5.0.1 and 5.1.x, and that each change's latest acceptance approval
matches the closing digest of its verification.json.

Usage: migrate_specsync_5_1_records.py [REPO_ROOT]
Defaults to the repository containing the script (scripts/..).
"""
from __future__ import annotations

import hashlib
import json
import struct
import sys
from pathlib import Path

__all__ = []

ROOT = (
    Path(sys.argv[1]).resolve()
    if len(sys.argv) > 1
    else Path(__file__).resolve().parent.parent
)
LEDGER_GLOBS = (
    ".specsync/changes/*/approvals.json",
    ".specsync/archive/changes/*/approvals.json",
)

CLOSING_DIGEST_DOMAIN = b"specsync.closing-digest.v2"


def framed(domain: bytes, frames: list[tuple[bytes, bytes]]) -> str:
    digest = hashlib.sha256()
    digest.update(struct.pack(">Q", len(b"domain")))
    digest.update(b"domain")
    digest.update(struct.pack(">Q", len(domain)))
    digest.update(domain)
    for tag, value in frames:
        digest.update(struct.pack(">Q", len(tag)))
        digest.update(tag)
        digest.update(struct.pack(">Q", len(value)))
        digest.update(value)
    return digest.hexdigest()


def closing_digest(change_id: str, verification: dict) -> str:
    """Closing digest as computed by spec-sync 5.0.1 and 5.1.x alike.

    The 5.1.x acceptance-manifest and semantic-succession frames are
    conditional on those fields being present; legacy verification
    records without them hash identically under both versions.
    """
    frames = [
        (b"record-id", change_id.encode()),
        (b"contract", verification["contract_digest"].encode()),
        (b"workspace", verification.get("workspace_digest", "").encode()),
        (b"commit", (verification.get("commit") or "").encode()),
    ]
    acceptance = verification.get("acceptance_input_digest")
    if acceptance is None:
        frames.append((b"acceptance", b"\x00"))
    else:
        frames.append((b"acceptance", b"\x01" + acceptance.encode()))
    if verification.get("acceptance_manifest") is not None:
        manifest = json.dumps(
            verification["acceptance_manifest"], separators=(",", ":")
        ).encode()
        frames.append((b"acceptance-input-manifest-v1", manifest))
    return framed(CLOSING_DIGEST_DOMAIN, frames)


def load_json(path: Path) -> dict:
    try:
        document = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        raise SystemExit(f"cannot read {path}: {error}") from error
    if not isinstance(document, dict):
        raise SystemExit(f"invalid {path}: root must be an object")
    return document


def backfill_reopenings(path: Path, ledger: dict) -> tuple[int, list[str]]:
    """Add the 5.1 digest fields where missing. Returns (count, problems)."""
    reopenings = ledger.get("reopenings") or []
    verification_path = path.with_name("verification.json")
    final_digest = None
    if verification_path.exists():
        final_digest = load_json(verification_path).get("acceptance_input_digest")
    migrated = 0
    problems = []
    change_id = change_id_for(path)
    for index, reopening in enumerate(reopenings):
        prior = reopening.get("prior_verification") or {}
        stale = prior.get("acceptance_input_digest")
        if stale is None:
            problems.append(f"reopening {index}: prior_verification has no acceptance_input_digest")
            stale = ""
        if "stale_acceptance_input_digest" not in reopening:
            reopening["stale_acceptance_input_digest"] = stale
            migrated += 1
        if "current_acceptance_input_digest" not in reopening:
            following = reopenings[index + 1 :]
            current = next(
                (
                    (r.get("prior_verification") or {}).get("acceptance_input_digest")
                    for r in following
                    if (r.get("prior_verification") or {}).get("acceptance_input_digest")
                ),
                final_digest or stale,
            )
            reopening["current_acceptance_input_digest"] = current
            migrated += 1
        superseded = reopening.get("superseded_approval") or {}
        expected = closing_digest(reopening.get("change_id", change_id), prior)
        if superseded.get("digest") != expected:
            problems.append(
                f"reopening {index}: superseded approval digest does not match "
                "prior verification closing digest"
            )
    return migrated, problems


def change_id_for(path: Path) -> str:
    """Active change dirs are named by id; archived dirs carry a date prefix."""
    for name in ("state.json", "accepted-state.json"):
        state_path = path.with_name(name)
        if state_path.exists():
            record_id = load_json(state_path).get("id")
            if isinstance(record_id, str) and record_id:
                return record_id
    return path.parent.name


def verify_closing_approval(path: Path, ledger: dict) -> list[str]:
    verification_path = path.with_name("verification.json")
    if not verification_path.exists():
        return []
    verification = load_json(verification_path)
    closing = next(
        (
            approval
            for approval in reversed(ledger.get("approvals") or [])
            if approval.get("gate") == "acceptance"
        ),
        None,
    )
    if closing is None:
        return []
    expected = closing_digest(change_id_for(path), verification)
    if closing.get("digest") != expected:
        return ["latest acceptance approval does not match verification closing digest"]
    return []


def main() -> int:
    paths = sorted({path for pattern in LEDGER_GLOBS for path in ROOT.glob(pattern)})
    if not paths:
        raise SystemExit("no approval ledgers found under .specsync")
    total_migrated = 0
    failures = 0
    for path in paths:
        ledger = load_json(path)
        migrated, problems = backfill_reopenings(path, ledger)
        problems += verify_closing_approval(path, ledger)
        relative = path.relative_to(ROOT)
        for problem in problems:
            print(f"error: {relative}: {problem}", file=sys.stderr)
            failures += 1
        if migrated:
            try:
                path.write_text(json.dumps(ledger, indent=2) + "\n", encoding="utf-8")
            except OSError as error:
                raise SystemExit(f"cannot write {path}: {error}") from error
            print(f"{relative}: backfilled {migrated} reopening digest fields")
            total_migrated += migrated
    print(f"migrated {total_migrated} fields across {len(paths)} ledgers")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
