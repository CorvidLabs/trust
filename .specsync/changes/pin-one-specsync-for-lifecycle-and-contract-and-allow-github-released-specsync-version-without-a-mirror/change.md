---
id: pin-one-specsync-for-lifecycle-and-contract-and-allow-github-released-specsync-version-without-a-mirror
state: implementing
type: bug_fix
base_commit: e964e042f7f2756333d4c46e685a4a6dc09077de
---

# Pin one SpecSync for lifecycle and contract and allow GitHub-released specsync-version without a mirror

## Intent

Pin one SpecSync for lifecycle and contract and allow GitHub-released specsync-version without a mirror

## Affected Canonical Specs

- `trust-action`

## Acceptance Criteria

- The Trust action installs the resolved SpecSync binary before lifecycle and prepends it to PATH, so lifecycle and contract use the same pin. A PATH SpecSync that is not that binary is ignored with a warning. Exact specsync-version values download from GitHub releases without a local mirror; file:// mirrors remain for self-host. tests/test.sh and fledge lanes run verify pass.

## No-spec Rationale

Not applicable
