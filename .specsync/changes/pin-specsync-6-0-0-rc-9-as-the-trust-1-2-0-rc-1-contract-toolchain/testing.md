---
change: pin-specsync-6-0-0-rc-9-as-the-trust-1-2-0-rc-1-contract-toolchain
artifact: testing
---

# Testing

- `tests/test.sh` resolver cases accept default `6.0.0-rc.9` with no mirror
  and reject other exact versions without a mirror, including former default
  `5.2.0`. Mirror validation cases stay on `5.0.1` fixtures.
- `tests/test.sh` requires README to install `CorvidLabs/trust@v$plugin_version`
  and `fledge trust --version` to match `plugin.toml`.
- `scripts/validate.py` fails unless the nested SpecSync action SHA pairs with
  binary `6.0.0-rc.9` in both `action.yml` and `release.yml`.
- `fledge lanes run verify` (fmt, lint, test) and
  `specsync check --force --strict` pass on this tree.
- `python3 scripts/release_channel.py v1.2.0-rc.1` reports promote=false for
  channel `v1`.

Evidence for REQ-trust-action-010 is the resolver suite in `tests/test.sh` and
the pairing assertions in `scripts/validate.py`. Plugin version identity is
covered by the `fledge trust --version` assertion against `plugin.toml`.
