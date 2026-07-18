---
id: CHG-0009-adopt-specsync-5-1-1-as-the-pinned-contract-toolchain
state: archived
type: feature
base_commit: cccb7d224765e0c821957f4ddacd02ef0493c4c6
---

# Adopt SpecSync 5.1.1 as the pinned contract toolchain

## Intent

Adopt SpecSync 5.1.1 as the pinned contract toolchain

## Affected Canonical Specs

- `trust-action`
- `trust-policy`
- `trust-provenance`

## Acceptance Criteria

- Trust pins SpecSync 5.1.1 as the composite action default and nested immutable action commit (a89d827e93fa0bc9e6168447e66a0ad30fa92e65); trust_cli.py, validate.py, release.yml, README, and RELEASING agree on the 5.1.1 pin; the 5.0.1-era change ledgers validate under both 5.0.1 and 5.1.1; fledge lanes run verify and strict contract validation pass with the 5.1.1 binary; stale accepted changes reopen and re-accept natively under 5.1.1 without replaying canonical deltas.

## No-spec Rationale

Not applicable
