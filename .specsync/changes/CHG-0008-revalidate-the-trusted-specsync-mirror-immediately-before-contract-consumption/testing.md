---
change: CHG-0008-revalidate-the-trusted-specsync-mirror-immediately-before-contract-consumption
artifact: testing
---

# Testing

- Assert the composite step order is lifecycle, mirror revalidation, then contract gate.
- Validate a mirror successfully, replace one contained file with an external symlink, and assert `action-revalidate-specsync` raises `TrustError`.
- Run `fledge lanes run verify` for syntax, manifest, native behavior, and strict contract checks.
- Require the hosted action smoke, provenance, failure-path, Atlas, repository-gate, CodeQL, and Windows plugin jobs to pass before promotion.
