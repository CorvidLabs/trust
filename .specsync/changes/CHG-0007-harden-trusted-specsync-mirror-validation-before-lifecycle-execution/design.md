---
change: CHG-0007-harden-trusted-specsync-mirror-validation-before-lifecycle-execution
artifact: design
---

# Design

Introduce `DEFAULT_SPECSYNC_VERSION` as the single released default. Resolve inputs in this order: exact SemVer, default-versus-mirror policy, URL syntax and encoding, mirror and boundary directories, then recursive entry validation.

The recursive validator enumerates without following links. It rejects each symbolic link before resolution, resolves every remaining entry strictly, verifies the result remains beneath the already resolved `RUNNER_TEMP`, and only descends into validated directories. Any inspection or resolution failure becomes `TrustError`.
