# Releasing Trust

Trust releases must prove both the repository implementation and its governed
contract. Run releases only from a clean `main` commit after its hosted checks
pass.

## First pre-1.0 tag

The intended first dogfood tag is `v0.2.0`. Rehearse it without changing git:

```bash
fledge lanes run release
fledge release 0.2.0 --dry-run --pre-lane release --non-interactive
```

After reviewing the version and generated changelog, create and push the exact
release through Fledge:

```bash
fledge release 0.2.0 --pre-lane release --push --non-interactive
```

The tag workflow then validates tag/version identity, installs the exact tag
through Fledge, and runs `doctor` plus `verify` with the pinned component
binaries in a disposable repository. It creates the GitHub prerelease and
records the eligible `v0` channel promotion only after those gates pass.

The `v0` tag ruleset intentionally reserves force-updates for organization
administrators. After the tag workflow succeeds, an administrator verifies the
workflow summary and promotes the protected channel:

```bash
git fetch --tags
git tag -f v0 v0.2.0
git push origin -f refs/tags/v0
```

Install the immutable tag into a disposable repository rather than using the
Trust source checkout:

```bash
fledge plugins install CorvidLabs/trust@v0.2.0
fledge trust adopt --dry-run
fledge trust adopt
fledge trust doctor
fledge trust verify
```

Only after exact-tag dogfooding and the generated GitHub workflow pass should
the supported `v0` Action channel be created at `v0.2.0`.

## Stable release

Trust 1.0.0 additionally requires spec-sync 5.0.0, an enabled provenance
ledger, the Homebrew bundle, the promoted active spec, and the `v1` Action
channel. Keep dependency Action code pinned to immutable commits and pair each
pin with its matching binary version before the final release rehearsal.
The same tag workflow publishes 1.0.0 as a stable GitHub release and selects
`v1`; a 1.0.0 release candidate is ineligible for that stable channel. Create a
maintainer-managed `v1` tag ruleset before the stable promotion.
Major channels move monotonically: publishing or replaying an older release
cannot roll `v0` or `v1` backward.
