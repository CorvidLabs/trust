---
change: CHG-0009-adopt-specsync-5-1-1-as-the-pinned-contract-toolchain
artifact: requirements
---

# Requirements

## Functional

- The composite action pins the nested SpecSync action to the immutable
  v5.1.1 commit `a89d827e93fa0bc9e6168447e66a0ad30fa92e65` and defaults the
  `specsync-version` input to `5.1.1` (`action.yml`).
- `scripts/trust_cli.py` defaults `DEFAULT_SPECSYNC_VERSION` to `5.1.1`.
- `scripts/validate.py` asserts the 5.1.1 action commit and version pairing.
- `.github/workflows/release.yml` pins the SpecSync action and binary to
  5.1.1 in every validation job.
- `README.md` and `RELEASING.md` describe SpecSync 5.1.1 as the pinned
  contract toolchain.
- The canonical specs state the 5.1.1 default (trust-action Public API and
  dependencies, REQ-trust-action-010 acceptance criteria, trust-provenance
  Public API).
- `scripts/migrate_specsync_5_1_records.py` ships the ledger migration used
  for this repository's 5.0.1-era records so consuming projects can backfill
  their own reopening digests.

## Acceptance criteria

- Trust pins SpecSync 5.1.1 as the composite action default and nested
  immutable action commit; `trust_cli.py`, `validate.py`, `release.yml`,
  `README`, and `RELEASING` agree on the 5.1.1 pin.
- The 5.0.1-era change ledgers validate under both 5.0.1 and 5.1.1.
- `fledge lanes run verify` and strict contract validation pass with the
  5.1.1 binary.
- Stale accepted changes reopen and re-accept natively under 5.1.1 without
  replaying canonical deltas.
