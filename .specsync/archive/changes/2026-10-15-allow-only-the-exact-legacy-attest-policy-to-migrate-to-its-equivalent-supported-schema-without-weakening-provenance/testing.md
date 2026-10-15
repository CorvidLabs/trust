---
change: allow-only-the-exact-legacy-attest-policy-to-migrate-to-its-equivalent-supported-schema-without-weakening-provenance
artifact: testing
---

# Testing

Extend tests/test.sh with the exact accepted migration in a real PR event fixture plus direct negative cases for weakened/missing/unknown/duplicate fields, bool type confusion, malformed JSON and reverse/current-schema changes. Run fledge trust verify, strict SpecSync, hi check, Augur and genuine Attest verification. Verify Account frontend lint/tests/build and backend fmt/Clippy/tests/build before reporting success.
