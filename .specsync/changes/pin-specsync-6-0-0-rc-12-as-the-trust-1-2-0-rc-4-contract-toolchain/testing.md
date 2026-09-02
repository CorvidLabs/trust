---
change: pin-specsync-6-0-0-rc-12-as-the-trust-1-2-0-rc-4-contract-toolchain
artifact: testing
---

# Testing

- `tests/test.sh` resolver cases accept default `6.0.0-rc.12` with no
  mirror; other exact GitHub-released versions still resolve without a mirror
  (the rc.2 behavior) and mirror validation cases stay on `5.0.1` fixtures.
- `tests/test.sh` requires README to install `CorvidLabs/trust@v$plugin_version`
  and `fledge trust --version` to match `plugin.toml`.
- `scripts/validate.py` fails unless the nested SpecSync action SHA pairs with
  binary `6.0.0-rc.12` in both `action.yml` and `release.yml`.
- `fledge lanes run verify` (fmt, lint, test) and
  `specsync check --force --strict` pass on this tree with the verified
  rc.12 binary first on PATH.
- `python3 scripts/release_channel.py v1.2.0-rc.4` reports promote=false for
  channel `v1`.

Evidence for REQ-trust-action-010 is the resolver suite in `tests/test.sh` and
the pairing assertions in `scripts/validate.py`. Plugin version identity is
covered by the `fledge trust --version` assertion against `plugin.toml`.
