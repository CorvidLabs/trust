# Changelog

## [v0.2.1] - 2026-07-11

### Other

- Fix: expose tagged component commands (#7) (82b38d0)

## [v0.2.0] - 2026-07-11

### Build

- bump actions/checkout from 5 to 7 (#2) (92675c7)

### Features

- scaffold unified trust orchestration (25c0ae4)

### Other

- Update: record provenance bootstrap (#6) (b13c576)
- Prepare Trust for 1.0 dogfooding (#4) (c1448c7)
- Add: stabilize Trust v0.1 policy and Action (#1) (46f61e0)

## [Unreleased]

### Fixed

- Expose suffixed Augur and Attest release assets under the canonical commands required by exact-tag dogfooding.

### Added

- Add CLI and status version reporting so installed plugin builds can be identified.
- Dogfood Trust through a repository-local workflow and committed managed configuration.
- Add merge-safe baseline provenance verification while retaining changed-commit scope as the compatibility default.
- Publish and dogfood the Homebrew Trust bundle and protected `v0` Action channel at v0.2.1.
- Require exact-tag releases to pass installed-plugin verification against a satisfied enforced baseline ledger.

### Changed

- Upgrade the composed SpecSync action and binary to 5.0.1 and activate the governed Trust contract with exact coverage.
- Require tagged source contract validation, a concrete Homebrew plugin wrapper, and an in-workflow Trust gate before provenance publication.
- Repair insufficient existing provenance notes before verifying and publishing the durable ledger.
- Align the governed Public API table for exact active coverage with the SpecSync 5.0.1 parser fix.
- Enforce the bootstrapped and independently verified main provenance ledger through protected baseline verification.
- Prevent pull requests from changing committed Attest policy contents or switching provenance scope outside migration.
- Normalize the SpecSync cache after forced verification and pin generated checkout steps to v7.0.0.
- Pin the validation dependency in both CI and the repository self-dogfood workflow.
- Keep SpecSync out of the lifecycle lane so the composite Action owns contract installation and verification order.
- Correct the contract and installation documentation to match the pre-release Action and plugin surfaces.
- Make Atlas explicit opt-in, verify its local report, and add push-only Pages publication to generated workflows.
- Exercise the complete plugin validation and behavior suite on Windows.

## [0.1.0] - 2026-07-10

### Added

- Add the `fledge trust` orchestration plugin with adopt, verify, status, and doctor commands.
- Add the `CorvidLabs/trust` composite action for one CI trust gate.
- Add managed templates for repository policy, agent instructions, and GitHub Actions.
- Add `.trust.toml` as the shared local and CI policy with standard and strict profiles.
- Add macOS/Linux Action smoke coverage, immutable dependency pins, event-aware ranges, and versioned gate outputs.
