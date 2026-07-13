---
id: CHG-0005-close-trust-1-0-1-contract-validation-and-canonical-quality-gaps
state: verifying
type: bug_fix
base_commit: 5e531ed98e1af0f224e0d5a84104238c679fc393
---

# Close Trust 1.0.1 contract validation and canonical quality gaps

## Intent

Close Trust 1.0.1 contract validation and canonical quality gaps

## Affected Canonical Specs

- `trust`
- `trust-action`
- `trust-plugin`
- `trust-policy`
- `trust-provenance`

## Acceptance Criteria

- Exact SpecSync versions reject every SemVer leading-zero violation
- safe authority-free file URLs beneath RUNNER_TEMP accept percent-encoded spaces while encoded traversal and separators remain rejected
- CLI status requirements describe the emitted versioned configuration-health document without claiming gate component results
- nested action components remain immutable while public generated workflow documentation may use the supported major channel
- suppressed action plumbing is documented as internal rather than public CLI
- the unused placeholder verification template is removed
- all five canonical Change Log tables are well-formed and deduplicated
- the full Trust release lane and strict 100 percent SpecSync validation pass.

## No-spec Rationale

Not applicable
