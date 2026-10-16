## ADDED

### REQUIREMENT REQ-trust-action-013

Action policy resolution SHALL allow the exact equivalent legacy Attest schema repair before executing all existing gate layers.

Acceptance Criteria

- The exact approved conversion reaches lifecycle, contract, risk and provenance checks without changing their configuration.
- Every other changed provenance policy remains blocked before layer execution.

## MODIFIED

### SPEC SECTION Behavioral Examples

```text
Given a standard policy and a pull request range
When the Trust action runs
Then lifecycle, contract, and risk must pass
And missing provenance may report degraded rather than failed

Given the exact legacy Attest policy requiring attestation, reviewer and passing tests
When a pull request translates it to required attestations, passing tests and agent:/human: reviewers
Then policy resolution permits that equivalent translation
And still rejects weakened, ambiguous or unrelated policy changes
```
