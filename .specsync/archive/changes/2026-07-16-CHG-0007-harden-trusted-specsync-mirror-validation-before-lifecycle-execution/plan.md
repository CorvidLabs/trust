---
change: CHG-0007-harden-trusted-specsync-mirror-validation-before-lifecycle-execution
artifact: plan
---

# Plan

1. Add focused resolver policy and recursive mirror-entry validation.
2. Extend the native action-input regressions without weakening existing cases.
3. Commit the implementation before recording verification evidence.
4. Reopen only previously accepted changes whose recorded inputs became stale, then reverify without replaying their already applied deltas.
5. Accept CHG7, run the strict final gate, and push for hosted verification.
