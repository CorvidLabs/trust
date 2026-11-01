---
id: run-the-specsync-archive-gate-before-every-ci-job
state: approved
type: operations
base_commit: 68603eb9e428b801bf9ff4bad2049c0bbdc3a1bb
---

# Run the SpecSync archive gate before every CI job

## Intent

Run the SpecSync archive gate before every CI job

## Affected Canonical Specs

- None

## Acceptance Criteria

- ci.yml and trust.yml each start with an archive-gate job named Archive that runs CorvidLabs/spec-sync pinned at 106aaa43d0bcf049f19b173ddb63815a25c3f931 with archive-gate-only 'true' and fails while any change under .specsync/changes/ is open; every other job in those workflows needs archive-gate directly or transitively, so nothing else runs until the change is archived.

## No-spec Rationale

CI workflow ordering only; no canonical spec owns .github/workflows
