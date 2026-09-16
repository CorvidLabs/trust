---
hi: 1
families: [POLICY]
---

# One committed decision

## Intent

How strongly a repository is gated is a decision the repository makes once, in a file it commits, and that decision governs both a laptop and CI. The file should be unforgiving about things it does not understand, because a typo that silently disables a gate is worse than a typo that stops the run. Strength is a one-way ratchet: a run, a workflow, or a proposed change can tighten the gate, and nothing can loosen what the branch already committed. Turning a layer off is allowed, but only out loud, with a reason someone wrote down.

## Criteria

- **POLICY-1**  One committed file decides how strongly this repository is gated.
  - **POLICY-1.a**  That same file governs a run on my laptop.
  - **POLICY-1.b**  That same file governs a run in CI.
- **POLICY-2**  A standard profile gates verification, contracts, and risk while signed provenance is still being adopted.
- **POLICY-3**  A strict profile demands complete contract coverage.
- **POLICY-4**  A strict profile demands enforced provenance.
- **POLICY-5**  A setting Trust does not recognize is refused rather than ignored.
  - **POLICY-5.a**  A layer switched off without a recorded reason is refused.
  - **POLICY-5.b**  A strict profile that also switches a layer off is refused as a contradiction.
  - **POLICY-5.c**  A policy written for a newer Trust than the one I am running is refused rather than half-understood.
- **POLICY-6**  An override supplied at run time can only make the gate stronger.
  - **POLICY-6.a**  Anything that would drop the repository out of strict is refused.
- **POLICY-7**  A proposed change cannot weaken the policy that the branch it targets already committed.
  - **POLICY-7.a**  Switching off contracts, provenance, or the coverage map in a proposed change is refused.
  - **POLICY-7.b**  Lowering required contract coverage in a proposed change is refused.
  - **POLICY-7.c**  Editing the contents of the committed provenance policy in a proposed change is refused.
  - **POLICY-7.d**  Moving provenance from the proposed commits to the merge base is allowed only as part of turning enforcement on.
- **POLICY-8**  When the committed policy on the base cannot be read, the run fails rather than falling back to something more permissive.
- **POLICY-9**  A repository adopting the gate for the first time is not blocked by there being no policy on the base branch yet.
