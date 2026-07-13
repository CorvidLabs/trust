---
change: CHG-0003-add-trusted-specsync-self-host-artifact-inputs
artifact: context
---

# Context

Trust 1.0.0 always composes released SpecSync 5.0.1. That is correct for consumers but prevents SpecSync from validating pull requests that evolve its own lifecycle schema. Disabling the contract is forbidden and unsafe. Trust needs a constrained bootstrap input that preserves released defaults while allowing SpecSync CI to supply a checksummed local action artifact.
