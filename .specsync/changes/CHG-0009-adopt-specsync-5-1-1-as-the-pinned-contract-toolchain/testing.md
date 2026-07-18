---
change: CHG-0009-adopt-specsync-5-1-1-as-the-pinned-contract-toolchain
artifact: testing
---

# Testing

- `fledge lanes run verify` (fmt, lint, test) passes with the 5.1.1 pins;
  `tests/test.sh` resolver regressions continue to accept exact SemVer
  inputs and reject invalid mirrors.
- `specsync check` (5.1.1) passes strict validation with 100% coverage;
  the same records also validate under 5.0.1.
- `scripts/migrate_specsync_5_1_records.py` is idempotent and
  self-verifying: a second run reports zero migrated fields and exits 0.
- CI matrix (ubuntu, macOS, windows; standard and strict profiles;
  provenance, atlas, and fatal-path fixtures) runs with the 5.1.1 nested
  action and binary.

Evidence for REQ-trust-action-010 is bound by the `tests/test.sh`
resolver regressions and the strict contract validation of the pinned
5.1.1 default.
