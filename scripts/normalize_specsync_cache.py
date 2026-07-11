#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path


__all__ = []

ROOT = Path(__file__).resolve().parent.parent
CACHE = ROOT / ".specsync/hashes.json"


def main() -> int:
    document = json.loads(CACHE.read_text(encoding="utf-8"))
    hashes = document.get("hashes")
    valid_hashes = isinstance(hashes, dict) and all(
        isinstance(key, str) and isinstance(value, str) for key, value in hashes.items()
    )
    if not valid_hashes:
        raise SystemExit("invalid spec-sync cache: hashes must be a string map")
    normalized = {"hashes": dict(sorted(hashes.items()))}
    CACHE.write_text(json.dumps(normalized, indent=2), encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
