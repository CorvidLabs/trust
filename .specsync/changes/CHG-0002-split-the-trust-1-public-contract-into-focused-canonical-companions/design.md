---
change: CHG-0002-split-the-trust-1-public-contract-into-focused-canonical-companions
artifact: design
---

# Design

Retain `trust` as the orchestration and distribution contract. Move unique file ownership into `trust-action`, `trust-plugin`, `trust-policy`, and `trust-provenance`. Each companion remains strict, uses stable requirements, and maps its declared files at 100% coverage.
