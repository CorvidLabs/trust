---
change: allow-only-the-exact-legacy-attest-policy-to-migrate-to-its-equivalent-supported-schema-without-weakening-provenance
artifact: design
---

# Design

Keep byte equality as the normal rule. For changed bytes, strictly parse JSON with duplicate-key rejection and accept exactly one direction: {require: {attestation: true, reviewer: true, testsPassed: true}} to {requireAttestation: true, requireTestsPassed: true, allowedReviewers: [agent:, human:]}. Compare canonical JSON to fixed shapes so integers cannot masquerade as booleans. Reject every other changed shape. No caller flag or permission bypass is added.
