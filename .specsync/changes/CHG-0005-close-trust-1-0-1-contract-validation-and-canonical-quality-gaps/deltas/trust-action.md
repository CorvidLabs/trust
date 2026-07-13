## MODIFIED

### REQUIREMENT REQ-trust-action-002

The Trust action SHALL pin every nested composed component immutably.

Acceptance Criteria

- Nested SpecSync, Augur, Attest, Atlas, checkout, upload, and deployment actions resolve to reviewed release commits or checksummed binaries.
- Public generated workflow guidance may use the maintained Trust major channel; CorvidLabs consumer workflows use a reviewed immutable Trust release commit.

### REQUIREMENT REQ-trust-action-010

The Trust action SHALL allow a governed self-hosting workflow to select a checksummed SpecSync artifact without weakening the contract layer.

Acceptance Criteria

- Defaults select released SpecSync 5.0.1 and exact version input follows SemVer 2.0 numeric-identifier rules.
- A mirror override accepts only an authority-free local `file://` URL resolving to a directory strictly beneath `RUNNER_TEMP`.
- Canonical percent-encoding for safe path characters is accepted, while traversal, encoded separators, symlink escape, query, fragment, remote authority, and non-local schemes fail before lifecycle execution.
- The immutable nested SpecSync action receives only resolver-validated values.

### SPEC SECTION Change Log

| Date | Change |
| --- | --- |
| 2026-07-12 | Stable Trust 1.0 action contract. |
| 2026-07-13 | Keep release-only component exposure under the distribution contract. |
| 2026-07-13 | Add trusted SpecSync self-host artifact inputs. |
