## MODIFIED

### REQUIREMENT REQ-trust-action-010

The Trust action SHALL allow a governed self-hosting workflow to select a checksummed SpecSync artifact without weakening the contract layer.

Acceptance Criteria

- Defaults select SpecSync 6.0.0-rc.9. Any other exact SemVer version downloads from GitHub releases unless a validated local mirror is supplied, and all exact versions follow SemVer 2.0 numeric-identifier rules.
- A mirror override accepts only an authority-free local `file://` URL resolving to a directory strictly beneath `RUNNER_TEMP` on Windows, Linux, and macOS.
- Canonical percent-encoding for safe path characters is accepted, while malformed URLs, traversal, encoded separators, query, fragment, remote authority, and non-local schemes fail before lifecycle execution.
- Every entry under the resolved mirror is non-symlinked and resolves beneath `RUNNER_TEMP` before lifecycle execution, then the same checks run again after lifecycle verification and immediately before contract consumption.
- The immutable nested SpecSync action receives only resolver-validated values.

## ADDED

### REQUIREMENT REQ-trust-action-011

The Trust action SHALL install the resolved SpecSync binary before lifecycle verification and SHALL use that binary for lifecycle.

Acceptance Criteria

- SpecSync is installed after policy resolution and Fledge, and before the lifecycle command.
- Lifecycle PATH prefers the Trust-pinned binary over any SpecSync already on the runner.
- A different SpecSync on PATH is reported and is not used for lifecycle.

## MODIFIED

### SPEC SECTION Invariants

1. Lifecycle runs before contract, risk, and provenance evaluation.
2. Contract and component actions use immutable released commits and binaries.
3. Soft provenance may degrade but never hides lifecycle, contract, or risk failure.
4. Atlas is disabled unless committed policy explicitly enables it.
5. Generated workflows keep Pages write permissions outside the Trust job.
6. SpecSync artifact overrides are local, checksummed, confined beneath `RUNNER_TEMP`, and resolved before lifecycle execution.
7. Lifecycle uses the same resolved SpecSync binary the contract step will use; runner PATH cannot select another SpecSync.

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
