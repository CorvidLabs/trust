---
id: CHG-0006-accept-canonical-windows-file-urls-for-trusted-specsync-mirrors
state: archived
type: bug_fix
base_commit: 1677ec3f68e5d07352f19b7fbe643d516675bc19
---

# Accept canonical Windows file URLs for trusted SpecSync mirrors

## Intent

Accept canonical Windows file URLs for trusted SpecSync mirrors

## Affected Canonical Specs

- `trust-action`

## Acceptance Criteria

- Canonical authority-free Windows file URLs produced by Path.as_uri resolve to their native absolute paths and remain confined strictly beneath RUNNER_TEMP
- Linux and macOS behavior remains unchanged
- every existing invalid authority traversal encoded-separator control symlink outside root and missing-path case remains rejected
- the Windows plugin behavior matrix and full Trust release lane pass.

## No-spec Rationale

Not applicable
