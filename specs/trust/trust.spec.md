---
module: trust
version: 1
status: active
files:
  - bin/fledge-trust
  - scripts/trust_cli.py
  - scripts/validate.py
  - scripts/expose_component_binaries.sh
  - scripts/normalize_specsync_cache.py
  - scripts/release_channel.py
  - scripts/record_provenance.sh
  - scripts/render_homebrew_formula.py
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
| `name` | Human-readable action name. |
| `description` | Marketplace action summary. |
| `author` | Action publisher identity. |
| `branding` | Marketplace icon and color metadata. |
| `inputs` | Action input definitions. |
| `outputs` | Action output definitions. |
| `runs` | Composite action step declaration. |
| `inputs.config` | Select the committed Trust policy path. |
| `inputs.profile` | Select standard or strict enforcement. |
| `inputs.range` | Select the git range for risk and provenance checks. |
| `inputs.working-directory` | Select the governed repository directory. |
| `inputs.augur-threshold` | Set the fatal Augur verdict threshold. |
| `outputs.status` | Expose the overall passed, degraded, or failed status. |
| `outputs.range` | Expose the resolved git comparison range. |
| `outputs.lifecycle-status` | Expose the lifecycle gate status. |
| `outputs.contract-status` | Expose the contract gate status. |
| `outputs.risk-status` | Expose the deterministic risk gate status. |
| `outputs.provenance-status` | Expose the provenance gate status. |
| `outputs.atlas-enabled` | Expose the committed Atlas publication decision. |
| `outputs.verdict` | Expose the Augur verdict. |
| `outputs.risk` | Expose the Augur risk score. |
| `on` | Events used by the generated workflow. |
| `permissions` | Least-privilege permissions used by the generated workflow. |
| `jobs` | Generated workflow job definitions. |
| `permissions.contents` | Read-only repository content access. |
| `permissions.pages` | Allow the generated Atlas deployment job to publish Pages. |
| `permissions.id-token` | Allow the generated Atlas deployment job to request an identity token. |
| `jobs.trust` | Generated unified trust job. |
| `jobs.deploy-atlas` | Generated push-only Atlas deployment job. |
| `outputs.atlas_enabled` | Pass the Atlas policy decision between generated workflow jobs. |

## User-facing Surface

| Command or Action | Description |
| --- | --- |
| `fledge trust adopt` | Conservatively add managed trust configuration to a git repository. |
| `fledge trust verify` | Run lifecycle, contract, risk, and provenance gates in order. |
| `fledge trust status` | Report installed tools and wired repository layers. |
| `fledge trust doctor` | Fail when required commands or repository configuration are missing. |
| `fledge trust --version` | Report the installed Trust plugin version. |
| `fledge trust adopt --atlas` | Opt into Atlas verification and Pages publication. |
| `CorvidLabs/trust@v0` | Composite GitHub Action exposing the unified CI gate. |

## Invariants

1. Trust orchestrates existing tools and does not reimplement their engines.
2. Adoption never overwrites an existing project file unless the caller passes `--force`.
3. Adoption preserves surrounding `AGENTS.md` content while appending or updating one uniquely marked managed block.
4. Verification runs lifecycle, contract, risk, provenance, and optional Atlas in that order.
5. An Augur block verdict is fatal and cannot be softened by a Trust profile.
6. Optional layers require explicit modes or skip reasons.
7. Machine-readable status includes `schemaVersion: 1`.
8. The strict profile cannot disable contract or provenance enforcement.
9. CI fetches the remote attestation ledger before provenance verification.
10. Status JSON reports the Trust plugin version from `plugin.toml`.
11. Atlas is disabled by default and requires explicit adoption plus a recorded `.atlasignore`.
12. Generated workflows publish Atlas only for pushes and isolate Pages write permissions to the deployment job.
13. Baseline provenance verifies the range base without changing the lifecycle, contract, or risk comparison.
14. Provenance scope can change only during a simultaneous soft-to-enforced baseline migration.
15. Pull requests cannot change the committed provenance policy contents.
16. Pull request policy comparison fails when the base commit object is unavailable.
17. Baseline pull requests fail unless their event base matches the live remote branch tip.

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
And augur gates the range before attest verifies the configured changes or baseline scope
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
| 1 | 2026-07-10 | Initial orchestration contract; corrected Action inputs and outputs before activation. |
| 1 | 2026-07-12 | Activate exact coverage and expose pinned release binaries under canonical command names. |
