---
id: pin-specsync-6-0-0-rc-12-as-the-trust-1-2-0-rc-4-contract-toolchain
state: implementing
type: migration
base_commit: 1ebcee1e8ae89a39b00b7039e3383311409407e6
---

# Pin SpecSync 6.0.0-rc.12 as the Trust 1.2.0-rc.4 contract toolchain

## Intent

Pin SpecSync 6.0.0-rc.12 as the Trust 1.2.0-rc.4 contract toolchain

## Affected Canonical Specs

- `trust-action`
- `trust-policy`
- `trust-plugin`
- `trust`

## Acceptance Criteria

- Trust 1.2.0-rc.4 pins SpecSync 6.0.0-rc.12 as the composite-action default and nested immutable action tag object 29392630a590c13fcca65bec2a3c0a8f8c9e4081 (peeled commit ac796b8eadd3092283093bbea331ec2d3494b527). action.yml, trust_cli.py, validate.py, release.yml, tests/test.sh, plugin.toml, README, and RELEASING agree on that pin. plugin.toml version is 1.2.0-rc.4 and README installs CorvidLabs/trust@v1.2.0-rc.4. fledge lanes run verify and specsync check --force --strict pass under SpecSync 6.0.0-rc.12. The contract gate still does not enable SpecSync lifecycle-enforce. A 1.2.0-rc.4 tag is a prerelease and cannot move the protected v1 channel.

## No-spec Rationale

Not applicable
