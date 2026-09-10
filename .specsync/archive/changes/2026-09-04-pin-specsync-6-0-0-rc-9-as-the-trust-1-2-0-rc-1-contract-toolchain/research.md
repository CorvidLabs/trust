---
change: pin-specsync-6-0-0-rc-9-as-the-trust-1-2-0-rc-1-contract-toolchain
artifact: research
---

# Research

- SpecSync `v6.0.0-rc.9` is published (2026-08-27) with linux and macOS
  archives plus SHA-256 sidecars. There is no `v6.0.0` GitHub release yet;
  the action's own default `version: "6.0.0"` would miss assets. Trust must
  default the binary version to `6.0.0-rc.9`.
- Annotated tag object `783a6d0ce2089c0f5c109dc795ac156518325727` peels to
  commit `62b297a4eb1822ec444460a172d6264317ebbf2e`. Trust 1.1.2 pinned
  SpecSync 5.2.0 the same way (tag object `ef3678c…`, peeled commit
  `342bd053…`). Keep that pairing style.
- SpecSync 6 `check` no longer fails on SDD lifecycle state. The nested
  SpecSync action's `lifecycle-enforce` input defaults to false; Trust must
  not turn it on.
- Observed consumer failures this change is meant to stop:
  - slug change IDs rejected by SpecSync 5.0.1 (`invalid change ID`)
  - `accepted change verification is stale for current delivery inputs`
  - git `dubious ownership` inside a Swift container reported as stale
    accepted changes
- Alternatives rejected: merging the July Trust 1.1.1 / SpecSync 5.1.1 pin
  PRs (still cannot parse 6.x IDs); defaulting Trust to `6.0.0` without an
  rc tag (no release assets); waiting for rc.10 / #737 (user chose pin now).
