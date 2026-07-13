---
id: CHG-0003-add-trusted-specsync-self-host-artifact-inputs
state: implementing
type: feature
base_commit: 2ede269961e37951a99bd3a5cd2f3424a6d430f8
---

# Add trusted SpecSync self-host artifact inputs

## Intent

Add trusted SpecSync self-host artifact inputs

## Affected Canonical Specs

- `trust-action`

## Acceptance Criteria

- Trust exposes SpecSync version and download-base inputs with released 5.0.1 defaults; only an empty mirror or a canonical local file URL confined beneath RUNNER_TEMP is accepted; invalid authority
- traversal
- symlink escape
- and non-local schemes fail before lifecycle execution; the nested immutable SpecSync action receives validated values; manifest and runtime regressions pass

## No-spec Rationale

Not applicable
