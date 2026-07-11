# Changelog

## [Unreleased]

### Added

- Add CLI and status version reporting so installed plugin builds can be identified.
- Dogfood Trust through a repository-local workflow and committed managed configuration.

### Changed

- Update the composed SpecSync action and binary to 4.8.0 while preparing the 5.0.0 release gate.
- Normalize the SpecSync cache after forced verification and pin generated checkout steps to v7.0.0.
- Pin the validation dependency in both CI and the repository self-dogfood workflow.

## [0.1.0] - 2026-07-10

### Added

- Add the `fledge trust` orchestration plugin with adopt, verify, status, and doctor commands.
- Add the `CorvidLabs/trust` composite action for one CI trust gate.
- Add managed templates for repository policy, agent instructions, and GitHub Actions.
- Add `.trust.toml` as the shared local and CI policy with standard and strict profiles.
- Add macOS/Linux Action smoke coverage, immutable dependency pins, event-aware ranges, and versioned gate outputs.
