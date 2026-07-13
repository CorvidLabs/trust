## ADDED

### REQUIREMENT REQ-trust-action-010

The Trust action SHALL allow a governed self-hosting workflow to select a checksummed SpecSync artifact without weakening the contract layer.

Acceptance Criteria

- Defaults select released SpecSync 5.0.1.
- A mirror override is accepted only as an authority-free local `file://` URL resolving beneath `RUNNER_TEMP`.
- Traversal, encoded traversal, symlink escape, remote authority, and non-local schemes fail before lifecycle execution.
- The immutable nested SpecSync action receives only resolver-validated values.

## MODIFIED

### SPEC SECTION Public API

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

### SPEC SECTION Invariants

1. Lifecycle runs before contract, risk, and provenance evaluation.
2. Contract and component actions use immutable released commits and binaries.
3. Soft provenance may degrade but never hides lifecycle, contract, or risk failure.
4. Atlas is disabled unless committed policy explicitly enables it.
5. Generated workflows keep Pages write permissions outside the Trust job.
6. SpecSync artifact overrides are local, checksummed, confined beneath `RUNNER_TEMP`, and resolved before lifecycle execution.
