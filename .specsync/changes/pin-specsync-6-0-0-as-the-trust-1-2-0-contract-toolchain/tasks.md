---
change: pin-specsync-6-0-0-as-the-trust-1-2-0-contract-toolchain
artifact: tasks
---

# Tasks

- [x] Pin SpecSync 6.0.0 in `action.yml` (default, description, nested tag object).
- [x] Update `DEFAULT_SPECSYNC_VERSION` and `validate.py` pairing.
- [x] Pin 6.0.0 in `.github/workflows/release.yml` jobs.
- [x] Update the resolver default in `tests/test.sh`; keep mirror rules.
- [x] Document the pin in `README.md` and `RELEASING.md`.
- [x] Update the Dependabot ignore comment to the v6.0.0 tag object.
- [x] Apply semantic deltas to trust-action, trust-policy, trust-plugin, and trust.
- [x] Run `fledge lanes run verify` and strict SpecSync check under 6.0.0.
- [x] Leave `plugin.toml` at 1.2.0-rc.4 for the post-merge `fledge release 1.2.0`.
