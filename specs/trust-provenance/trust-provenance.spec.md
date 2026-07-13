---
module: trust-provenance
version: 5
status: stable
files:
  - scripts/record_provenance.sh
  - scripts/trust_cli.py
  - action.yml
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

| Export | Description |
| --- | --- |
| `name` | Composite Trust action name. |
| `description` | Composite Trust action summary. |
| `author` | Action publisher. |
| `branding` | Marketplace presentation. |
| `inputs` | Public action input map. |
| `outputs` | Public action output map. |
| `runs` | Composite action implementation. |
| `inputs.config` | Committed Trust policy path. |
| `inputs.working-directory` | Governed repository directory. |
| `inputs.range` | Explicit comparison range override. |
| `inputs.profile` | Optional stricter profile override. |
| `inputs.augur-threshold` | Optional stricter risk threshold override. |
| `outputs.status` | Overall Trust result. |
| `outputs.range` | Canonical resolved comparison range. |
| `outputs.lifecycle-status` | Lifecycle component result. |
| `outputs.contract-status` | SpecSync component result. |
| `outputs.risk-status` | Augur component result. |
| `outputs.provenance-status` | Attest provenance component result. |
| `outputs.atlas-enabled` | Committed Atlas publication decision. |
| `outputs.verdict` | Augur verdict. |
| `outputs.risk` | Augur risk score. |

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
| 3 | 2026-07-13 | Map consumer verification and action provenance steps to the provenance contract. |
| 2026-07-13 | CHG-0002-split-the-trust-1-public-contract-into-focused-canonical-companions: Split the Trust 1 public contract into focused canonical companions |
| 2026-07-13 | CHG-0002-split-the-trust-1-public-contract-into-focused-canonical-companions: Split the Trust 1 public contract into focused canonical companions |
