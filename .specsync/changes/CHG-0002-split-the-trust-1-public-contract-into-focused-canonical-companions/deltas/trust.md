## MODIFIED

### REQUIREMENT REQ-trust-001

Tagged publication SHALL validate the Trust source contract with the pinned SpecSync release before exact-tag dogfooding.

Acceptance Criteria

- Release validation completes before installation tests use the new tag.

### REQUIREMENT REQ-trust-002

Exact-tag dogfooding SHALL expose suffixed release assets through canonical `augur` and `attest` command names.

Acceptance Criteria

- A tagged installation resolves and executes both component binaries.

### REQUIREMENT REQ-trust-003

Exact-tag dogfooding SHALL verify an installed release against an enforced, satisfied baseline ledger.

Acceptance Criteria

- The installed bundle passes its own Trust verification using tagged artifacts.

### REQUIREMENT REQ-trust-004

The Homebrew bundle SHALL expose `fledge-trust` as a concrete executable for Fledge PATH discovery.

Acceptance Criteria

- A fresh bundle installation exposes `fledge trust` without repository-local shims.

## REMOVED

### REQUIREMENT REQ-trust-005

The implementation SHALL satisfy this requirement.

Acceptance Criteria

- Verification runs lifecycle, contract, risk, and provenance in order.

### REQUIREMENT REQ-trust-006

The implementation SHALL satisfy this requirement.

Acceptance Criteria

- The composite action exposes Augur verdict and risk outputs.

### REQUIREMENT REQ-trust-007

The implementation SHALL satisfy this requirement.

Acceptance Criteria

- Status JSON is versioned and valid.

### REQUIREMENT REQ-trust-008

The implementation SHALL satisfy this requirement.

Acceptance Criteria

- CLI and status output report the plugin manifest version.

### REQUIREMENT REQ-trust-009

The implementation SHALL satisfy this requirement.

Acceptance Criteria

- Atlas publication is explicit opt-in and never runs for pull request events.

### REQUIREMENT REQ-trust-010

The implementation SHALL satisfy this requirement.

Acceptance Criteria

- Enabled Atlas policy is verified locally and published by the generated workflow on pushes.

### REQUIREMENT REQ-trust-011

The implementation SHALL satisfy this requirement.

Acceptance Criteria

- Tagged publication validates the Trust source contract with the pinned SpecSync release before exact-tag dogfooding.

### REQUIREMENT REQ-trust-012

The implementation SHALL satisfy this requirement.

Acceptance Criteria

- Exact-tag dogfooding exposes suffixed release assets through canonical `augur` and `attest` command names.

### REQUIREMENT REQ-trust-013

The implementation SHALL satisfy this requirement.

Acceptance Criteria

- Exact-tag dogfooding verifies an installed release against an enforced, satisfied baseline ledger.

### REQUIREMENT REQ-trust-014

The implementation SHALL satisfy this requirement.

Acceptance Criteria

- Main provenance waits for the repository Trust gate in the same workflow and repairs insufficient existing notes.

### REQUIREMENT REQ-trust-015

The implementation SHALL satisfy this requirement.

Acceptance Criteria

- The Homebrew bundle exposes `fledge-trust` as a concrete executable for Fledge PATH discovery.

### REQUIREMENT REQ-trust-016

The implementation SHALL satisfy this requirement.

Acceptance Criteria

- Baseline provenance verifies the protected base commit while lifecycle, contract, and risk gate the proposed range.

### REQUIREMENT REQ-trust-017

The implementation SHALL satisfy this requirement.

Acceptance Criteria

- Baseline pull requests fail when their event base is not the live remote branch tip.

### REQUIREMENT REQ-trust-018

The implementation SHALL satisfy this requirement.

Acceptance Criteria

- Provenance scope changes are limited to a simultaneous soft-to-enforced baseline migration.

### REQUIREMENT REQ-trust-019

The implementation SHALL satisfy this requirement.

Acceptance Criteria

- Pull requests cannot change the committed provenance policy contents.

### REQUIREMENT REQ-trust-020

The implementation SHALL satisfy this requirement.

Acceptance Criteria

- Pull request policy comparison fails closed when the base commit is unavailable.

### REQUIREMENT REQ-trust-021

The implementation SHALL satisfy this requirement.

Acceptance Criteria

- External governed worktrees ignore the host GitHub event and require an explicit range.

### REQUIREMENT REQ-trust-022

The implementation SHALL satisfy this requirement.

Acceptance Criteria

- GitHub event repository identity matches both server origin and owner/repository name.

### REQUIREMENT REQ-trust-023

The implementation SHALL satisfy this requirement.

Acceptance Criteria

- Native pull request comparisons are fixed to the event base and head commits.
