---
change: pin-specsync-6-0-0-as-the-trust-1-2-0-contract-toolchain
artifact: docs
---

# Docs

- `README.md`: plugin install tag stays `v1.2.0-rc.4`. The self-hosting
  paragraph names SpecSync `6.0.0` as the default consumers get when they
  omit `specsync-version`.
- `RELEASING.md`: current pin pairing is SpecSync action tag object
  `3c2ed4972c8c53ae02ab5dd5775beccd6da3eeb8` with binary `6.0.0`.
  `v1.2.0-rc.4` remains a prerelease and cannot move `v1`; the later
  `v1.2.0` tag is eligible.
- `.github/dependabot.yml`: ignore comment names the v6.0.0 tag object.
- Historical 0.2.1 / 1.0.0 rehearsal examples in `RELEASING.md` stay as
  audit history.
- Companion history in `specs/trust/context.md` and `specs/trust/tasks.md`
  that narrates the 5.0.1 era stays unchanged.
