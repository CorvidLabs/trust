---
change: pin-specsync-6-0-0-rc-9-as-the-trust-1-2-0-rc-1-contract-toolchain
artifact: context
---

# Context

Trust 1.1.2 still defaults the composed SpecSync contract to 5.2.0. CorvidLabs
consumers are mostly still on Trust 1.0.0, which installs SpecSync 5.0.1. Local
agent work already uses SpecSync 6, which mints slug-only change identities
without a `CHG-NNNN` ordinal.

That skew is what is failing Trust CI: product tests pass, then the contract
step rejects a 6.x change ID, and Augur is skipped. SpecSync 5 also fails
`specsync check` on stale accepted-change bookkeeping. SpecSync 6 severs that
gate — `check` reports lifecycle state and exits on spec validation only.

This change pins Trust 1.2.0-rc.1 to SpecSync 6.0.0-rc.9 so CI speaks the same
language as local SpecSync 6. The RC is ineligible for the protected `v1`
channel. Line-ending hash fix spec-sync#737 is on spec-sync main and is not in
rc.9; that is a known follow-up, not a blocker for this pin.
