---
change: CHG-0009-adopt-specsync-5-1-1-as-the-pinned-contract-toolchain
artifact: plan
---

# Plan

1. Land the additive ledger backfill (commit `cccb7d2`) and the reusable
   `scripts/migrate_specsync_5_1_records.py` migration script.
2. Flip every SpecSync pin to 5.1.1: `action.yml` (default, description,
   nested action commit), `scripts/trust_cli.py`, `scripts/validate.py`,
   `.github/workflows/release.yml`, `README.md`, `RELEASING.md`.
3. Update the canonical contract through semantic deltas (trust-action,
   trust-provenance).
4. Run the full verification lane and strict contract validation with the
   5.1.1 binary; record fresh verification evidence.
5. Accept; after merge, reopen any accepted changes made stale by the new
   delivery inputs and re-accept them natively under 5.1.1 (no delta
   replay), then cut the 1.1.0 release.
