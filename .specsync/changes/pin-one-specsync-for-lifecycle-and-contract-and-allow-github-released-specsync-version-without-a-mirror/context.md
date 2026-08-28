---
change: pin-one-specsync-for-lifecycle-and-contract-and-allow-github-released-specsync-version-without-a-mirror
artifact: context
---

# Context

CorvidLabs/trust#29: Trust's lifecycle step used whatever `specsync` was on
the runner PATH, while the contract step installed Trust's pin. A self-hosted
runner with a SpecSync 6 RC made `specsync check --strict` in a lifecycle
script fail, while `main` on GitHub-hosted runners stayed green.

Non-default `specsync-version` also required a `file://` mirror, so consumers
could not opt into SpecSync 6 on Trust 1.1.2. Trust 1.2.0-rc.1 defaults to
6.0.0-rc.9, but lifecycle still ignored that pin.
