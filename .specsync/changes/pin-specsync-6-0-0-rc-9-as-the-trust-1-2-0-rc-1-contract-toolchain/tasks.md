---
change: pin-specsync-6-0-0-rc-9-as-the-trust-1-2-0-rc-1-contract-toolchain
artifact: tasks
---

# Tasks

- [x] Pin SpecSync 6.0.0-rc.9 in `action.yml` (default, description, nested commit).
- [x] Update `DEFAULT_SPECSYNC_VERSION` and `validate.py` pairing.
- [x] Pin 6.0.0-rc.9 in `.github/workflows/release.yml` jobs.
- [x] Update resolver tests for the new default; keep mirror rules.
- [x] Set `plugin.toml` to 1.2.0-rc.1 and match README install tag.
- [x] Document the pin in `README.md` and `RELEASING.md`.
- [x] Apply semantic deltas to trust-action, trust-policy, trust-plugin, and trust.
- [x] Run `fledge lanes run verify` and strict SpecSync check.
