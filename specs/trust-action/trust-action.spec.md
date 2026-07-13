---
module: trust-action
version: 7
status: stable
files:
  - action.yml
  - templates/trust.yml
  - scripts/trust_cli.py
  - scripts/normalize_specsync_cache.py
db_tables: []
depends_on: [trust-policy, trust-provenance]
---

# Trust GitHub Action

## Purpose

The released Trust action composes lifecycle verification, SpecSync contracts,
Augur risk, progressive Attest provenance, and optional Atlas publication.

## Public API

| Export | Description |
| --- | --- |
| `name` | Action or generated workflow name. |
| `description` | Marketplace action description. |
| `author` | Marketplace publisher. |
| `branding` | Marketplace presentation. |
| `inputs` | Action input map. |
| `outputs` | Action output map. |
| `runs` | Composite implementation. |
| `inputs.config` | Committed Trust policy path. |
| `inputs.working-directory` | Governed repository directory. |
| `inputs.range` | Optional explicit comparison range. |
| `inputs.profile` | Optional stricter profile override. |
| `inputs.augur-threshold` | Optional stricter risk threshold. |
| `inputs.specsync-version` | Exact SpecSync version, defaulting to released 5.0.1. |
| `inputs.specsync-download-base-url` | Optional authority-free runner-local mirror URL for governed self-hosting. |
| `outputs.status` | Overall passed, degraded, or failed status. |
| `outputs.range` | Canonical comparison range. |
| `outputs.lifecycle-status` | Lifecycle result. |
| `outputs.contract-status` | SpecSync result. |
| `outputs.risk-status` | Augur result. |
| `outputs.provenance-status` | Attest result. |
| `outputs.atlas-enabled` | Atlas publication decision. |
| `outputs.verdict` | Augur verdict. |
| `outputs.risk` | Augur risk score. |
| `on` | Generated workflow events. |
| `permissions` | Generated least-privilege permissions. |
| `jobs` | Generated workflow jobs. |
| `permissions.contents` | Repository read permission. |
| `permissions.pages` | Atlas Pages publication permission. |
| `permissions.id-token` | Atlas identity-token permission. |
| `jobs.trust` | Unified required job. |
| `jobs.deploy-atlas` | Conditional Atlas deployment job. |
| `outputs.atlas_enabled` | Cross-job Atlas decision. |

## Invariants

1. Lifecycle runs before contract, risk, and provenance evaluation.
2. Contract and component actions use immutable released commits and binaries.
3. Soft provenance may degrade but never hides lifecycle, contract, or risk failure.
4. Atlas is disabled unless committed policy explicitly enables it.
5. Generated workflows keep Pages write permissions outside the Trust job.
6. SpecSync artifact overrides are local, checksummed, confined beneath `RUNNER_TEMP`, and resolved before lifecycle execution.

## Behavioral Examples

```text
Given a standard policy and a pull request range
When the Trust action runs
Then lifecycle, contract, and risk must pass
And missing provenance may report degraded rather than failed
```

## Error Cases

| Error | Behavior |
| --- | --- |
| Invalid policy | Fail before installing or running component gates. |
| Contract drift | Fail the overall action. |
| Component installation failure | Fail rather than classify the policy as unsatisfied. |

## Dependencies

- Fledge 1.7.0
- SpecSync 5.0.1
- Augur 1.0.0
- Attest 1.0.0

## Change Log

| Date | Change |
| --- | --- |
| 2026-07-12 | Stable Trust 1.0 action contract. |
| 2026-07-13 | Keep release-only component exposure under the distribution contract. |
| 2026-07-13 | Add trusted SpecSync self-host artifact inputs. |
| 2026-07-13 | CHG-0005-close-trust-1-0-1-contract-validation-and-canonical-quality-gaps: Close Trust 1.0.1 contract validation and canonical quality gaps |
