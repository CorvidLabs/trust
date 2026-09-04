---
change: pin-specsync-6-0-0-rc-11-as-the-trust-1-2-0-rc-3-contract-toolchain
artifact: context
---

# Context

Trust 1.2.0-rc.2 pins SpecSync 6.0.0-rc.9 (2026-08-27). SpecSync has since
published 6.0.0-rc.10 and 6.0.0-rc.11 (2026-08-29); rc.11 is the newest tag and
carries the line-ending hash fix (spec-sync#737) that the rc.9 pin recorded as a
known follow-up. Consumer repositories are moving their local agents to rc.11,
so Trust CI should speak the same SpecSync as the tree it audits.

This change is the same coordinated pin flip as the rc.9 change: every SpecSync
pin moves to rc.11, and Trust becomes 1.2.0-rc.3. No gate, input, or mirror
rule changes. The rc.3 tag is a prerelease and cannot move the protected `v1`
channel.

Session instruction: pin SpecSync 6.0.0-rc.11 now and cut Trust 1.2.0-rc.3.
Trust 1.2.0-rc.2 is already an immutable tag on rc.9 and stays as it is.
