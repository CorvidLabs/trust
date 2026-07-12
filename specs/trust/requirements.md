---
spec: trust.spec.md
---

## User Stories

- As a maintainer, I want one command to adopt the CorvidLabs trust toolchain without losing existing configuration.
- As a contributor, I want one local command to reproduce the trust gate that CI runs.
- As an agent, I want deterministic status and stop conditions for every trust layer.
- As a team, I want the component tools to remain independently usable and releasable.

## Durable Requirements

### REQ-trust-001

The implementation SHALL satisfy the following criterion: `adopt --dry-run` reports changes and writes nothing.

Acceptance Criteria

- `adopt --dry-run` reports changes and writes nothing.

### REQ-trust-002

The implementation SHALL satisfy the following criterion: Repeated adoption is idempotent.

Acceptance Criteria

- Repeated adoption is idempotent.

### REQ-trust-003

The implementation SHALL satisfy the following criterion: Existing files are preserved unless `--force` is passed.

Acceptance Criteria

- Existing files are preserved unless `--force` is passed.

### REQ-trust-004

The implementation SHALL satisfy the following criterion: The managed AGENTS block is present exactly once.

Acceptance Criteria

- The managed AGENTS block is present exactly once.

### REQ-trust-005

The implementation SHALL satisfy the following criterion: Verification runs lifecycle, contract, risk, and provenance in order.

Acceptance Criteria

- Verification runs lifecycle, contract, risk, and provenance in order.

### REQ-trust-006

The implementation SHALL satisfy the following criterion: The composite action exposes Augur verdict and risk outputs.

Acceptance Criteria

- The composite action exposes Augur verdict and risk outputs.

### REQ-trust-007

The implementation SHALL satisfy the following criterion: Status JSON is versioned and valid.

Acceptance Criteria

- Status JSON is versioned and valid.

### REQ-trust-008

The implementation SHALL satisfy the following criterion: CLI and status output report the plugin manifest version.

Acceptance Criteria

- CLI and status output report the plugin manifest version.

### REQ-trust-009

The implementation SHALL satisfy the following criterion: Atlas publication is explicit opt-in and never runs for pull request events.

Acceptance Criteria

- Atlas publication is explicit opt-in and never runs for pull request events.

### REQ-trust-010

The implementation SHALL satisfy the following criterion: Enabled Atlas policy is verified locally and published by the generated workflow on pushes.

Acceptance Criteria

- Enabled Atlas policy is verified locally and published by the generated workflow on pushes.

### REQ-trust-011

The implementation SHALL satisfy the following criterion: Tagged publication validates the Trust source contract with the pinned SpecSync release before exact-tag dogfooding.

Acceptance Criteria

- Tagged publication validates the Trust source contract with the pinned SpecSync release before exact-tag dogfooding.

### REQ-trust-012

The implementation SHALL satisfy the following criterion: Exact-tag dogfooding exposes suffixed release assets through canonical `augur` and `attest` command names.

Acceptance Criteria

- Exact-tag dogfooding exposes suffixed release assets through canonical `augur` and `attest` command names.

### REQ-trust-013

The implementation SHALL satisfy the following criterion: Exact-tag dogfooding verifies an installed release against an enforced, satisfied baseline ledger.

Acceptance Criteria

- Exact-tag dogfooding verifies an installed release against an enforced, satisfied baseline ledger.

### REQ-trust-014

The implementation SHALL satisfy the following criterion: Main provenance waits for the repository Trust gate in the same workflow and repairs insufficient existing notes.

Acceptance Criteria

- Main provenance waits for the repository Trust gate in the same workflow and repairs insufficient existing notes.

### REQ-trust-015

The implementation SHALL satisfy the following criterion: The Homebrew bundle exposes `fledge-trust` as a concrete executable for Fledge PATH discovery.

Acceptance Criteria

- The Homebrew bundle exposes `fledge-trust` as a concrete executable for Fledge PATH discovery.

### REQ-trust-016

The implementation SHALL satisfy the following criterion: Baseline provenance verifies the protected base commit while lifecycle, contract, and risk gate the proposed range.

Acceptance Criteria

- Baseline provenance verifies the protected base commit while lifecycle, contract, and risk gate the proposed range.

### REQ-trust-017

The implementation SHALL satisfy the following criterion: Baseline pull requests fail when their event base is not the live remote branch tip.

Acceptance Criteria

- Baseline pull requests fail when their event base is not the live remote branch tip.

### REQ-trust-018

The implementation SHALL satisfy the following criterion: Provenance scope changes are limited to a simultaneous soft-to-enforced baseline migration.

Acceptance Criteria

- Provenance scope changes are limited to a simultaneous soft-to-enforced baseline migration.

### REQ-trust-019

The implementation SHALL satisfy the following criterion: Pull requests cannot change the committed provenance policy contents.

Acceptance Criteria

- Pull requests cannot change the committed provenance policy contents.

### REQ-trust-020

The implementation SHALL satisfy the following criterion: Pull request policy comparison fails closed when the base commit is unavailable.

Acceptance Criteria

- Pull request policy comparison fails closed when the base commit is unavailable.

### REQ-trust-021

The implementation SHALL satisfy the following criterion: External governed worktrees ignore the host GitHub event and require an explicit range.

Acceptance Criteria

- External governed worktrees ignore the host GitHub event and require an explicit range.

### REQ-trust-022

The implementation SHALL satisfy the following criterion: GitHub event repository identity matches both server origin and owner/repository name.

Acceptance Criteria

- GitHub event repository identity matches both server origin and owner/repository name.

### REQ-trust-023

The implementation SHALL satisfy the following criterion: Native pull request comparisons are fixed to the event base and head commits.

Acceptance Criteria

- Native pull request comparisons are fixed to the event base and head commits.

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
