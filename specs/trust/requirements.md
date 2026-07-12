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
- Tagged publication validates the Trust source contract with the pinned SpecSync release before exact-tag dogfooding.
- Exact-tag dogfooding exposes suffixed release assets through canonical `augur` and `attest` command names.
- Exact-tag dogfooding verifies an installed release against an enforced, satisfied baseline ledger.
- Main provenance waits for the repository Trust gate in the same workflow and repairs insufficient existing notes.
- The Homebrew bundle exposes `fledge-trust` as a concrete executable for Fledge PATH discovery.
- Baseline provenance verifies the protected base commit while lifecycle, contract, and risk gate the proposed range.
- Baseline pull requests fail when their event base is not the live remote branch tip.
- Provenance scope changes are limited to a simultaneous soft-to-enforced baseline migration.
- Pull requests cannot change the committed provenance policy contents.
- Pull request policy comparison fails closed when the base commit is unavailable.
- External governed worktrees ignore the host GitHub event and require an explicit range.
- GitHub event repository identity matches both server origin and owner/repository name.
- Native pull request comparisons are fixed to the event base and head commits.

## Constraints

- Shell behavior supports Bash 3.2 or newer on macOS and current Bash on Linux.
- GitHub Action inputs enter shell scripts through environment variables.
- The repository contains orchestration only, not copied component engines.

## Out of Scope

- Replacing the individual CLIs or GitHub Actions.
- Hosting a central policy service.
- Silently overriding block verdicts or provenance failures.
