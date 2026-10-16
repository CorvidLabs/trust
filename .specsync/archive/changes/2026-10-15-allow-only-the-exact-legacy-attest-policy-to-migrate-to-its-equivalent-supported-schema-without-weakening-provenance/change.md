---
id: allow-only-the-exact-legacy-attest-policy-to-migrate-to-its-equivalent-supported-schema-without-weakening-provenance
state: archived
type: bug_fix
base_commit: bccd89c111d47778c97c5064fb62ab51695e04ea
---

# Allow only the exact legacy Attest policy to migrate to its equivalent supported schema without weakening provenance protection

## Intent

Allow only the exact legacy Attest policy to migrate to its equivalent supported schema without weakening provenance protection

## Affected Canonical Specs

- `trust-action`
- `trust-policy`

## Acceptance Criteria

- Accept only the exact legacy require object with attestation, reviewer and testsPassed all true migrating to requireAttestation true, requireTestsPassed true and allowedReviewers agent:/human:; reject every weakening, unknown field, duplicate key, malformed JSON, invalid type, reverse migration and unrelated policy change; run all Trust checks and full Account verification without bypasses.

## No-spec Rationale

Not applicable
