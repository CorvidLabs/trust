---
change: run-the-specsync-archive-gate-before-every-ci-job
artifact: context
---

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
