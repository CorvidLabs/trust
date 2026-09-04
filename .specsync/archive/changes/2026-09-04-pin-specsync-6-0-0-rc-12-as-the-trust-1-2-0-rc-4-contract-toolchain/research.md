---
change: pin-specsync-6-0-0-rc-12-as-the-trust-1-2-0-rc-4-contract-toolchain
artifact: research
---

# Research

- SpecSync `v6.0.0-rc.12` is published (2026-09-02, prerelease) with
  linux x86_64 / x86_64-musl / aarch64 and macOS x86_64 / aarch64 archives plus
  SHA-256 sidecars. Qualify jobs for ubuntu and macos were green. There is
  still no `v6.0.0` GitHub release, so the nested action's own
  `version: "6.0.0"` default would miss assets; Trust must keep an exact rc
  default.
- Annotated tag object `29392630a590c13fcca65bec2a3c0a8f8c9e4081` peels to
  commit `ac796b8eadd3092283093bbea331ec2d3494b527`. The rc.11 pin used tag
  object `2371bf3122919a6548eb790d258e036c0220776b` (peeled `6a5a7a7d…`);
  keep that pairing style. Release runs for `v1.2.0-rc.3` prove the
  tag-object pin resolves in the nested `uses:`.
- The linux x86_64 rc.12 archive verified against its published SHA-256
  sidecar locally and reports `specsync 6.0.0`; the binary self-reports the
  base version, the tag carries the rc identifier.
- `fledge lanes run verify` is both the committed `.trust.toml` lifecycle
  command and the policy's verification command; the contract gate stays
  `specsync check` with `lifecycle-enforce` unset.
- Alternatives rejected: leaving Trust on rc.11 (consumers on rc.12 would
  audit under a different SpecSync than CI); re-cutting rc.3 (immutable
  tag); merging Trust#33 (same rc.11, peeled commit instead of tag object);
  waiting for 6.0.0 GA (no date).
