---
change: CHG-0008-revalidate-the-trusted-specsync-mirror-immediately-before-contract-consumption
artifact: docs
---

# Docs

The public inputs and supported self-hosting workflow do not change. The canonical action contract now states that mirror confinement and symlink checks run both before lifecycle execution and immediately before contract consumption. No README expansion is needed for this internal security boundary.
