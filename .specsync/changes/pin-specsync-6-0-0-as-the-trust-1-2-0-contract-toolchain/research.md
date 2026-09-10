---
change: pin-specsync-6-0-0-as-the-trust-1-2-0-contract-toolchain
artifact: research
---

# Research

- SpecSync `v6.0.0` is published (2026-09-09, stable, not prerelease) with
  linux x86_64 / x86_64-musl / aarch64 and macOS x86_64 / aarch64 archives
  plus SHA-256 sidecars. The rc.12 research note that Trust must keep an
  exact rc default no longer applies: the nested action can pin `6.0.0`.
- Annotated tag object `3c2ed4972c8c53ae02ab5dd5775beccd6da3eeb8` peels to
  commit `b9ff32310181b796cc617406ff9298c533ebeb15`. The rc.12 pin used tag
  object `29392630a590c13fcca65bec2a3c0a8f8c9e4081` (peeled `ac796b8e…`);
  keep that pairing style. Dependabot is ignored for this governed pin
  because it re-raises the peeled commit as an upgrade.
- The locally installed `specsync` binary reports `specsync 6.0.0`. crates.io
  also lists `specsync 6.0.0`.
- `fledge lanes run verify` is both the committed `.trust.toml` lifecycle
  command and the policy's verification command; the contract gate stays
  `specsync check` with `lifecycle-enforce` unset.
- `python3 scripts/release_channel.py` reports `promote: false` for
  `v1.2.0-rc.4` and `promote: true` for a later `v1.2.0` tag.
- Alternatives rejected: leaving Trust on rc.12 (consumers on 6.0.0 would
  audit under a different SpecSync than CI); retagging rc.4 (immutable);
  bumping `plugin.toml` to 1.2.0 in this pin (RELEASING.md cuts the stable
  tag with `fledge release 1.2.0` from clean main after hosted checks).
