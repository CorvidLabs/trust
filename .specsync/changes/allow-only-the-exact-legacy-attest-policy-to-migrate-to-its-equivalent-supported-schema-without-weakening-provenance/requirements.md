---
change: allow-only-the-exact-legacy-attest-policy-to-migrate-to-its-equivalent-supported-schema-without-weakening-provenance
artifact: requirements
---

# Requirements

### REQ-trust-policy-008

Trust SHALL accept only the exact equivalent legacy Attest schema translation while retaining rejection of unrelated committed-policy changes.

Acceptance Criteria

- All three legacy requirements remain enforced by the supported policy.
- False values, numeric boolean substitutes, missing/extra/duplicate keys, malformed JSON, role changes, reverse translation and changes to current supported policies fail closed.
- Unchanged policy bytes retain their existing behavior.
- Account full verification passes against the repaired action.
