---
hi: 1
families: [CHECKUP]
---

# Is this repository wired up?

## Intent

Before running the gate, I want to know whether this repository could even pass it: which tools are missing, which configuration is absent, which managed files never landed. Looking should be free and never stop me, while asking whether things are actually healthy should produce an answer a script can act on. The report tells me everything that is wrong at once, not the first thing, and can be read by a program as easily as by a person.

## Criteria

- **CHECKUP-1**  One command tells me whether this repository is properly wired for the gate.
  - **CHECKUP-1.a**  Looking never stops me, however unhealthy the repository turns out to be.
- **CHECKUP-2**  A second command fails when something is missing, so a script can depend on it.
- **CHECKUP-3**  The report names every tool the committed policy needs and says whether it is installed.
- **CHECKUP-4**  The report tells me whether everything adoption should have left behind is still in place.
  - **CHECKUP-4.a**  A missing CI workflow shows up in the report.
  - **CHECKUP-4.b**  Missing managed agent rules show up in the report.
  - **CHECKUP-4.c**  An enabled layer with no configuration shows up in the report.
- **CHECKUP-5**  The report lists every problem it found, not only the first one.
- **CHECKUP-6**  I can get the report as JSON so another program can read it.
  - **CHECKUP-6.a**  The JSON says which version of its own shape it follows.
  - **CHECKUP-6.b**  The JSON names the installed Trust version.
  - **CHECKUP-6.c**  The JSON names the profile the repository is running under.
- **CHECKUP-7**  A policy file Trust cannot parse is reported as an unhealthy repository rather than crashing the command.
- **CHECKUP-8**  Each problem in the report comes with what to do about it.
