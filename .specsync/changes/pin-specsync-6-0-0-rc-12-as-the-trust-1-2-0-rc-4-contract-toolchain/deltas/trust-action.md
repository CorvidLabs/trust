## MODIFIED

### REQUIREMENT REQ-trust-action-010

The Trust action SHALL allow a governed self-hosting workflow to select a checksummed SpecSync artifact without weakening the contract layer.

Acceptance Criteria

- Defaults select SpecSync 6.0.0-rc.12. Any other exact SemVer version downloads from GitHub releases unless a validated local mirror is supplied, and all exact versions follow SemVer 2.0 numeric-identifier rules.
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
| `inputs.specsync-version` | Exact SpecSync version, defaulting to 6.0.0-rc.12. |
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
- SpecSync 6.0.0-rc.12
- Augur 1.0.0
- Attest 1.0.0

### SPEC SECTION Change Log

| Date | Change |
| --- | --- |
| 2026-07-12 | Stable Trust 1.0 action contract. |
| 2026-07-13 | Keep release-only component exposure under the distribution contract. |
| 2026-07-13 | Add trusted SpecSync self-host artifact inputs. |
| 2026-07-13 | CHG-0005-close-trust-1-0-1-contract-validation-and-canonical-quality-gaps: Close Trust 1.0.1 contract validation and canonical quality gaps |
| 2026-07-13 | CHG-0006-accept-canonical-windows-file-urls-for-trusted-specsync-mirrors: Accept canonical Windows file URLs for trusted SpecSync mirrors |
| 2026-07-13 | CHG-0007-harden-trusted-specsync-mirror-validation-before-lifecycle-execution: Harden trusted SpecSync mirror validation before lifecycle execution |
| 2026-07-13 | CHG-0008-revalidate-the-trusted-specsync-mirror-immediately-before-contract-consumption: Revalidate the trusted SpecSync mirror immediately before contract consumption |
| 2026-07-18 | CHG-0009-adopt-specsync-5-1-1-as-the-pinned-contract-toolchain: Adopt SpecSync 5.1.1 as the pinned contract toolchain |
| 2026-07-27 | Bump pinned SpecSync to 5.2.0 |
| 2026-08-27 | pin-specsync-6-0-0-rc-9-as-the-trust-1-2-0-rc-1-contract-toolchain: Pin SpecSync 6.0.0-rc.9 as the Trust 1.2.0-rc.1 contract toolchain |
| 2026-08-27 | pin-one-specsync-for-lifecycle-and-contract-and-allow-github-released-specsync-version-without-a-mirror: Pin one SpecSync for lifecycle and contract |
| 2026-09-01 | pin-specsync-6-0-0-rc-11-as-the-trust-1-2-0-rc-3-contract-toolchain: Pin SpecSync 6.0.0-rc.11 as the Trust 1.2.0-rc.3 contract toolchain |
| 2026-09-02 | pin-specsync-6-0-0-rc-12-as-the-trust-1-2-0-rc-4-contract-toolchain: Pin SpecSync 6.0.0-rc.12 as the Trust 1.2.0-rc.4 contract toolchain |
