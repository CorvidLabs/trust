---
change: CHG-0008-revalidate-the-trusted-specsync-mirror-immediately-before-contract-consumption
artifact: design
---

# Design

Add a hidden `action-revalidate-specsync` command that calls the same exact-version, URL, directory, boundary, and recursive-entry validator used during initial configuration. The composite action invokes it with the already resolved outputs and `runner.temp` after lifecycle verification and directly before the contract gate.

Using the shared resolver prevents the two validation boundaries from drifting. The released default without a mirror remains valid, while a configured mirror must still exist, remain beneath `RUNNER_TEMP`, and contain no symlink entries at the second boundary.
