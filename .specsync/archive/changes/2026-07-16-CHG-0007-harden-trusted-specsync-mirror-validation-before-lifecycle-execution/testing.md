---
change: CHG-0007-harden-trusted-specsync-mirror-validation-before-lifecycle-execution
artifact: testing
---

# Testing

- Run `fledge lanes run verify` for syntax, manifest validation, and the full native shell test suite.
- Exercise an unmatched IPv6 bracket and assert it is translated into `TrustError`.
- Reject stable and prerelease non-default exact versions when no mirror is supplied.
- Accept those versions when their local mirror is valid.
- Reject a file symlink inside a valid mirror, including when its target exists outside `RUNNER_TEMP`.
- Run strict SpecSync verification and record immutable lifecycle evidence before acceptance.
