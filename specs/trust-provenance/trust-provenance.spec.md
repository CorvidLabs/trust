---
module: trust-provenance
version: 2
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
scope, remote note discovery, and release-action note recording.

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

| Version | Date | Changes |
| --- | --- | --- |
| 1 | 2026-07-12 | Stable Trust 1.0 provenance contract. |
| 2026-07-12 | CHG-0002-split-the-trust-1-public-contract-into-focused-canonical-companions: Split the Trust 1 public contract into focused canonical companions |
