---
change: pin-specsync-6-0-0-rc-12-as-the-trust-1-2-0-rc-4-contract-toolchain
artifact: tasks
---

# Tasks

- [x] Pin SpecSync 6.0.0-rc.12 in `action.yml` (default, description, nested tag object).
- [x] Update `DEFAULT_SPECSYNC_VERSION` and `validate.py` pairing.
- [x] Pin 6.0.0-rc.12 in `.github/workflows/release.yml` jobs.
- [x] Update the resolver default in `tests/test.sh`; keep mirror rules.
- [x] Set `plugin.toml` to 1.2.0-rc.4 and match README install tag.
- [x] Document the pin in `README.md` and `RELEASING.md`.
- [x] Apply semantic deltas to trust-action, trust-policy, trust-plugin, and trust.
- [x] Run `fledge lanes run verify` and strict SpecSync check under rc.12.
