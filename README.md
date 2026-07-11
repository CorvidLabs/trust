# CorvidLabs Trust

One adoption path for the CorvidLabs trust toolchain.

Trust keeps the underlying tools independent and composes them into one gate:

1. **fledge** runs the repository's verification lifecycle.
2. **spec-sync** checks the code against its contract.
3. **augur** blocks changes whose deterministic risk reaches the configured threshold.
4. **attest** verifies signed provenance recorded in git notes.
5. **atlas** optionally publishes the result as a living coverage map.

## Install

The first release will be available as a Homebrew bundle. Until then, install
the four tools and this plugin directly:

```bash
brew tap CorvidLabs/tap
brew install fledge spec-sync augur attest
fledge plugins install CorvidLabs/trust
```

## Adopt the gate

Run this inside an existing git repository:

```bash
fledge trust adopt --dry-run
fledge trust adopt
# Review fledge.toml and ensure it contains a real [lanes.verify] lane.
fledge trust doctor
fledge trust verify
```

`adopt` is conservative and idempotent. It creates missing configuration,
workflow, policy, and standing-rules files but does not overwrite existing
project files unless `--force` is explicitly passed.
When fledge cannot infer a complete verification lane, adoption leaves a clear
note and `doctor` stays red until the repository defines the real commands.

Optional layers can be skipped with a recorded reason:

```bash
fledge trust adopt --no-specs "content-only repository" --no-atlas "Pages is disabled"
```

## GitHub Actions

The composite action runs the same gate in CI. Checkout must use full history
because augur and attest inspect commit ranges and git notes.

```yaml
steps:
  - uses: actions/checkout@v5
    with:
      fetch-depth: 0

  - uses: CorvidLabs/trust@v1
    with:
      profile: standard
      range: origin/main..HEAD
```

The individual actions remain available when a repository needs custom step
ordering or versions.

## Commands

| Command | Purpose |
| --- | --- |
| `fledge trust adopt` | Add the managed workflow, policies, and agent rules to a repository. |
| `fledge trust verify` | Run lifecycle, contract, risk, and provenance gates in order. |
| `fledge trust status` | Report installed tools and wired repository layers. |
| `fledge trust doctor` | Fail when required tools or configuration are missing. |

## Design boundary

This repository owns orchestration only. Parsing specs, scoring diffs, storing
attestations, and rendering Atlas remain in their respective repositories and
release independently.

## License

MIT
