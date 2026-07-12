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

Trust SHALL ensure the following: `adopt --dry-run` reports changes and writes nothing.

Acceptance Criteria

- `adopt --dry-run` reports changes and writes nothing.
### REQ-trust-002

Trust SHALL ensure the following: Repeated adoption is idempotent.

Acceptance Criteria

- Repeated adoption is idempotent.
### REQ-trust-003

Trust SHALL ensure the following: Existing files are preserved unless `--force` is passed.

Acceptance Criteria

- Existing files are preserved unless `--force` is passed.
### REQ-trust-004

Trust SHALL ensure the following: The managed AGENTS block is present exactly once.

Acceptance Criteria

- The managed AGENTS block is present exactly once.
### REQ-trust-005

Trust SHALL ensure the following: Verification runs lifecycle, contract, risk, and provenance in order.

Acceptance Criteria

- Verification runs lifecycle, contract, risk, and provenance in order.
### REQ-trust-006

Trust SHALL ensure the following: The composite action exposes Augur verdict and risk outputs.

Acceptance Criteria

- The composite action exposes Augur verdict and risk outputs.
### REQ-trust-007

Trust SHALL ensure the following: Status JSON is versioned and valid.

Acceptance Criteria

- Status JSON is versioned and valid.
### REQ-trust-008

Trust SHALL ensure the following: CLI and status output report the plugin manifest version.

Acceptance Criteria

- CLI and status output report the plugin manifest version.
### REQ-trust-009

Trust SHALL ensure the following: Atlas publication is explicit opt-in and never runs for pull request events.

Acceptance Criteria

- Atlas publication is explicit opt-in and never runs for pull request events.
### REQ-trust-010

Trust SHALL ensure the following: Enabled Atlas policy is verified locally and published by the generated workflow on pushes.

Acceptance Criteria

- Enabled Atlas policy is verified locally and published by the generated workflow on pushes.
### REQ-trust-011

Trust SHALL ensure the following: Tagged publication validates the Trust source contract with the pinned SpecSync release before exact-tag dogfooding.

Acceptance Criteria

- Tagged publication validates the Trust source contract with the pinned SpecSync release before exact-tag dogfooding.
### REQ-trust-012

Trust SHALL ensure the following: Exact-tag dogfooding exposes suffixed release assets through canonical `augur` and `attest` command names.

Acceptance Criteria

- Exact-tag dogfooding exposes suffixed release assets through canonical `augur` and `attest` command names.
### REQ-trust-013

Trust SHALL ensure the following: Exact-tag dogfooding verifies an installed release against an enforced, satisfied baseline ledger.

Acceptance Criteria

- Exact-tag dogfooding verifies an installed release against an enforced, satisfied baseline ledger.
### REQ-trust-014

Trust SHALL ensure the following: Main provenance waits for the repository Trust gate in the same workflow and repairs insufficient existing notes.

Acceptance Criteria

- Main provenance waits for the repository Trust gate in the same workflow and repairs insufficient existing notes.
### REQ-trust-015

Trust SHALL ensure the following: The Homebrew bundle exposes `fledge-trust` as a concrete executable for Fledge PATH discovery.

Acceptance Criteria

- The Homebrew bundle exposes `fledge-trust` as a concrete executable for Fledge PATH discovery.
### REQ-trust-016

Trust SHALL ensure the following: Baseline provenance verifies the protected base commit while lifecycle, contract, and risk gate the proposed range.

Acceptance Criteria

- Baseline provenance verifies the protected base commit while lifecycle, contract, and risk gate the proposed range.
### REQ-trust-017

Trust SHALL ensure the following: Baseline pull requests fail when their event base is not the live remote branch tip.

Acceptance Criteria

- Baseline pull requests fail when their event base is not the live remote branch tip.
### REQ-trust-018

Trust SHALL ensure the following: Provenance scope changes are limited to a simultaneous soft-to-enforced baseline migration.

Acceptance Criteria

- Provenance scope changes are limited to a simultaneous soft-to-enforced baseline migration.
### REQ-trust-019

Trust SHALL ensure the following: Pull requests cannot change the committed provenance policy contents.

Acceptance Criteria

- Pull requests cannot change the committed provenance policy contents.
### REQ-trust-020

Trust SHALL ensure the following: Pull request policy comparison fails closed when the base commit is unavailable.

Acceptance Criteria

- Pull request policy comparison fails closed when the base commit is unavailable.
### REQ-trust-021

Trust SHALL ensure the following: External governed worktrees ignore the host GitHub event and require an explicit range.

Acceptance Criteria

- External governed worktrees ignore the host GitHub event and require an explicit range.
### REQ-trust-022

Trust SHALL ensure the following: GitHub event repository identity matches both server origin and owner/repository name.

Acceptance Criteria

- GitHub event repository identity matches both server origin and owner/repository name.
### REQ-trust-023

Trust SHALL ensure the following: Native pull request comparisons are fixed to the event base and head commits.

Acceptance Criteria

- Native pull request comparisons are fixed to the event base and head commits.

## Constraints

- Shell behavior supports Bash 3.2 or newer on macOS and current Bash on Linux.
- GitHub Action inputs enter shell scripts through environment variables.
- The repository contains orchestration only, not copied component engines.

## Out of Scope

- Replacing the individual CLIs or GitHub Actions.
- Hosting a central policy service.
- Silently overriding block verdicts or provenance failures.
