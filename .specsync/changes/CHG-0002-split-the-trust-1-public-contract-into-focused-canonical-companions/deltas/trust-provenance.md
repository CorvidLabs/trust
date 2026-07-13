## MODIFIED

### REQUIREMENT REQ-trust-provenance-001

Trust SHALL classify missing policy evidence separately from component failure.

Acceptance Criteria

- Soft missing evidence degrades while installation, execution, and malformed reports fail.

### REQUIREMENT REQ-trust-provenance-002

Trust SHALL leave consumer note minting to independent signing workflows.

Acceptance Criteria

- The unified consumer action only fetches and verifies Attest notes.

### REQUIREMENT REQ-trust-provenance-003

Main provenance SHALL wait for the repository Trust gate and repair insufficient existing notes.

Acceptance Criteria

- Signing occurs only after a passing gate and produces policy-satisfying evidence.

### REQUIREMENT REQ-trust-provenance-004

Baseline provenance SHALL verify the protected base commit while lifecycle, contract, and risk gate the proposed range.

Acceptance Criteria

- Provenance scope and proposed-change scope remain explicit and independently reported.

### REQUIREMENT REQ-trust-provenance-005

Provenance scope changes SHALL be limited to a simultaneous soft-to-enforced baseline migration.

Acceptance Criteria

- A pull request cannot silently swap provenance scope without the associated policy transition.
