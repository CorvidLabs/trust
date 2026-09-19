# trust

Trust is for a maintainer who wants their repository properly gated without spending a week wiring five tools together, and for everyone who works in that repository afterwards. Adopting it should feel like one small decision you can see in full before you make it: nothing you wrote yourself is touched, and running it twice does nothing. Running the gate should feel identical on a laptop and in CI, and when it objects it should be obvious which layer objected and why. Above all the gate should only ever get stronger by accident — a proposed change can tighten it, but no input, override, or edit can loosen what the branch already committed.

## Features

<!-- hi:index -->
- [adopt](hi/adopt.md): ADOPT (21 criteria)
- [checkup](hi/checkup.md): CHECKUP (15 criteria)
- [ci](hi/ci.md): CI (17 criteria)
- [gate](hi/gate.md): GATE (17 criteria)
- [policy](hi/policy.md): POLICY (19 criteria)
- [provenance](hi/provenance.md): PROVENANCE (17 criteria)
- [release](hi/release.md): RELEASE (18 criteria)
- [tools](hi/tools.md): TOOLS (19 criteria)
<!-- /hi:index -->
