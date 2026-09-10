---
change: pin-specsync-6-0-0-rc-11-as-the-trust-1-2-0-rc-3-contract-toolchain
artifact: design
---

# Design

Coordinated pin flip. No new gates, no new inputs, no change to mirror
validation or to the GitHub-released-version path added for rc.2.

- Nested SpecSync action moves to immutable tag object
  `2371bf3122919a6548eb790d258e036c0220776b` (`v6.0.0-rc.11`).
- `inputs.specsync-version` default, `DEFAULT_SPECSYNC_VERSION`, release
  workflow binary version, resolver test default, and validator pairing all
  become `6.0.0-rc.11`.
- The composed SpecSync step still does not set `lifecycle-enforce`;
  SpecSync 6 `check` remains the contract gate.
- `plugin.toml` version becomes `1.2.0-rc.3`. README install tag tracks
  that manifest. `release_channel.py` already refuses to promote a
  prerelease onto `v1`.
- Fledge, Augur, and Attest pins stay at 1.7.0 / 1.0.0 / 1.0.0.
