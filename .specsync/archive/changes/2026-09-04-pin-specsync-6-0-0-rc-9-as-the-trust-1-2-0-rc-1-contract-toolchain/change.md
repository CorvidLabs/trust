---
id: pin-specsync-6-0-0-rc-9-as-the-trust-1-2-0-rc-1-contract-toolchain
state: archived
type: migration
base_commit: 887c7d74828cc0c7e2f620bdd0325ac8ca9250d1
---

# Pin SpecSync 6.0.0-rc.9 as the Trust 1.2.0-rc.1 contract toolchain

## Intent

Pin SpecSync 6.0.0-rc.9 as the Trust 1.2.0-rc.1 contract toolchain

## Affected Canonical Specs

- `trust-action`
- `trust-policy`
- `trust-plugin`
- `trust`

## Acceptance Criteria

- Trust 1.2.0-rc.1 pins SpecSync 6.0.0-rc.9 as the composite-action default and nested immutable action commit 783a6d0ce2089c0f5c109dc795ac156518325727. action.yml, trust_cli.py, validate.py, release.yml, plugin.toml, README, and RELEASING agree on that pin. plugin.toml version is 1.2.0-rc.1. fledge lanes run verify and specsync check --force --strict pass. The contract gate does not enable SpecSync lifecycle-enforce, so specsync check no longer fails CI on SDD bookkeeping. A 1.2.0-rc.1 tag is a prerelease and cannot move the protected v1 channel.

## No-spec Rationale

Not applicable
