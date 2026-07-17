---
id: CHG-0007-harden-trusted-specsync-mirror-validation-before-lifecycle-execution
state: archived
type: bug_fix
base_commit: 1c7b2c43f44b256570a8a5a5bfbd4c4c224f1560
---

# Harden trusted SpecSync mirror validation before lifecycle execution

## Intent

Harden trusted SpecSync mirror validation before lifecycle execution

## Affected Canonical Specs

- `trust-action`

## Acceptance Criteria

- Malformed mirror URLs fail with a clean TrustError; empty mirror URLs accept only released default SpecSync 5.0.1; non-default exact SemVer requires a validated local mirror; every entry under a resolved mirror is non-symlinked and resolves beneath RUNNER_TEMP before lifecycle execution; regression tests cover malformed IPv6
- non-default versions without mirrors
- and file symlink escape

## No-spec Rationale

Not applicable
