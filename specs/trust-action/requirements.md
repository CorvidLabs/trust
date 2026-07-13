---
spec: trust-action.spec.md
---

## Acceptance Criteria

### REQ-trust-action-001

The Trust action SHALL expose stable component and overall status outputs.

Acceptance Criteria

- Every released input and output in action.yml is documented and validated.

### REQ-trust-action-002

The Trust action SHALL pin every composed component immutably.

Acceptance Criteria

- Trust, SpecSync, Augur, Attest, and Fledge resolve to reviewed release commits or checksummed binaries.

### REQ-trust-action-003

The generated workflow SHALL keep the required job name trust.

Acceptance Criteria

- Pull requests always post trust and optional Atlas publication remains push-only.

### REQ-trust-action-004

Verification SHALL run lifecycle, contract, risk, and provenance in order.

Acceptance Criteria

- A failed earlier layer cannot be hidden by a later component result.

### REQ-trust-action-006

Atlas publication SHALL require explicit policy opt-in and SHALL NOT run for pull request events.

Acceptance Criteria

- Enabled Atlas policy verifies locally and publishes only from the generated push workflow.

### REQ-trust-action-007

External governed worktrees SHALL ignore the host GitHub event and require an explicit range.

Acceptance Criteria

- Event-derived ranges are used only when the event repository matches the governed origin.

### REQ-trust-action-008

GitHub event repository identity SHALL match both server origin and owner/repository name.

Acceptance Criteria

- Foreign or mismatched event context is rejected rather than trusted.

### REQ-trust-action-009

Native pull request comparisons SHALL be fixed to the event base and head commits.

Acceptance Criteria

- The action does not silently widen or move a pull request comparison.
