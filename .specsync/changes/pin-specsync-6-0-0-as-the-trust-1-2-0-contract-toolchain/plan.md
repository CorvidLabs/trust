---
change: pin-specsync-6-0-0-as-the-trust-1-2-0-contract-toolchain
artifact: plan
---

# Plan

1. Record definition artifacts and semantic deltas for the 6.0.0 default.
2. Flip every SpecSync pin: `action.yml`, `scripts/trust_cli.py`,
   `scripts/validate.py`, `.github/workflows/release.yml`, `tests/test.sh`,
   `README.md`, `RELEASING.md`, `.github/dependabot.yml`, and the affected
   canonical specs.
3. Leave `plugin.toml` at `1.2.0-rc.4` and README install at
   `CorvidLabs/trust@v1.2.0-rc.4`.
4. Run `fledge lanes run verify` and `specsync check --force --strict`
   with SpecSync 6.0.0 on PATH.
5. After merge of this change and hosted checks, cut `v1.2.0` from main
   with `fledge release 1.2.0 --pre-lane release --push --non-interactive`.
   An administrator then promotes the protected `v1` channel.
