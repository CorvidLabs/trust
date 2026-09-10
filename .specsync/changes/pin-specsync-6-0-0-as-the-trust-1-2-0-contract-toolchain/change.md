---
id: pin-specsync-6-0-0-as-the-trust-1-2-0-contract-toolchain
state: implementing
type: migration
base_commit: e39c7e4862af35eb10e40058eb46e894efef249e
---

# Pin SpecSync 6.0.0 as the Trust 1.2.0 contract toolchain

## Intent

Pin SpecSync 6.0.0 as the Trust 1.2.0 contract toolchain

## Affected Canonical Specs

- `trust-action`
- `trust-policy`
- `trust-plugin`
- `trust`

## Acceptance Criteria

- Trust pins SpecSync 6.0.0 as the composite-action default and nested immutable action tag object 3c2ed4972c8c53ae02ab5dd5775beccd6da3eeb8 (peeled commit b9ff32310181b796cc617406ff9298c533ebeb15). action.yml, trust_cli.py, validate.py, release.yml, tests/test.sh, README, RELEASING, and dependabot.yml agree on that pin. plugin.toml remains 1.2.0-rc.4 so fledge release 1.2.0 can bump and tag from clean main after merge. fledge lanes run verify and specsync check --force --strict pass under SpecSync 6.0.0. The contract gate still does not enable SpecSync lifecycle-enforce. A later 1.2.0 tag is eligible to promote the protected v1 channel.

## No-spec Rationale

Not applicable
