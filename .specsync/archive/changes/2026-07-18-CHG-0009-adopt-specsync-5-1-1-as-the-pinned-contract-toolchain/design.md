---
change: CHG-0009-adopt-specsync-5-1-1-as-the-pinned-contract-toolchain
artifact: design
---

# Design

The change is a coordinated pin flip plus a ledger backfill; no new
components or control flow.

- **Pin surface**: the nested SpecSync action moves to immutable commit
  `a89d827e93fa0bc9e6168447e66a0ad30fa92e65` (v5.1.1) and every default,
  assertion, and document naming 5.0.1 moves to 5.1.1 in the same change,
  keeping action code and binary paired.
- **Ledger backfill**: 5.1.1 requires `stale_acceptance_input_digest` and
  `current_acceptance_input_digest` on reopening records. The backfill is
  additive: `stale` copies each reopening's embedded
  `prior_verification.acceptance_input_digest`; `current` takes the next
  acceptance digest in the ledger chain (equal to `stale` for
  evidence-refresh reopens whose delivery inputs did not change). Serde on
  5.0.1 ignores unknown fields, so both binaries validate the result.
- **Evidence continuity**: 5.0.1 closing digests are byte-identical under
  5.1.1 when no acceptance manifest is present, so previously accepted
  changes keep validating; delivery-input changes from this flip are
  handled through native reopen/re-acceptance without delta replay.
- **Consumer reuse**: the migration script ships in `scripts/` so other
  repositories can backfill before their first 5.1.1 validation.
