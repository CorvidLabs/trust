#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path


__all__ = []

ROOT = Path(__file__).resolve().parent.parent
CACHE = ROOT / ".specsync/hashes.json"


def normalize(cache: Path) -> None:
    try:
        document = json.loads(cache.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        raise SystemExit(f"cannot read spec-sync cache: {error}") from error
    if not isinstance(document, dict):
        raise SystemExit("invalid spec-sync cache: root must be an object")
    hashes = document.get("hashes")
    valid_hashes = isinstance(hashes, dict) and all(
        isinstance(key, str) and isinstance(value, str) for key, value in hashes.items()
    )
    if not valid_hashes:
        raise SystemExit("invalid spec-sync cache: hashes must be a string map")
    normalized = {"hashes": dict(sorted(hashes.items()))}
    try:
        cache.write_text(json.dumps(normalized, indent=2) + "\n", encoding="utf-8")
    except OSError as error:
        raise SystemExit(f"cannot write spec-sync cache: {error}") from error


def main() -> int:
    normalize(CACHE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
