---
change: CHG-0003-add-trusted-specsync-self-host-artifact-inputs
artifact: research
---

# Research

The nested SpecSync 5 action already supports `version` and `download-base-url` and verifies adjacent SHA-256 files before extraction. Trust currently hard-codes version 5.0.1 and exposes no override. `urllib.parse` plus `Path.resolve(strict=True)` can reject authority, query, fragment, traversal, missing directories, and symlink escape before any component runs.
