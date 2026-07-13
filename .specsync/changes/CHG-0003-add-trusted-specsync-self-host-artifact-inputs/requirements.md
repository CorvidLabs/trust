---
change: CHG-0003-add-trusted-specsync-self-host-artifact-inputs
artifact: requirements
---

# Requirements

## REQ-trust-action-010

The Trust action SHALL allow a governed self-hosting workflow to select a checksummed SpecSync artifact without weakening the contract layer.

Acceptance Criteria

- Defaults select released SpecSync 5.0.1.
- A mirror override is accepted only as an authority-free local `file://` URL resolving beneath `RUNNER_TEMP`.
- Traversal, encoded traversal, symlink escape, remote authority, and non-local schemes fail before lifecycle execution.
- The immutable nested SpecSync action receives only resolver-validated values.
