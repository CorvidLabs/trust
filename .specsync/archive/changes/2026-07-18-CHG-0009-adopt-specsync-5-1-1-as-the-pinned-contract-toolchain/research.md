---
change: CHG-0009-adopt-specsync-5-1-1-as-the-pinned-contract-toolchain
artifact: research
---

# Research

- Component survey (2026-07-18): spec-sync v5.1.1 is the latest 5.x
  release; fledge v1.7.0, attest 1.0.0, augur 1.0.0, and
  fledge-plugin-atlas v1.3.1 are already the latest in their majors.
- v5.1.1 release notes: lifecycle evidence hardening and a static
  x86_64-musl build; the tag object `cb52f0f7` peels to commit
  `a89d827e93fa0bc9e6168447e66a0ad30fa92e65`, matching the existing
  pin pattern (v5.0.1 tag peels to the currently pinned `59bbfa76`).
- Compatibility evidence gathered on this repository's ledgers before
  definition approval: with the additive reopening backfill, both
  `specsync check` 5.0.1 and 5.1.1 exit 0; all 40 historical reopenings
  and 8 closing approvals reproduce their recorded digests under the
  5.1.1 verifier; manifest-less verification records remain accepted
  through the 5.1.1 legacy path.
- Alternatives considered: staying on 5.0.1 (rejected — misses lifecycle
  hardening and strands local Homebrew tooling at a parse-incompatible
  version); moving to 5.1.1 without the ledger backfill (rejected — the
  contract gate fails closed on unparseable reopening records).
