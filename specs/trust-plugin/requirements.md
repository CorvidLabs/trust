---
spec: trust-plugin.spec.md
---

## Acceptance Criteria

### REQ-trust-plugin-001

The plugin SHALL expose Trust through the Fledge command registry.

Acceptance Criteria

- A fresh tagged installation makes fledge trust available.

### REQ-trust-plugin-002

The launcher SHALL forward arguments and exit status without reinterpretation.

Acceptance Criteria

- Plugin behavior tests cover success, invalid input, and missing dependency paths.
