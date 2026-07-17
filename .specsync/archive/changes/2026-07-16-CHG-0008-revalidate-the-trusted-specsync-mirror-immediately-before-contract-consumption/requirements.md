---
change: CHG-0008-revalidate-the-trusted-specsync-mirror-immediately-before-contract-consumption
artifact: requirements
---

# Requirements

- The action SHALL revalidate configured SpecSync mirror inputs after lifecycle verification and before the immutable SpecSync contract action.
- Revalidation SHALL enforce the same exact-version, local-file URL, `RUNNER_TEMP` boundary, and recursive non-symlink rules as initial resolution.
- A mirror entry replaced with a symlink during lifecycle verification SHALL fail before contract consumption.
- Released default behavior without a mirror SHALL remain unchanged.
