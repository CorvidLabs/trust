---
spec: trust-action.spec.md
---

## Acceptance Criteria

### REQ-trust-action-001

The Trust action SHALL expose stable component and overall status outputs.

Acceptance Criteria

- Every released input and output in action.yml is documented and validated.

### REQ-trust-action-002

The Trust action SHALL pin every nested composed component immutably.

Acceptance Criteria

- Nested SpecSync, Augur, Attest, Atlas, checkout, upload, and deployment actions resolve to reviewed release commits or checksummed binaries.
- Public generated workflow guidance may use the maintained Trust major channel; CorvidLabs consumer workflows use a reviewed immutable Trust release commit.

### REQ-trust-action-003

The generated workflow SHALL keep the required job name trust.

Acceptance Criteria

- Pull requests always post trust and optional Atlas publication remains push-only.

### REQ-trust-action-004

Verification SHALL run lifecycle, contract, risk, and provenance in order.

Acceptance Criteria

- A failed earlier layer cannot be hidden by a later component result.

### REQ-trust-action-006

Atlas publication SHALL require explicit policy opt-in and SHALL NOT run for pull request events.

Acceptance Criteria

- Enabled Atlas policy verifies locally and publishes only from the generated push workflow.

### REQ-trust-action-007

External governed worktrees SHALL ignore the host GitHub event and require an explicit range.

Acceptance Criteria

- Event-derived ranges are used only when the event repository matches the governed origin.

### REQ-trust-action-008

GitHub event repository identity SHALL match both server origin and owner/repository name.

Acceptance Criteria

- Foreign or mismatched event context is rejected rather than trusted.

### REQ-trust-action-009

Native pull request comparisons SHALL be fixed to the event base and head commits.

Acceptance Criteria

- The action does not silently widen or move a pull request comparison.

### REQ-trust-action-010

The Trust action SHALL allow a governed self-hosting workflow to select a checksummed SpecSync artifact without weakening the contract layer.

Acceptance Criteria

- Defaults select released SpecSync 5.0.1; any other exact SemVer version requires a validated local mirror, and all exact versions follow SemVer 2.0 numeric-identifier rules.
- A mirror override accepts only an authority-free local `file://` URL resolving to a directory strictly beneath `RUNNER_TEMP` on Windows, Linux, and macOS.
- Canonical percent-encoding for safe path characters is accepted, while malformed URLs, traversal, encoded separators, query, fragment, remote authority, and non-local schemes fail before lifecycle execution.
- Every entry under the resolved mirror is non-symlinked and resolves beneath `RUNNER_TEMP` before lifecycle execution, then the same checks run again after lifecycle verification and immediately before contract consumption.
- The immutable nested SpecSync action receives only resolver-validated values.

