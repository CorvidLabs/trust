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

The implementation SHALL satisfy this requirement.

Acceptance Criteria

- `adopt --dry-run` reports changes and writes nothing.
### REQ-trust-002

The implementation SHALL satisfy this requirement.

Acceptance Criteria

- Repeated adoption is idempotent.
### REQ-trust-003

The implementation SHALL satisfy this requirement.

Acceptance Criteria

- Existing files are preserved unless `--force` is passed.
### REQ-trust-004

The implementation SHALL satisfy this requirement.

Acceptance Criteria

- The managed AGENTS block is present exactly once.
### REQ-trust-005

The implementation SHALL satisfy this requirement.

Acceptance Criteria

- Verification runs lifecycle, contract, risk, and provenance in order.
### REQ-trust-006

The implementation SHALL satisfy this requirement.

Acceptance Criteria

- The composite action exposes Augur verdict and risk outputs.
### REQ-trust-007

The implementation SHALL satisfy this requirement.

Acceptance Criteria

- Status JSON is versioned and valid.
### REQ-trust-008

The implementation SHALL satisfy this requirement.

Acceptance Criteria

- CLI and status output report the plugin manifest version.
### REQ-trust-009

The implementation SHALL satisfy this requirement.

Acceptance Criteria

- Atlas publication is explicit opt-in and never runs for pull request events.
### REQ-trust-010

The implementation SHALL satisfy this requirement.

Acceptance Criteria

- Enabled Atlas policy is verified locally and published by the generated workflow on pushes.
### REQ-trust-011

The implementation SHALL satisfy this requirement.

Acceptance Criteria

- Tagged publication validates the Trust source contract with the pinned SpecSync release before exact-tag dogfooding.
### REQ-trust-012

The implementation SHALL satisfy this requirement.

Acceptance Criteria

- Exact-tag dogfooding exposes suffixed release assets through canonical `augur` and `attest` command names.
### REQ-trust-013

The implementation SHALL satisfy this requirement.

Acceptance Criteria

- Exact-tag dogfooding verifies an installed release against an enforced, satisfied baseline ledger.
### REQ-trust-014

The implementation SHALL satisfy this requirement.

Acceptance Criteria

- Main provenance waits for the repository Trust gate in the same workflow and repairs insufficient existing notes.
### REQ-trust-015

The implementation SHALL satisfy this requirement.

Acceptance Criteria

- The Homebrew bundle exposes `fledge-trust` as a concrete executable for Fledge PATH discovery.
### REQ-trust-016

The implementation SHALL satisfy this requirement.

Acceptance Criteria

- Baseline provenance verifies the protected base commit while lifecycle, contract, and risk gate the proposed range.
### REQ-trust-017

The implementation SHALL satisfy this requirement.

Acceptance Criteria

- Baseline pull requests fail when their event base is not the live remote branch tip.
### REQ-trust-018

The implementation SHALL satisfy this requirement.

Acceptance Criteria

- Provenance scope changes are limited to a simultaneous soft-to-enforced baseline migration.
### REQ-trust-019

The implementation SHALL satisfy this requirement.

Acceptance Criteria

- Pull requests cannot change the committed provenance policy contents.
### REQ-trust-020

The implementation SHALL satisfy this requirement.

Acceptance Criteria

- Pull request policy comparison fails closed when the base commit is unavailable.
### REQ-trust-021

The implementation SHALL satisfy this requirement.

Acceptance Criteria

- External governed worktrees ignore the host GitHub event and require an explicit range.
### REQ-trust-022

The implementation SHALL satisfy this requirement.

Acceptance Criteria

- GitHub event repository identity matches both server origin and owner/repository name.
### REQ-trust-023

The implementation SHALL satisfy this requirement.

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
