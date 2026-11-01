---
change: run-the-specsync-archive-gate-before-every-ci-job
artifact: testing
---

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
