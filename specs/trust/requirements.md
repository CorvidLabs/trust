---
spec: trust.spec.md
---

## User Stories

- As a maintainer, I want one command to adopt the CorvidLabs trust toolchain without losing existing configuration.
- As a contributor, I want one local command to reproduce the trust gate that CI runs.
- As an agent, I want deterministic status and stop conditions for every trust layer.
- As a team, I want the component tools to remain independently usable and releasable.

## Acceptance Criteria

### REQ-trust-001

Tagged publication SHALL validate the Trust source contract with the pinned SpecSync release before exact-tag dogfooding.

Acceptance Criteria

- Release validation completes before installation tests use the new tag.

### REQ-trust-002

Exact-tag dogfooding SHALL expose suffixed release assets through canonical `augur` and `attest` command names.

Acceptance Criteria

- A tagged installation resolves and executes both component binaries.

### REQ-trust-003

Exact-tag dogfooding SHALL verify an installed release against an enforced, satisfied baseline ledger.

Acceptance Criteria

- The installed bundle passes its own Trust verification using tagged artifacts.

### REQ-trust-004

The Homebrew bundle SHALL expose `fledge-trust` as a concrete executable for Fledge PATH discovery.

Acceptance Criteria

- A fresh bundle installation exposes `fledge trust` without repository-local shims.

## Constraints

- Shell behavior supports Bash 3.2 or newer on macOS and current Bash on Linux.
- GitHub Action inputs enter shell scripts through environment variables.
- The repository contains orchestration only, not copied component engines.

## Out of Scope

- Replacing the individual CLIs or GitHub Actions.
- Hosting a central policy service.
- Silently overriding block verdicts or provenance failures.
