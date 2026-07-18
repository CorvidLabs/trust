---
change: CHG-0009-adopt-specsync-5-1-1-as-the-pinned-contract-toolchain
artifact: docs
---

# Docs

- `README.md`: the self-hosting paragraph names SpecSync 5.1.1 as the
  released default.
- `RELEASING.md`: the Homebrew bundle and stable-release sections pair the
  immutable SpecSync action commit with binary version 5.1.1.
- Spec companion documents that narrate the original 5.0.1 adoption
  (`specs/trust/context.md`, `specs/trust/tasks.md`) are historical records
  of that era and intentionally remain unchanged.
- Consuming projects should run
  `python3 scripts/migrate_specsync_5_1_records.py` before their first
  5.1.1 validation so 5.0.1-era reopening records parse.
