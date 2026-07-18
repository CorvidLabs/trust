## MODIFIED

### REQUIREMENT REQ-trust-action-010

The Trust action SHALL allow a governed self-hosting workflow to select a checksummed SpecSync artifact without weakening the contract layer.

Acceptance Criteria

- Defaults select released SpecSync 5.1.1; any other exact SemVer version requires a validated local mirror, and all exact versions follow SemVer 2.0 numeric-identifier rules.
- A mirror override accepts only an authority-free local `file://` URL resolving to a directory strictly beneath `RUNNER_TEMP` on Windows, Linux, and macOS.
- Canonical percent-encoding for safe path characters is accepted, while malformed URLs, traversal, encoded separators, query, fragment, remote authority, and non-local schemes fail before lifecycle execution.
- Every entry under the resolved mirror is non-symlinked and resolves beneath `RUNNER_TEMP` before lifecycle execution, then the same checks run again after lifecycle verification and immediately before contract consumption.
- The immutable nested SpecSync action receives only resolver-validated values.

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
| `inputs.specsync-version` | Exact SpecSync version, defaulting to released 5.1.1. |
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

### SPEC SECTION Dependencies

- Fledge 1.7.0
- SpecSync 5.1.1
- Augur 1.0.0
- Attest 1.0.0
