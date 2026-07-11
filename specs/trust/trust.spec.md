---
module: trust
version: 1
status: review
files:
  - bin/fledge-trust
  - action.yml
  - plugin.toml
  - templates/trust.yml

db_tables: []
depends_on: []
---

# Trust

## Purpose

CorvidLabs Trust provides one adoption and verification surface for fledge,
spec-sync, augur, attest, and optional Atlas without absorbing their engines or
forcing them into a shared release cycle.

## Public API

| Export | Description |
| --- | --- |
| `fledge trust adopt` | Conservatively add managed trust configuration to a git repository. |
| `fledge trust verify` | Run lifecycle, contract, risk, and provenance gates in order. |
| `fledge trust status` | Report installed tools and wired repository layers. |
| `fledge trust doctor` | Fail when required commands or repository configuration are missing. |
| `CorvidLabs/trust@v1` | Composite GitHub Action exposing the unified CI gate. |
| `name` | Human-readable action name. |
| `description` | Marketplace action summary. |
| `author` | Action publisher identity. |
| `branding` | Marketplace icon and color metadata. |
| `inputs` | Action input definitions. |
| `outputs` | Action output definitions. |
| `runs` | Composite action step declaration. |
| `inputs.profile` | Select standard or strict enforcement. |
| `inputs.range` | Select the git range for risk and provenance checks. |
| `inputs.working-directory` | Select the governed repository directory. |
| `inputs.verify-command` | Configure or disable lifecycle verification. |
| `inputs.fledge-version` | Pin the fallback Fledge installation. |
| `inputs.spec-sync-version` | Pin the SpecSync binary used by its action. |
| `inputs.spec-mode` | Enforce, soften, or disable the contract gate. |
| `inputs.require-coverage` | Set the minimum spec file coverage percentage. |
| `inputs.augur-threshold` | Set the fatal Augur verdict threshold. |
| `inputs.attest-mode` | Enforce, soften, or disable provenance verification. |
| `inputs.attest-policy` | Select the Attest policy path. |
| `outputs.verdict` | Expose the Augur verdict. |
| `outputs.risk` | Expose the Augur risk score. |
| `on` | Events used by the generated workflow. |
| `permissions` | Least-privilege permissions used by the generated workflow. |
| `jobs` | Generated workflow job definitions. |
| `permissions.contents` | Read-only repository content access. |
| `jobs.trust` | Generated unified trust job. |

## Invariants

1. Trust orchestrates existing tools and does not reimplement their engines.
2. Adoption never overwrites an existing project file unless the caller passes `--force`.
3. Adoption never replaces `AGENTS.md`; it appends one uniquely marked managed block.
4. Verification runs lifecycle, contract, risk, and provenance in that order.
5. An Augur block verdict is fatal and cannot be softened by a Trust profile.
6. Optional layers require explicit modes or skip reasons.
7. Machine-readable status includes `schemaVersion: 1`.
8. The strict profile cannot disable contract or provenance enforcement.
9. CI fetches the remote attestation ledger before provenance verification.

## Behavioral Examples

### Scenario: Adopt without overwriting project configuration

```text
Given a repository already has fledge.toml
When fledge trust adopt runs without --force
Then fledge.toml is preserved
And every missing managed file is created
```

### Scenario: Run the unified gate

```text
Given all four tools are installed and configured
When fledge trust verify --range origin/main..HEAD runs
Then the verify lane runs before specsync check
And augur gates the range before attest verifies its provenance
```

## Error Cases

| Error | Condition |
| --- | --- |
| Not a repository | `adopt` is run outside a git work tree. |
| Missing tool | A required verification layer is configured but its command is unavailable. |
| Missing verify lane | Lifecycle verification is enabled without `[lanes.verify]`. |
| Invalid option | A command receives an unknown flag or a skip option has no reason. |

## Dependencies

| Tool | Role |
| --- | --- |
| fledge | Lifecycle orchestration and plugin host. |
| spec-sync | Bidirectional contract validation. |
| augur | Deterministic diff-risk gate. |
| attest | Git-notes provenance policy gate. |
| atlas | Optional visualization and coverage publication. |

## Change Log

| Version | Date | Changes |
| --- | --- | --- |
| 1 | 2026-07-10 | Initial orchestration contract. |
