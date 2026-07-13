---
change: CHG-0005-close-trust-1-0-1-contract-validation-and-canonical-quality-gaps
artifact: design
---

# Design

Replace the permissive version expression with a SemVer 2.0 expression that
distinguishes zero from non-zero numeric identifiers and excludes leading-zero
numeric prerelease segments. Preserve valid build metadata.

For local mirrors, parse the URL structurally, require an empty authority and
plain `file` scheme, reject query/fragment/control data and percent-encoded path
separators, decode the path once, and then reuse canonical filesystem boundary,
directory, child, and symlink checks. This admits spaces without admitting
encoded traversal.

Correct specifications to match actual surfaces: status JSON is readiness data;
Action outputs carry gate results; suppressed action commands are internal;
immutable composition covers nested dependencies; shared file mappings are
intentional responsibility slices. Normalize Change Log sections to the
two-column format written by the lifecycle and remove the unused placeholder
template.
