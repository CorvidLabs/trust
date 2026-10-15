## ADDED

### REQUIREMENT REQ-trust-policy-008

Trust SHALL accept only the exact equivalent legacy Attest schema translation while retaining rejection of unrelated committed-policy changes.

Acceptance Criteria

- The protected-base policy is exactly the legacy require object with attestation, reviewer and testsPassed all true.
- The proposed policy requires attestations and passing tests and allows only agent: and human: reviewer roles.
- Unknown or duplicate keys, missing rules, false values, numeric boolean substitutes, malformed JSON, reverse migrations and unrelated policy changes fail closed.

## MODIFIED

### SPEC SECTION Invariants

1. Unknown policy keys fail closed.
2. Strict policy cannot be downgraded by inputs or pull-request changes.
3. Native PR ranges exactly match the event base-to-head comparison.
4. External worktrees require explicit ranges.
5. Adoption preserves unmanaged content unless force is explicit.
6. Changed provenance policy bytes are rejected except for the exact one-way equivalent legacy Attest schema repair; every legacy requirement remains represented.
