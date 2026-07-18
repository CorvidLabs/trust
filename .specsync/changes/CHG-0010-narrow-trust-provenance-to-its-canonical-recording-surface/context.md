---
change: CHG-0010-narrow-trust-provenance-to-its-canonical-recording-surface
artifact: context
---

# Context

SpecSync 5.1.1 strict validation requires every source file to have exactly
one canonical spec owner. The Trust 1 contract split gave
`scripts/trust_cli.py` four owners and `action.yml` two. CHG-0009 adopted
5.1.1; this change completes it by consolidating ownership and narrowing the
trust-provenance Public API to the surface present in its canonical file,
`scripts/record_provenance.sh`. The full composite action surface remains
documented once, by trust-action.
