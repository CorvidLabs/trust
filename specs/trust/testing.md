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
| Tagged release | Source contract validation, tag/version identity, exact-tag installation, enforced baseline provenance, pinned tools, and monotonic channel selection. |
| Component exposure | Relative suffixed Augur and Attest assets resolve to absolute executable canonical command links. |
| Main provenance | The in-workflow Trust gate passes before CI repairs, verifies, and durably publishes a risk-bound git note. |
| Homebrew renderer | Release version, archive digest, dependency version, executable wrapper target, placeholders, Ruby syntax, and style validate. |
| Active contract | Released SpecSync 5.0.1 reports 30/30 exports, zero warnings, and zero failures. |
| Baseline provenance | Risk retains the proposed range while Attest verifies its resolved base commit. |
| Stale baseline | Baseline pull requests fail when the protected remote branch has advanced. |
| Policy immutability | Pull requests cannot weaken or replace the committed Attest policy contents. |
| Base availability | Missing pull request base objects fail closed instead of bypassing policy comparison. |
| External fixture isolation | Governed worktrees with a different origin require explicit ranges and ignore host PR metadata. |
| Repository identity | Same-named repositories on another server remain external to the host GitHub event. |

## Manual Release Checks

- Run `fledge lanes run release` from a clean release commit.
- Rehearse the intended version with `fledge release VERSION --dry-run --pre-lane release --non-interactive`.
- Confirm the tag workflow publishes only after exact-tag installation and verification pass.
- Install the plugin through `fledge plugins install CorvidLabs/trust`.
- Adopt it into a disposable repository with at least one real language stack.
- Run the generated workflow on a pull request with full git history.
- Confirm the individual component checks remain diagnosable from the unified job.
