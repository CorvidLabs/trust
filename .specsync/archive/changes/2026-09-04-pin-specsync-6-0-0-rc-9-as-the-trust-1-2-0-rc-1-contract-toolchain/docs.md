---
change: pin-specsync-6-0-0-rc-9-as-the-trust-1-2-0-rc-1-contract-toolchain
artifact: docs
---

# Docs

- `README.md`: plugin install tag is `v1.2.0-rc.1`. The self-hosting paragraph
  names SpecSync `6.0.0-rc.9` as the default consumers get when they omit
  `specsync-version`.
- `RELEASING.md`: current pin pairing is SpecSync action commit
  `783a6d0ce2089c0f5c109dc795ac156518325727` with binary `6.0.0-rc.9`.
  `v1.2.0-rc.1` is a prerelease and cannot move `v1`.
- Historical 0.2.1 / 1.0.0 rehearsal examples in `RELEASING.md` stay as
  audit history.
- Companion history in `specs/trust/context.md` and `specs/trust/tasks.md`
  that narrates the 5.0.1 era stays unchanged except the current-gate line
  that names the live pin.
