---
spec: trust.spec.md
---

# Trust - Context

## Release Intent

Trust 1.0.0 is the first stable orchestration contract for the CorvidLabs trust
toolchain. It must ship on spec-sync 5.0.0 rather than merely accepting it as an
optional upgrade after release.

## Architecture Decisions

- Trust owns orchestration and policy strength, while component repositories
  continue to own parsing, risk scoring, provenance, and visualization.
- Lifecycle verification runs before contract, risk, and provenance gates. A
  repository lifecycle lane must not depend on tools installed by later gates.
- `.trust.toml` is the committed policy authority for local and CI execution.
  Workflow inputs may strengthen that policy but cannot weaken it.
- Composite Action code is pinned to immutable commits and paired with explicit
  component binary versions.
- Atlas is disabled by default. Explicit opt-in adds local report verification
  and push-only publication with Pages permissions isolated to the deploy job.
- Pre-release consumers use the `v0` Action channel after the first tag. Trust
  1.0.0 promotes the supported channel to `v1`.

## Current External Gates

- spec-sync 5.0.0 is released and pinned for both local and composite Action verification.
  The dotted-symbol parser fix is prepared in CorvidLabs/spec-sync#344 for 5.0.1,
  and Trust's Public API table is aligned to reach exact active coverage with
  that fix. The contract remains in review until 5.0.1 is released and pinned.
- A tagged Trust release is required before the Homebrew bundle and tagged
  plugin installation path can be tested honestly.
- Main-branch CI is prepared to bootstrap `refs/notes/attest` after the
  readiness work lands; enforced provenance waits for that durable first note.
- Repositories opting into Atlas must configure GitHub Pages to use GitHub
  Actions before their first publication push.

## Trust 1.0.0 Proof

The stable release requires all of the following evidence:

1. The plugin behavior suite and composite Action matrix pass on every supported
   operating system.
2. Trust is installed from a tag, adopted into a disposable repository, and run
   through doctor and verify without relying on the source checkout.
3. The Trust repository passes its own local and GitHub-hosted gate with an
   enabled provenance ledger.
4. The contract is validated and promoted to active by spec-sync 5.0.0.
5. Atlas behavior is either fully published by the generated workflow or
   explicitly disabled with a recorded reason; enabled-but-unused policy is not
   acceptable.
6. The Homebrew bundle, `v1` Action channel, release notes, and 1.0.0 artifacts
   are verified after the final immutable dependency pins are known.
