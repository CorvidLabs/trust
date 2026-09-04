---
id: pin-specsync-6-0-0-rc-11-as-the-trust-1-2-0-rc-3-contract-toolchain
state: archived
type: migration
base_commit: fcebc62303f89ad6573113313d75d0d26d7d2477
---

# Pin SpecSync 6.0.0-rc.11 as the Trust 1.2.0-rc.3 contract toolchain

## Intent

Pin SpecSync 6.0.0-rc.11 as the Trust 1.2.0-rc.3 contract toolchain

## Affected Canonical Specs

- `trust-action`
- `trust-policy`
- `trust-plugin`
- `trust`

## Acceptance Criteria

- Trust 1.2.0-rc.3 pins SpecSync 6.0.0-rc.11 as the composite-action default and nested immutable action tag object 2371bf3122919a6548eb790d258e036c0220776b (peeled commit 6a5a7a7d893fb43515c51514989e5b06674656c4). action.yml, trust_cli.py, validate.py, release.yml, tests/test.sh, plugin.toml, README, and RELEASING agree on that pin. plugin.toml version is 1.2.0-rc.3 and README installs CorvidLabs/trust@v1.2.0-rc.3. fledge lanes run verify and specsync check --force --strict pass under SpecSync 6.0.0-rc.11. The contract gate still does not enable SpecSync lifecycle-enforce. A 1.2.0-rc.3 tag is a prerelease and cannot move the protected v1 channel.

## No-spec Rationale

Not applicable
