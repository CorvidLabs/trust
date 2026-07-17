---
change: CHG-0008-revalidate-the-trusted-specsync-mirror-immediately-before-contract-consumption
artifact: plan
---

# Plan

1. Add a focused internal command that reuses the existing SpecSync input resolver.
2. Invoke it after lifecycle verification and immediately before the contract action.
3. Add structural ordering coverage and a mutation regression that replaces a validated mirror file with a symlink.
4. Run native verification, record fresh SpecSync evidence, and require the hosted action matrix before promotion.
