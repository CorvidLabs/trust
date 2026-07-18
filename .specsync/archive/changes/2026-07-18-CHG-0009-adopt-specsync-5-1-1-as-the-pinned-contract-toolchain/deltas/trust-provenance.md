## MODIFIED

### SPEC SECTION Public API

The provenance surface supports soft or enforced verification, range or baseline
scope, remote note discovery, and release-action note recording.

| Export | Description |
| --- | --- |
| `name` | Composite Trust action name. |
| `description` | Composite Trust action summary. |
| `author` | Action publisher. |
| `branding` | Marketplace presentation. |
| `inputs` | Public action input map. |
| `outputs` | Public action output map. |
| `runs` | Composite action implementation. |
| `inputs.config` | Committed Trust policy path. |
| `inputs.working-directory` | Governed repository directory. |
| `inputs.range` | Explicit comparison range override. |
| `inputs.profile` | Optional stricter profile override. |
| `inputs.augur-threshold` | Optional stricter risk threshold override. |
| `inputs.specsync-version` | Exact SpecSync version, defaulting to released 5.1.1. |
| `inputs.specsync-download-base-url` | Optional authority-free runner-local mirror URL for governed self-hosting. |
| `outputs.status` | Overall Trust result. |
| `outputs.range` | Canonical resolved comparison range. |
| `outputs.lifecycle-status` | Lifecycle component result. |
| `outputs.contract-status` | SpecSync component result. |
| `outputs.risk-status` | Augur component result. |
| `outputs.provenance-status` | Attest provenance component result. |
| `outputs.atlas-enabled` | Committed Atlas publication decision. |
| `outputs.verdict` | Augur verdict. |
| `outputs.risk` | Augur risk score. |
