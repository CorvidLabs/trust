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
