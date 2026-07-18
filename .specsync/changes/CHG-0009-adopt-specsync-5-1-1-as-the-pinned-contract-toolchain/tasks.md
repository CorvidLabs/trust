---
change: CHG-0009-adopt-specsync-5-1-1-as-the-pinned-contract-toolchain
artifact: tasks
---

# Tasks

- [x] Backfill 5.1 reopening digest fields in change ledgers (`cccb7d2`).
- [x] Add `scripts/migrate_specsync_5_1_records.py` for consuming projects.
- [x] Pin SpecSync 5.1.1 in `action.yml` (default + nested action commit).
- [x] Update `DEFAULT_SPECSYNC_VERSION` and `validate.py` assertions.
- [x] Pin 5.1.1 in `.github/workflows/release.yml` jobs.
- [x] Document 5.1.1 in `README.md` and `RELEASING.md`.
- [x] Apply semantic deltas to trust-action and trust-provenance specs.
- [x] Verify with the 5.1.1 binary and record closing acceptance.
