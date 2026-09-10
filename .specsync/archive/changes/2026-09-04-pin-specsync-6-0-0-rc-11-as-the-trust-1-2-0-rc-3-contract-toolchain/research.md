---
change: pin-specsync-6-0-0-rc-11-as-the-trust-1-2-0-rc-3-contract-toolchain
artifact: research
---

# Research

- SpecSync `v6.0.0-rc.11` is published (2026-08-29T22:45Z, prerelease) with
  linux x86_64 / x86_64-musl / aarch64 and macOS x86_64 / aarch64 archives plus
  SHA-256 sidecars. There is still no `v6.0.0` GitHub release, so the nested
  action's own `version: "6.0.0"` default would miss assets; Trust must keep
  an exact rc default.
- Annotated tag object `2371bf3122919a6548eb790d258e036c0220776b` peels to commit
  `6a5a7a7d893fb43515c51514989e5b06674656c4`. The rc.9 pin used tag object
  `783a6d0ce2089c0f5c109dc795ac156518325727` (peeled `62b297a4…`) and
  5.2.0 used tag object `ef3678c…`; keep that pairing style. Release runs
  for `v1.2.0-rc.1` and `v1.2.0-rc.2` prove the tag-object pin resolves
  in the nested `uses:`.
- The macOS aarch64 rc.11 archive verified against its published SHA-256
  sidecar locally (`0b28961c…`) and reports `specsync 6.0.0`; the binary
  self-reports the base version, the tag carries the rc identifier.
- `fledge lanes run verify` is both the committed `.trust.toml` lifecycle
  command and the policy's verification command; the contract gate stays
  `specsync check` with `lifecycle-enforce` unset.
- Alternatives rejected: leaving Trust on rc.9 (consumers on rc.11 would audit
  under a different SpecSync than CI); re-cutting rc.2 (immutable tag);
  waiting for 6.0.0 GA (no date).
