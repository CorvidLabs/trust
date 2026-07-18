---
change: CHG-0009-adopt-specsync-5-1-1-as-the-pinned-contract-toolchain
artifact: context
---

# Context

Trust pins each composed component to the latest release within its declared
major line. Fledge 1.7.0, Attest 1.0.0, Augur 1.0.0, and Atlas 1.3.1 are
already the latest releases in their majors; SpecSync is the only component
behind, pinned at 5.0.1 while 5.1.1 is the latest 5.x release.

SpecSync 5.1.x hardens the verified lifecycle this repository relies on:
native `change reopen`, reacceptance that records closing approval without
replaying already-canonical deltas, and hardened reopening evidence
(`stale_acceptance_input_digest` / `current_acceptance_input_digest`). The
5.0.1-era change ledgers cannot be parsed by 5.1.1 until those fields are
backfilled; that additive migration landed in `cccb7d2` and validates under
both binaries. The reusable migration script ships in this change so
consuming projects can migrate their own ledgers.

The upgrade is released as Trust 1.1.0 (minor): it changes the public
`specsync-version` input default, so consumer-facing behavior moves while
remaining compatible with the existing input surface.
