---
change: pin-specsync-6-0-0-rc-11-as-the-trust-1-2-0-rc-3-contract-toolchain
artifact: plan
---

# Plan

1. Record definition artifacts and semantic deltas for the 6.0.0-rc.11 default.
2. Flip every SpecSync pin: `action.yml`, `scripts/trust_cli.py`,
   `scripts/validate.py`, `.github/workflows/release.yml`, `tests/test.sh`,
   `README.md`, `RELEASING.md`, and the affected canonical specs.
3. Set `plugin.toml` to `1.2.0-rc.3` and point README install at
   `CorvidLabs/trust@v1.2.0-rc.3`.
4. Run `fledge lanes run verify` and `specsync check --force --strict`
   with SpecSync 6.0.0-rc.11 on PATH.
5. After merge of this change, tag `v1.2.0-rc.3` from main. Do not move `v1`.
