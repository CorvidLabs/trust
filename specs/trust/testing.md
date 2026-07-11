---
spec: trust.spec.md
---

# Trust - Testing

## Automated Tests

| Test | What it verifies |
| --- | --- |
| Shell syntax | The plugin dispatcher and behavior test parse under Bash. |
| Manifest validation | Action, workflow, plugin, policy, and composed action references are structurally valid. |
| Dry-run adoption | No managed file is written. |
| Real adoption | Every expected managed file is created. |
| Idempotent adoption | A second run preserves existing files and the single managed rules block. |
| Managed rules update | An obsolete managed block is replaced while surrounding AGENTS.md content is preserved. |
| Status JSON | Output parses and reports workflow and rules wiring. |
| Verification order | Fake component commands observe lifecycle, contract, risk, and provenance in order. |
| Version identity | CLI and status output match the plugin manifest version. |
| Self-adoption | Trust's own policy, workflow, risk configuration, and managed rules pass doctor and verify. |
| Action matrix | Standard, strict, provenance, and fatal paths run on Linux and macOS fixture repositories. |
| Atlas opt-in | Default adoption records Atlas off; explicit adoption verifies reports and renders publication assets. |
| Windows plugin | The complete manifest and plugin behavior suite runs under Git Bash on `windows-latest`. |
| Tagged release | Tag/version identity, exact-tag installation, pinned tools, and monotonic channel selection. |
| Main provenance | Every green main CI matrix records, verifies, and durably publishes a risk-bound git note. |
| Homebrew renderer | Release version, archive digest, dependency version, placeholders, and Ruby syntax validate. |

## Manual Release Checks

- Run `fledge lanes run release` from a clean release commit.
- Rehearse the intended version with `fledge release VERSION --dry-run --pre-lane release --non-interactive`.
- Confirm the tag workflow publishes only after exact-tag installation and verification pass.
- Install the plugin through `fledge plugins install CorvidLabs/trust`.
- Adopt it into a disposable repository with at least one real language stack.
- Run the generated workflow on a pull request with full git history.
- Confirm the individual component checks remain diagnosable from the unified job.
