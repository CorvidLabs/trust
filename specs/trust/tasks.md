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
- [x] Separate Trust's lifecycle lane from its composed SpecSync contract gate.
- [x] Add an end-to-end Action smoke matrix against fixture repositories.
- [x] Replace an older managed rules block without touching surrounding AGENTS.md content.
- [x] Add opt-in Atlas verification and push-only GitHub Pages publication.
- [x] Run the complete plugin behavior suite on Windows and resolve Git Bash command and path portability.
- [x] Add a release lane that composes code verification with the spec contract gate.
- [x] Dogfood immutable commit installation through Fledge in a disposable governed repository.
- [x] Gate tagged releases on exact-tag installation, real component verification, and monotonic channel selection.
- [x] Add bootstrap-safe recording and durable verification for landed main provenance.

## Next

- [ ] Tag and dogfood a pre-1.0 release through the supported plugin installation path.
- [ ] Add a Homebrew `corvid-trust` bundle after the first tagged release.
- [ ] Promote the spec from review to active after spec-sync can match dotted YAML Public API symbols.
- [ ] Upgrade the Action and release validation to spec-sync 5.0.0 before Trust 1.0.0.
- [ ] Enable and publish the Trust repository's provenance ledger before Trust 1.0.0.
- [ ] Add a maintainer-managed `v1` tag ruleset before promoting the stable Action channel.
- [ ] Cut Trust 1.0.0 and move the supported composite Action channel from `v0` to `v1`.
