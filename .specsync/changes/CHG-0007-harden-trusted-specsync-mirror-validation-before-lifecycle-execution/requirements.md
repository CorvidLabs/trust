---
change: CHG-0007-harden-trusted-specsync-mirror-validation-before-lifecycle-execution
artifact: requirements
---

# Requirements

- The empty mirror input SHALL be valid only for the released default SpecSync version `5.0.1`.
- Any other exact SemVer version SHALL require a validated local mirror.
- Malformed local mirror URLs SHALL produce a clean `TrustError` before lifecycle execution.
- Every entry recursively contained by a local mirror SHALL be non-symlinked and resolve beneath `RUNNER_TEMP` before lifecycle execution.
- Existing version, URL, directory, traversal, percent-encoding, and boundary checks SHALL remain enforced.
