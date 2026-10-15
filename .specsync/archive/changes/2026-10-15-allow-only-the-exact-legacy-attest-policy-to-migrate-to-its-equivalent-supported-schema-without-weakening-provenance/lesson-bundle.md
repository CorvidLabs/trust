# Lesson bundle — allow-only-the-exact-legacy-attest-policy-to-migrate-to-its-equivalent-supported-schema-without-weakening-provenance

Material for folding this change's lessons into the affected specs' `context.md`.
Synthesise from what actually happened below; do not restate the change description.

## What this change was

- **Title**: Allow only the exact legacy Attest policy to migrate to its equivalent supported schema without weakening provenance protection
- **Kind**: BugFix
- **Specs**: trust-action, trust-policy
- **Paths**: scripts/trust_cli.py, tests/test.sh, README.md, hi/
- **Acceptance**: Accept only the exact legacy require object with attestation, reviewer and testsPassed all true migrating to requireAttestation true, requireTestsPassed true and allowedReviewers agent:/human:; reject every weakening, unknown field, duplicate key, malformed JSON, invalid type, reverse migration and unrelated policy change; run all Trust checks and full Account verification without bypasses.

## Evidence

- Verification commit: `6eb34caadfb04587506edb42992f81e60d88c5f7`
- Base commit: `bccd89c111d47778c97c5064fb62ab51695e04ea`
- Verified by: `specsync check --spec trust-action --spec trust-policy --strict`

## From the change's context.md

# Context

Account PRs #11 and #12 cannot replace an unsupported nested Attest policy because Trust compares policy bytes against the protected base. The user approved a narrowly equivalent translation on 2026-10-15. An owner/admin merge remains unauthorized. Existing provenance modes, paths, scope, actor records and gates stay intact.

## From the change's design.md

# Design

Keep byte equality as the normal rule. For changed bytes, strictly parse JSON with duplicate-key rejection and accept exactly one direction: {require: {attestation: true, reviewer: true, testsPassed: true}} to {requireAttestation: true, requireTestsPassed: true, allowedReviewers: [agent:, human:]}. Compare canonical JSON to fixed shapes so integers cannot masquerade as booleans. Reject every other changed shape. No caller flag or permission bypass is added.

## From the change's testing.md

# Testing

Extend tests/test.sh with the exact accepted migration in a real PR event fixture plus direct negative cases for weakened/missing/unknown/duplicate fields, bool type confusion, malformed JSON and reverse/current-schema changes. Run fledge trust verify, strict SpecSync, hi check, Augur and genuine Attest verification. Verify Account frontend lint/tests/build and backend fmt/Clippy/tests/build before reporting success.

## Where these lessons go

- `specs/trust-action/context.md`
- `specs/trust-policy/context.md`
