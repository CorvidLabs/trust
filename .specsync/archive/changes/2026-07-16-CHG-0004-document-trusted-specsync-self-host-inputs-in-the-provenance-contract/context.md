---
change: CHG-0004-document-trusted-specsync-self-host-inputs-in-the-provenance-contract
artifact: context
---

# Context

The provenance companion intentionally maps `action.yml` because Trust's action
surface controls how provenance verification participates in the unified gate.
CHG-0003 added two validated SpecSync self-host inputs to that shared action
surface and documented them in `trust-action`, but `trust-provenance` still
omits them. Strict export coverage therefore correctly reports two undocumented
public inputs in this companion.
