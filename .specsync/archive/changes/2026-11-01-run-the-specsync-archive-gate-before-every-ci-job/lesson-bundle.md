# Lesson bundle — run-the-specsync-archive-gate-before-every-ci-job

Material for folding this change's lessons into the affected specs' `context.md`.
Synthesise from what actually happened below; do not restate the change description.

## What this change was

- **Title**: Run the SpecSync archive gate before every CI job
- **Kind**: Operations
- **Paths**: .github/workflows/ci.yml, .github/workflows/trust.yml
- **Acceptance**: ci.yml and trust.yml each start with an archive-gate job named Archive that runs CorvidLabs/spec-sync pinned at 106aaa43d0bcf049f19b173ddb63815a25c3f931 with archive-gate-only 'true' and fails while any change under .specsync/changes/ is open; every other job in those workflows needs archive-gate directly or transitively, so nothing else runs until the change is archived.

## Evidence

- Verification commit: `15ab1b92bc93f0a3a5122982f96dbf5f432672be`
- Base commit: `68603eb9e428b801bf9ff4bad2049c0bbdc3a1bb`
- Verified by: `specsync check (no spec in scope)`

## From the change's context.md

# Context

Every SpecSync change must be archived before a pull request merges, and CI
should spend nothing on a pull request until it is. This is the org-wide rollout
of CorvidLabs/spec-sync#832 (merged as
106aaa43d0bcf049f19b173ddb63815a25c3f931), which added an archive gate to the
spec-sync GitHub Action: `archive-gate-only: 'true'` runs only
`.github/scripts/archive-readiness.sh` (bash and python3, no binary download)
and fails while any change under `.specsync/changes/` is still open. The
rollout was approved by 0xLeif.

Published spec-sync v6.1.1 and older ignore the new input, so the step pins the
commit instead of a release tag; it should move to the first release that ships
the gate. Branch protection is configured separately by an org ruleset that
requires a check named Archive, which is why the job's display name is exactly
`Archive`. A skipped job counts as passing, so merge blocking relies on that
ruleset rather than on the downstream jobs.

`release.yml` triggers only on version tags and is out of scope. At the time of
this change the default branch already carries two open changes
(`CHG-0003-add-trusted-specsync-self-host-artifact-inputs` and
`pin-specsync-6-0-0-as-the-trust-1-2-0-contract-toolchain`); this change does
not touch them, and the Archive check stays red until their owners archive them.

## From the change's testing.md

# Testing

- Both edited workflows parse with Ruby Psych `safe_load`, and the printed job
  graph shows `archive-gate` with no needs and every other job needing it
  directly, or transitively for `record-provenance`.
- `python3 scripts/validate.py` passes (full-SHA pins, the verbatim
  `record-provenance` needs list, pinned validation dependency).
- `bash tests/test.sh` passes.
- `bash .github/scripts/archive-readiness.sh .` from spec-sync at the pinned
  behaviour fails while changes are open under `.specsync/changes/`, which is
  the expected result until they are archived.
- In CI, the Archive job runs first on pull requests and pushes to main, and no
  other job in ci.yml or trust.yml starts unless it succeeds.

## Where these lessons go

This change declared no affected specs, so there is no module context to fold into.
