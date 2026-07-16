---
change: CHG-0005-close-trust-1-0-1-contract-validation-and-canonical-quality-gaps
artifact: testing
---

# Testing

- Add negative exact-version cases for leading-zero core and prerelease numeric
  identifiers and positive cases for valid prerelease/build metadata.
- Add a positive mirror path containing spaces and negative encoded separator,
  encoded traversal, authority, query, fragment, sibling, root, missing,
  non-directory, and symlink-escape cases.
- Assert status/doctor JSON schema, version, health, tools, files, and errors.
- Validate the public template's major channel separately from immutable nested
  component pins and CorvidLabs consumer policy.
- Assert the unused placeholder template is absent and every canonical Change
  Log row matches its two-column header without duplicate change IDs.
- Run `fledge lanes run release`, all agent status checks, and local Trust doctor
  and verify before closing approval.
