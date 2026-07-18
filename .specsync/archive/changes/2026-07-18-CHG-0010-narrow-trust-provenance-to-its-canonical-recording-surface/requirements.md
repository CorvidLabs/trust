---
change: CHG-0010-narrow-trust-provenance-to-its-canonical-recording-surface
artifact: requirements
---

# Requirements

## Functional

- `scripts/trust_cli.py` is owned solely by trust-policy; `action.yml` is
  owned solely by trust-action.
- trust-provenance owns `scripts/record_provenance.sh` and its Public API
  documents only exports present in that file.
- The composite action input/output surface stays documented exactly once,
  in trust-action.

## Acceptance criteria

- trust-provenance documents only exports present in its owned files.
- No source file is claimed by more than one canonical spec.
- `specsync check` (5.1.1) reports 5/5 specs passed with zero
  duplicate-ownership errors and 100% coverage.
