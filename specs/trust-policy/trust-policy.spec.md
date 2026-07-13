---
module: trust-policy
version: 4
status: stable
files:
  - scripts/trust_cli.py
  - scripts/validate.py
  - .trust.toml
  - .attest.json
  - .augur.toml
  - AGENTS.md
  - templates/trust.toml
  - templates/attest.json
  - templates/augur.toml
  - templates/agents-rules.md
db_tables: []
depends_on: []
---

# Trust Policy Resolution

## Purpose

Trust policy resolution parses committed configuration, validates repository
context, prevents enforcement downgrades, and derives canonical comparison ranges.

## Public API

The policy surface provides adoption, status, doctor, local verification, and
composite-action resolution. It accepts a committed policy path, optional
explicit range, and only stricter profile or risk overrides. Machine status is
schema-versioned and Action resolution emits the canonical component settings.

## Invariants

1. Unknown policy keys fail closed.
2. Strict policy cannot be downgraded by inputs or pull-request changes.
3. Native PR ranges exactly match the event base-to-head comparison.
4. External worktrees require explicit ranges.
5. Adoption preserves unmanaged content unless force is explicit.

## Behavioral Examples

```text
Given a committed standard policy
When a pull request supplies a stricter risk threshold
Then policy resolution accepts the override
But rejects any attempt to disable contract or provenance enforcement
```

## Error Cases

| Error | Behavior |
| --- | --- |
| Unknown key or type | Reject the policy. |
| Missing base object | Fail pull-request comparison. |
| Mismatched event repository | Require an explicit range. |
| Existing unmanaged file | Preserve it unless force is passed. |

## Dependencies

- Python standard library
- Git
- Fledge, SpecSync, Augur, and Attest executables when enabled

## Change Log

| Version | Date | Changes |
| --- | --- | --- |
| 1 | 2026-07-12 | Stable Trust 1.0 policy contract. |
| 2026-07-12 | CHG-0002-split-the-trust-1-public-contract-into-focused-canonical-companions: Split the Trust 1 public contract into focused canonical companions |
| 3 | 2026-07-13 | Map committed policies, generated defaults, managed rules, and status JSON to policy resolution. |
| 2026-07-13 | CHG-0002-split-the-trust-1-public-contract-into-focused-canonical-companions: Split the Trust 1 public contract into focused canonical companions |
