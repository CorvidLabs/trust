---
spec: trust-policy.spec.md
---

## Acceptance Criteria

### REQ-trust-policy-001

Trust SHALL reject unknown or weakening policy input.

Acceptance Criteria

- Invalid keys, invalid types, weaker profiles, and weaker thresholds fail closed.

### REQ-trust-policy-002

Trust SHALL derive pull-request ranges from canonical event and remote state.

Acceptance Criteria

- A missing, stale, or foreign base is rejected rather than guessed.

### REQ-trust-policy-003

Adoption SHALL preserve existing unmanaged repository content.

Acceptance Criteria

- Dry-run writes nothing and force is required before replacing existing managed files.
