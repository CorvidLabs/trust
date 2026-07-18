# Releasing Trust

Trust releases must prove both the repository implementation and its governed
contract. Run releases only from a clean `main` commit after its hosted checks
pass.

## Corrective pre-1.0 tag

The immutable `v0.2.0` tag proved source validation and plugin installation but
failed final dogfooding because suffixed component assets were not exposed as
canonical commands. Do not move or overwrite it. Rehearse `v0.2.1` without
changing git:

```bash
fledge lanes run release
fledge release 0.2.1 --dry-run --pre-lane release --non-interactive
```

After reviewing the version and generated changelog, create and push the exact
release through Fledge:

```bash
fledge release 0.2.1 --pre-lane release --push --non-interactive
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
git tag -f v0 v0.2.1
git push origin -f refs/tags/v0
```

Install the immutable tag into a disposable repository rather than using the
Trust source checkout:

```bash
fledge plugins install CorvidLabs/trust@v0.2.1
fledge trust adopt --dry-run
fledge trust adopt
fledge trust doctor
fledge trust verify
```

Only after exact-tag dogfooding and the generated GitHub workflow pass should
the supported `v0` Action channel be created at `v0.2.1`.

## Provenance bootstrap

Trust self-provenance uses enforced `baseline` scope. Pull requests and main
pushes verify the already-attested base while lifecycle, contract, and risk
gate the proposed range. The main provenance job records a risk-bound,
tests-passed note for the landed commit, verifies the committed policy, and
fails if the remote note cannot be published durably.

After the readiness merge, verify the external ledger proof locally:

```bash
git fetch origin "+refs/notes/attest:refs/notes/attest"
attest verify --commit origin/main --policy .attest.json
```

Do not claim the provenance release gate complete until both the hosted record
job and this remote-ledger verification pass.

Branch governance must require pull requests to be current with `main`. That
keeps the proof inductive: the base is attested before merge and the landed
commit is attested before another proposal based on it can pass.

## Homebrew bundle

After the immutable tag exists, download its GitHub source archive, calculate
the SHA-256, and render the formula with the matching SpecSync version:

```bash
python3 scripts/render_homebrew_formula.py 0.2.1 ARCHIVE_SHA256 \
  --specsync-version 5.0.1
```

Copy the output to `Formula/corvid-trust.rb` in `CorvidLabs/homebrew-tap` only
after the real digest is known. The formula installs the plugin under `libexec`,
wraps it with the guaranteed Homebrew Python path, depends on the four pinned
component formulae, and tests discovery through `fledge trust --version`.

For Homebrew installations with third-party tap trust enforcement, grant
formula-scoped trust to `corvid-trust`, `fledge`, `spec-sync`, `augur`, and
`attest`; whole-tap trust is not required.

## Stable release

Trust 1.0.0 additionally requires an enabled provenance ledger, the Homebrew
bundle, the promoted active spec, and the `v1` Action channel. SpecSync 5.1.1 is
pinned to its immutable Action commit and paired with binary version 5.1.1;
preserve that pairing through the final release rehearsal.
The same tag workflow publishes 1.0.0 as a stable GitHub release and selects
`v1`; a 1.0.0 release candidate is ineligible for that stable channel. Create a
maintainer-managed `v1` tag ruleset before the stable promotion.
Major channels move monotonically: publishing or replaying an older release
cannot roll `v0` or `v1` backward.

After the exact `v1.0.0` tag workflow passes and an administrator promotes the
protected `v1` channel, stable consumers install the immutable plugin tag and
use the supported major Action channel:

```bash
fledge plugins install CorvidLabs/trust@v1.0.0
```

```yaml
- uses: CorvidLabs/trust@v1
```
