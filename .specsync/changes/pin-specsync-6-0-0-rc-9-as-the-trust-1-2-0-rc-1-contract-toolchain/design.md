---
change: pin-specsync-6-0-0-rc-9-as-the-trust-1-2-0-rc-1-contract-toolchain
artifact: design
---

# Design

Coordinated pin flip. No new gates, no new inputs, no change to mirror
validation.

- Nested SpecSync action moves to immutable tag object
  `783a6d0ce2089c0f5c109dc795ac156518325727` (`v6.0.0-rc.9`).
- `inputs.specsync-version` default, `DEFAULT_SPECSYNC_VERSION`, release
  workflow binary version, and validator pairing all become `6.0.0-rc.9`.
- Non-default versions still require a validated local mirror. `5.2.0`
  becomes non-default and therefore needs a mirror.
- The composed SpecSync step does not set `lifecycle-enforce`; SpecSync 6
  `check` is the contract gate.
- `plugin.toml` version becomes `1.2.0-rc.1`. README install tag tracks that
  manifest. `release_channel.py` already refuses to promote a prerelease
  onto `v1`.
- Fledge, Augur, and Attest pins stay at 1.7.0 / 1.0.0 / 1.0.0.
