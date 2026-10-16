---
change: allow-only-the-exact-legacy-attest-policy-to-migrate-to-its-equivalent-supported-schema-without-weakening-provenance
artifact: context
---

# Context

Account PRs #11 and #12 cannot replace an unsupported nested Attest policy because Trust compares policy bytes against the protected base. The user approved a narrowly equivalent translation on 2026-10-15. An owner/admin merge remains unauthorized. Existing provenance modes, paths, scope, actor records and gates stay intact.
