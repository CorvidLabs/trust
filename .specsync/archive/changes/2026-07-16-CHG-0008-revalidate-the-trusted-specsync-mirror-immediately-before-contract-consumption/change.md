---
id: CHG-0008-revalidate-the-trusted-specsync-mirror-immediately-before-contract-consumption
state: archived
type: bug_fix
base_commit: d34acd9d206291dd9d337a427db6f1fd137eb544
---

# Revalidate the trusted SpecSync mirror immediately before contract consumption

## Intent

Revalidate the trusted SpecSync mirror immediately before contract consumption

## Affected Canonical Specs

- `trust-action`

## Acceptance Criteria

- The composite action revalidates any configured runner-local SpecSync mirror after lifecycle verification and immediately before the pinned contract action; a regression proves lifecycle-time symlink replacement is rejected before contract consumption; native verification
- strict SpecSync validation
- and the hosted Linux/macOS/Windows action matrix pass.

## No-spec Rationale

Not applicable
