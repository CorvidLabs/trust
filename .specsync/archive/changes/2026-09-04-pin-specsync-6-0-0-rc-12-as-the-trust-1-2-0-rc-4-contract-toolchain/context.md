---
change: pin-specsync-6-0-0-rc-12-as-the-trust-1-2-0-rc-4-contract-toolchain
artifact: context
---

# Context

Trust 1.2.0-rc.3 pins SpecSync 6.0.0-rc.11 (2026-09-01). SpecSync has since
published 6.0.0-rc.12 (2026-09-02); rc.12 is the newest tag and ships the
product cut that `check` is the product with SDD opt-in (spec-sync#748) and
the same-actor scoped-review fix (spec-sync#749). Consumer repositories will
move their local agents to rc.12, so Trust CI should speak the same SpecSync
as the tree it audits.

This change is the same coordinated pin flip as the rc.11 change: every
SpecSync pin moves to rc.12, and Trust becomes 1.2.0-rc.4. No gate, input, or
mirror rule changes. The rc.4 tag is a prerelease and cannot move the
protected `v1` channel.

Session instruction: pin SpecSync 6.0.0-rc.12 now and cut Trust 1.2.0-rc.4.
Trust 1.2.0-rc.3 is already an immutable tag on rc.11 and stays as it is.
Do not merge Trust#33 (Dependabot rewrite of the rc.11 tag object to its
peeled commit).
