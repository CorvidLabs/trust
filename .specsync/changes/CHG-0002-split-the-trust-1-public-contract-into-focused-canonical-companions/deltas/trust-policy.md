## MODIFIED

### REQUIREMENT REQ-trust-policy-001

Trust SHALL reject unknown or weakening policy input.

Acceptance Criteria

- Invalid keys, invalid types, weaker profiles, and weaker thresholds fail closed.

### REQUIREMENT REQ-trust-policy-002

Trust SHALL derive pull-request ranges from canonical event and remote state.

Acceptance Criteria

- A missing, stale, or foreign base is rejected rather than guessed.

### REQUIREMENT REQ-trust-policy-003

Adoption SHALL preserve existing unmanaged repository content.

Acceptance Criteria

- Dry-run writes nothing and force is required before replacing existing managed files.

### REQUIREMENT REQ-trust-policy-004

Baseline pull requests SHALL fail when their event base is not the live remote branch tip.

Acceptance Criteria

- A stale base cannot satisfy protected-branch provenance policy.

### REQUIREMENT REQ-trust-policy-005

Pull requests SHALL NOT weaken or replace committed provenance policy contents.

Acceptance Criteria

- Policy comparison uses the protected base and fails on a weakening change.

### REQUIREMENT REQ-trust-policy-006

Pull request policy comparison SHALL fail closed when the base commit is unavailable.

Acceptance Criteria

- Missing history or fetch failure cannot degrade into a permissive policy result.

### REQUIREMENT REQ-trust-policy-007

The Trust CLI SHALL emit versioned, valid status JSON.

Acceptance Criteria

- Consumers can parse overall and component status without scraping logs; Action resolution exposes canonical component settings.
