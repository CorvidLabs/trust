---
spec: trust-provenance.spec.md
---

## Acceptance Criteria

### REQ-trust-provenance-001

Trust SHALL classify missing policy evidence separately from component failure.

Acceptance Criteria

- Soft missing evidence degrades while installation, execution, and malformed reports fail.

### REQ-trust-provenance-002

Trust SHALL leave consumer note minting to independent signing workflows.

Acceptance Criteria

- The unified consumer action only fetches and verifies Attest notes.
