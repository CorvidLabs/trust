---
change: pin-specsync-6-0-0-as-the-trust-1-2-0-contract-toolchain
artifact: design
---

# Design

Coordinated pin flip. No new gates, no new inputs, no change to mirror
validation or to the GitHub-released-version path.

- Nested SpecSync action moves to immutable tag object
  `3c2ed4972c8c53ae02ab5dd5775beccd6da3eeb8` (`v6.0.0`).
- `inputs.specsync-version` default, `DEFAULT_SPECSYNC_VERSION`, release
  workflow binary version, resolver test default, and validator pairing all
  become `6.0.0`.
- The composed SpecSync step still does not set `lifecycle-enforce`;
  SpecSync 6 `check` remains the contract gate.
- `plugin.toml` stays `1.2.0-rc.4`. README install tag stays
  `CorvidLabs/trust@v1.2.0-rc.4` until `fledge release 1.2.0`.
- Fledge, Augur, and Attest pins stay at 1.7.0 / 1.0.0 / 1.0.0.
- Dependabot ignore comments name the new tag object so the governed-pin
  rationale stays accurate.
