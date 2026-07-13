---
module: trust
version: 3
status: active
files:
  - scripts/render_homebrew_formula.py
  - scripts/release_channel.py
  - scripts/expose_component_binaries.sh
  - .github/workflows/release.yml
  - packaging/homebrew/corvid-trust.rb.in

db_tables: []
depends_on: []
---

# Trust

## Purpose

CorvidLabs Trust provides one adoption and verification surface for fledge,
spec-sync, augur, attest, and optional Atlas without absorbing their engines or
forcing them into a shared release cycle.

## Public API

The distribution surface accepts semantic release tags and released checksums,
decides whether stable and major channels advance, and renders the
`corvid-trust` Homebrew formula containing Trust and SpecSync.

## Invariants

1. Stable and major channels advance only when the target version is newer.
2. Homebrew output pins the Trust and SpecSync versions and their checksums.
3. Distribution logic does not alter action, plugin, policy, or provenance behavior.

## Behavioral Examples

### Scenario: Advance a release channel

```text
Given v1 points to an older Trust release
When decision evaluates a newer v1 target
Then the major channel is marked for advancement
```

### Scenario: Render the Homebrew formula

```text
Given released Trust and SpecSync versions and checksums
When render builds the formula
Then the formula installs both components under the corvid-trust bundle
```

## Error Cases

| Error | Condition |
| --- | --- |
| Invalid tag | A release channel target is not semantic versioned. |
| Missing checksum | Formula rendering lacks a released asset checksum. |

## Dependencies

| Tool | Role |
| --- | --- |
| Python standard library | Version parsing and deterministic formula rendering. |

## Change Log

| Version | Date | Changes |
| --- | --- | --- |
| 1 | 2026-07-10 | Initial orchestration contract; corrected Action inputs and outputs before activation. |
| 1 | 2026-07-12 | Activate exact coverage and expose pinned release binaries under canonical command names. |
| 1 | 2026-07-12 | Split focused public contracts into dedicated companions. |
| 2026-07-12 | CHG-0002-split-the-trust-1-public-contract-into-focused-canonical-companions: Split the Trust 1 public contract into focused canonical companions |
| 3 | 2026-07-13 | Map release workflow, component exposure, and Homebrew formula artifacts to the distribution contract. |
