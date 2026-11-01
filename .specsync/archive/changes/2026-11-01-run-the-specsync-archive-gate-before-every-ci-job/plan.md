---
change: run-the-specsync-archive-gate-before-every-ci-job
artifact: plan
---

# Plan

## Approach

Add an `archive-gate` job, displayed as `Archive`, at the top of `jobs:` in
`.github/workflows/ci.yml` and `.github/workflows/trust.yml`. It checks out the
pull request head (or the pushed commit) with the workflow's existing pinned
`actions/checkout`, without persisted credentials, and runs
`CorvidLabs/spec-sync@106aaa43d0bcf049f19b173ddb63815a25c3f931` with
`archive-gate-only: 'true'` on `ubuntu-latest` with a five-minute timeout.
Every job without `needs` gains `needs: archive-gate`.

## Out of scope

- `release.yml`, which runs only on version tags.
- The org ruleset that requires the Archive check.
- The two changes already open on the default branch.
- Moving the pin to a release tag; that follows once a release ships the gate.

## Steps

1. Insert the archive-gate job at the top of `jobs:` in both workflows.
2. Add `needs: archive-gate` to `validate`, `plugin-windows`, `action-smoke`,
   `action-provenance`, `action-atlas`, `action-fatal-paths`,
   `repository-trust` (ci.yml) and `trust` (trust.yml).
3. Leave `record-provenance` unchanged: its needs list reaches archive-gate
   transitively and `scripts/validate.py` asserts that list verbatim.
4. Parse both workflows and print each job's needs to confirm the graph.
5. Run the repository's own validation and tests.

## Risks

- While any change is open, no other CI job runs; that is the intended effect,
  and it applies to this pull request until the preexisting open changes are
  archived.
- The pin is a commit on spec-sync main rather than a release; it must be
  moved to the first release that includes the gate.
- A skipped downstream job reports as passing, so merge blocking depends on the
  org ruleset requiring Archive.

## Constraints consulted

AGENTS.md: keep generated trust configuration and the managed block in place
(untouched), keep module specs synchronized with implementation (no spec owns
the workflows, so none changes), and do not bypass or weaken the trust gate
(every existing job and the Repository Trust gate still run, after the archive
gate). `scripts/validate.py` requires full-SHA pins for external actions, which
the new step satisfies.
