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
