---
spec: trust.spec.md
---

## User Stories

- As a maintainer, I want one command to adopt the CorvidLabs trust toolchain without losing existing configuration.
- As a contributor, I want one local command to reproduce the trust gate that CI runs.
- As an agent, I want deterministic status and stop conditions for every trust layer.
- As a team, I want the component tools to remain independently usable and releasable.

## Acceptance Criteria

- `adopt --dry-run` reports changes and writes nothing.
- Repeated adoption is idempotent.
- Existing files are preserved unless `--force` is passed.
- The managed AGENTS block is present exactly once.
- Verification runs lifecycle, contract, risk, and provenance in order.
- The composite action exposes Augur verdict and risk outputs.
- Status JSON is versioned and valid.
- CLI and status output report the plugin manifest version.
- Atlas publication is explicit opt-in and never runs for pull request events.
- Enabled Atlas policy is verified locally and published by the generated workflow on pushes.

## Constraints

- Shell behavior supports Bash 3.2 or newer on macOS and current Bash on Linux.
- GitHub Action inputs enter shell scripts through environment variables.
- The repository contains orchestration only, not copied component engines.

## Out of Scope

- Replacing the individual CLIs or GitHub Actions.
- Hosting a central policy service.
- Silently overriding block verdicts or provenance failures.
