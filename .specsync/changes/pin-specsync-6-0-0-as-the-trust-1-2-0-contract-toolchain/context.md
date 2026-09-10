---
change: pin-specsync-6-0-0-as-the-trust-1-2-0-contract-toolchain
artifact: context
---

# Context

Trust 1.2.0-rc.4 pins SpecSync 6.0.0-rc.12 (2026-09-02). SpecSync 6.0.0 is
now a stable GitHub release (2026-09-09) at annotated tag object
`3c2ed4972c8c53ae02ab5dd5775beccd6da3eeb8` (peeled commit
`b9ff32310181b796cc617406ff9298c533ebeb15`), with linux and macOS archives
plus SHA-256 sidecars. crates.io also publishes `specsync 6.0.0`.

Consumer repositories are moving to SpecSync 6.0.0, so Trust CI must speak
the same SpecSync as the tree it audits. This change is the same coordinated
pin flip as the rc.12 change: every SpecSync pin moves to 6.0.0. No gate,
input, or mirror rule changes.

`plugin.toml` stays `1.2.0-rc.4`. After this pin merges to `main` and hosted
checks pass, `fledge release 1.2.0 --pre-lane release --push --non-interactive`
bumps the plugin, tags `v1.2.0`, and is eligible to promote the protected
`v1` channel. Do not retag `v1.2.0-rc.4`. Do not touch the spec-sync git
repository.

CHG-0003 remains verifying on main with a v1 workflow and a REQ-trust-action-010
ADD conflict; this change MODIFIES that living requirement and does not
archive or adopt CHG-0003.
