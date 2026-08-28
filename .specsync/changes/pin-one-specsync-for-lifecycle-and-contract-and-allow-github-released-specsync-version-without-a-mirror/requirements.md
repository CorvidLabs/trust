---
change: pin-one-specsync-for-lifecycle-and-contract-and-allow-github-released-specsync-version-without-a-mirror
artifact: requirements
---

# Requirements

### REQ-trust-action-010

The Trust action SHALL allow a governed self-hosting workflow to select a checksummed SpecSync artifact without weakening the contract layer.

Acceptance Criteria

- Defaults select SpecSync 6.0.0-rc.9. Any other exact SemVer version downloads from GitHub releases unless a validated local mirror is supplied, and all exact versions follow SemVer 2.0 numeric-identifier rules.
- A mirror override accepts only an authority-free local `file://` URL resolving to a directory strictly beneath `RUNNER_TEMP` on Windows, Linux, and macOS.
- Canonical percent-encoding for safe path characters is accepted, while malformed URLs, traversal, encoded separators, query, fragment, remote authority, and non-local schemes fail before lifecycle execution.
- Every entry under the resolved mirror is non-symlinked and resolves beneath `RUNNER_TEMP` before lifecycle execution, then the same checks run again after lifecycle verification and immediately before contract consumption.
- The immutable nested SpecSync action receives only resolver-validated values.

### REQ-trust-action-011

The Trust action SHALL install the resolved SpecSync binary before lifecycle verification and SHALL use that binary for lifecycle.

Acceptance Criteria

- SpecSync is installed after policy resolution and Fledge, and before the lifecycle command.
- Lifecycle PATH prefers the Trust-pinned binary over any SpecSync already on the runner.
- A different SpecSync on PATH is reported and is not used for lifecycle.
