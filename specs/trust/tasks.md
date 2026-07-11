---
spec: trust.spec.md
---

## Completed

- [x] Scaffold the public Trust repository.
- [x] Add the Fledge plugin command surface.
- [x] Add conservative, idempotent adoption templates.
- [x] Add the composite GitHub Action.
- [x] Add local behavior and manifest validation.
- [x] Govern the orchestration contract with strict spec-sync validation.
- [x] Adopt Trust into its own repository and run the local gate against itself.
- [x] Make forced spec checks leave the tracked cache deterministic.

## Next

- [ ] Add a Homebrew `corvid-trust` bundle after the first tagged release.
- [ ] Add an end-to-end action smoke test against a fixture repository.
- [ ] Add optional Atlas publication to the composite workflow.
- [ ] Add managed-block updates that replace an older block without touching surrounding AGENTS.md content.
- [ ] Add Windows plugin behavior coverage.
- [ ] Promote the spec from review to active after spec-sync can match dotted YAML Public API symbols.
- [ ] Upgrade the Action and release validation to spec-sync 5.0.0 before Trust 1.0.0.
- [ ] Enable and publish the Trust repository's provenance ledger before Trust 1.0.0.
