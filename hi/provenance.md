---
hi: 1
families: [PROVENANCE]
---

# Signed provenance, adopted gradually

## Intent

Most repositories cannot turn on signed provenance overnight, so Trust lets them live in a state where a missing ledger is reported rather than fatal, and tighten later. Trust verifies the attestations it finds; it never signs one on a contributor's behalf, because that would make the evidence worthless. A repository that only signs after merge can have provenance judged on the base its change sits on, while verification, contracts, and risk still judge the change itself — which keeps the proof inductive as long as the base is genuinely current. After a change lands, CI records the note that the next change will rest on.

## Criteria

- **PROVENANCE-1**  A repository can adopt signed provenance gradually instead of all at once.
  - **PROVENANCE-1.a**  A ledger that does not exist yet is reported as degraded while provenance is soft.
  - **PROVENANCE-1.b**  A ledger that does not exist fails the gate once provenance is enforced.
- **PROVENANCE-2**  Trust verifies the attestations it finds.
- **PROVENANCE-3**  Trust never signs an attestation on my behalf.
- **PROVENANCE-4**  Provenance can be judged on the commits I am proposing.
- **PROVENANCE-5**  Provenance can instead be judged on the base my change sits on, so signing can happen after merge.
  - **PROVENANCE-5.a**  Judging provenance on the base leaves verification, contracts, and risk judging the proposed commits.
  - **PROVENANCE-5.b**  A proposed change whose base branch has moved on is failed rather than trusted.
- **PROVENANCE-6**  The remote ledger is fetched before verification so a note recorded by CI is actually visible.
- **PROVENANCE-7**  A provenance report that disagrees with the tool's own exit status is treated as a broken run, not a pass.
- **PROVENANCE-8**  After a change lands, CI records a signed note for it so the next change has an attested base to build on.
  - **PROVENANCE-8.a**  The note is signed only after the repository's own gate has passed.
  - **PROVENANCE-8.b**  The note carries the risk assessment recorded for the landed commits.
  - **PROVENANCE-8.c**  A note already present that does not satisfy the policy is repaired rather than left alone.
  - **PROVENANCE-8.d**  Two runs publishing notes at the same time merge instead of one clobbering the other.
- **PROVENANCE-9**  A provenance failure shows the commits that violated the policy, not just that provenance failed.
