---
change: CHG-0005-close-trust-1-0-1-contract-validation-and-canonical-quality-gaps
artifact: requirements
---

# Requirements

- Exact SpecSync input versions obey SemVer numeric-identifier leading-zero
  rules for core and prerelease components.
- Runner-local `file://` mirrors accept canonical percent-encoding for safe path
  characters while rejecting encoded separators, traversal, authorities,
  queries, fragments, controls, and symlink escape.
- Status JSON promises configuration health, tool availability, and managed-file
  state; gate component results remain Action outputs.
- Immutable composition applies to nested released components. Public templates
  may demonstrate the supported major channel, while CorvidLabs consumers pin a
  reviewed release commit.
- Hidden action plumbing remains an internal interface.
- Canonical stable specs contain well-formed, unique audit history and shipped
  templates contain no false-green placeholder task.
