---
change: allow-only-the-exact-legacy-attest-policy-to-migrate-to-its-equivalent-supported-schema-without-weakening-provenance
artifact: plan
---

# Plan

1. Record the approved criteria and definition.
2. Add the exact one-way migration predicate and regression checks.
3. Materialize owning policy/action specs and run full Trust verification.
4. Publish a ready-for-review Trust PR with genuine provenance.
5. Pin that immutable action commit in Account repair branches, carry current main runner setup and async-trait compatibility, then run native and hosted verification.
6. Present evidence for genuine human closing review. No merge or deployment.
