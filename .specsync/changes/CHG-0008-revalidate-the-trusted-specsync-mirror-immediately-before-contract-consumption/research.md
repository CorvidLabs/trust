---
change: CHG-0008-revalidate-the-trusted-specsync-mirror-immediately-before-contract-consumption
artifact: research
---

# Research

Initial path validation does not protect a later filesystem read when an intervening untrusted process can mutate the validated directory. Trust's lifecycle lane executes repository-controlled commands between configuration resolution and SpecSync artifact download, so the existing validation has a time-of-check/time-of-use gap.

Reusing `resolve_specsync_inputs` at the consumption boundary covers both ordinary file replacement and symlink replacement without introducing a second validation implementation.
