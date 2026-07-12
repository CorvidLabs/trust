# CorvidLabs Trust

One adoption path for the CorvidLabs trust toolchain.

Trust keeps the underlying tools independent and composes them into one gate:

1. **fledge** runs the repository's verification lifecycle.
2. **spec-sync** checks the code against its contract.
3. **augur** blocks changes whose deterministic risk reaches the configured threshold.
4. **attest** verifies signed provenance recorded in git notes.
5. **atlas** optionally publishes the result as a living coverage map.

## Install the pre-release plugin

Until the first tagged Trust release and Homebrew bundle are published, install
the plugin from the repository:

```bash
fledge plugins install CorvidLabs/trust
```

Trust verification also requires the independently distributed `specsync`,
`augur`, and `attest` commands locally. The composite GitHub Action installs its
own pinned tool versions.

## Adopt the gate

Run this inside an existing git repository:

```bash
fledge trust adopt --dry-run
fledge trust adopt
# Review fledge.toml and ensure it contains a real [lanes.verify] lane.
fledge trust doctor
fledge trust verify
```

`adopt` is conservative, transactional, and idempotent. It resolves the Git
root, validates every generated file, and writes only after preflight succeeds.
When it cannot infer a real verification lane, it stops without changing the
repository.

Atlas publication is opt-in and requires GitHub Pages to use GitHub Actions as
its source:

```bash
fledge trust adopt --atlas
```

Other optional layers can be skipped with a recorded reason, for example
`fledge trust adopt --no-specs "content-only repository"`.

The decision is stored in `.trust.toml`, the canonical policy used by both the
local plugin and GitHub Action. Workflow overrides may strengthen that policy,
but cannot weaken it.

## Policy

Standard mode enforces lifecycle verification, SpecSync, and Augur. Attest is
progressive: an unavailable or unsatisfied provenance ledger is reported as
degraded while the repository adopts signed provenance. Strict mode forces
100% contract coverage and enforced provenance. Atlas is disabled unless
adoption explicitly opts into Pages publication with `--atlas`.

## GitHub Actions

The composite Action reads the same `.trust.toml` and resolves pull request,
push, and initial-push ranges from the GitHub event. Checkout must use full
history because Augur and Attest inspect commits and git notes.

```yaml
steps:
  - uses: actions/checkout@9c091bb21b7c1c1d1991bb908d89e4e9dddfe3e0 # v7.0.0
    with:
      fetch-depth: 0

  - uses: CorvidLabs/trust@v0
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
| `fledge trust --version` | Report the installed Trust plugin version. |

## Design boundary

This repository owns orchestration only. Parsing specs, scoring diffs, storing
attestations, and rendering Atlas remain in their respective repositories and
release independently.

## License

MIT
