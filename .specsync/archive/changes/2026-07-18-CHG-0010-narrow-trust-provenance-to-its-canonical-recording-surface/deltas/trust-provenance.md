## MODIFIED

### SPEC SECTION Public API

The provenance surface supports soft or enforced verification, range or baseline
scope, remote note discovery, and release-action note recording. The recording
contract takes the pinned Attest and Augur binaries, a landed comparison range,
and an Augur JSON report; it signs a policy-satisfying note for the landed
commit and publishes the Attest ledger with merge-and-retry semantics.
