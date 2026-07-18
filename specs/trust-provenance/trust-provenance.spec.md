---
module: trust-provenance
version: 9
status: stable
files:
  - scripts/record_provenance.sh
db_tables: []
depends_on: [trust-policy]
---

# Trust Provenance

## Purpose

Trust verifies Attest notes and dogfoods provenance for its own released action;
consumer signing workflows remain separate and authoritative.

## Public API

The provenance surface supports soft or enforced verification, range or baseline
scope, remote note discovery, and release-action note recording. The recording
contract takes the pinned Attest and Augur binaries, a landed comparison range,
and an Augur JSON report; it signs a policy-satisfying note for the landed
commit and publishes the Attest ledger with merge-and-retry semantics.

## Invariants

1. Trust does not mint consumer provenance notes.
2. Missing notes degrade only when committed policy is soft.
3. Installation and runtime failures remain fatal in every mode.
4. Baseline verification does not change lifecycle, contract, or risk scope.
5. Concurrent remote notes are merged before publication.

## Behavioral Examples

```text
Given soft provenance and no remote Attest ledger
When Trust verifies a pull request
Then provenance is degraded
And lifecycle, contract, and risk still determine pass or failure
```

## Error Cases

| Error | Behavior |
| --- | --- |
| Missing ledger in enforced mode | Fail. |
| Invalid Attest report | Fail as an action/runtime error. |
| Concurrent note update | Fetch, merge, and retry publication. |

## Dependencies

- Git notes
- Attest 1.0.0
- Augur assessment metadata

## Change Log

| Date | Change |
| --- | --- |
| 2026-07-12 | Stable Trust 1.0 provenance contract. |
| 2026-07-13 | Map consumer verification and action provenance steps to the provenance contract. |
| 2026-07-13 | Document trusted SpecSync self-host inputs in the provenance contract. |
| 2026-07-13 | CHG-0005-close-trust-1-0-1-contract-validation-and-canonical-quality-gaps: Close Trust 1.0.1 contract validation and canonical quality gaps |
| 2026-07-18 | CHG-0009-adopt-specsync-5-1-1-as-the-pinned-contract-toolchain: Adopt SpecSync 5.1.1 as the pinned contract toolchain |
| 2026-07-18 | CHG-0010-narrow-trust-provenance-to-its-canonical-recording-surface: Narrow trust-provenance to its canonical recording surface |
