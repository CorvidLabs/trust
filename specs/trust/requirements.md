---
spec: trust.spec.md
---

# Requirements — Trust Distribution

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
