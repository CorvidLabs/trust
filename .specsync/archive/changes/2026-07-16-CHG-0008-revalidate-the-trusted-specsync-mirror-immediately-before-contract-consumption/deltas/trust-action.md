## MODIFIED

### REQUIREMENT REQ-trust-action-010

The Trust action SHALL allow a governed self-hosting workflow to select a checksummed SpecSync artifact without weakening the contract layer.

Acceptance Criteria

- Defaults select released SpecSync 5.0.1; any other exact SemVer version requires a validated local mirror, and all exact versions follow SemVer 2.0 numeric-identifier rules.
- A mirror override accepts only an authority-free local `file://` URL resolving to a directory strictly beneath `RUNNER_TEMP` on Windows, Linux, and macOS.
- Canonical percent-encoding for safe path characters is accepted, while malformed URLs, traversal, encoded separators, query, fragment, remote authority, and non-local schemes fail before lifecycle execution.
- Every entry under the resolved mirror is non-symlinked and resolves beneath `RUNNER_TEMP` before lifecycle execution, then the same checks run again after lifecycle verification and immediately before contract consumption.
- The immutable nested SpecSync action receives only resolver-validated values.
