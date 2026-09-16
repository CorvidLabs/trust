---
hi: 1
families: [GATE]
---

# Running the gate

## Intent

The gate is one command that runs the same four checks, in the same order, that CI will run — so a surprise in CI is a bug, not a way of life. Order matters and is fixed: verification first, then contracts, then risk, then provenance, because an earlier failure must never be papered over by a later result. When it stops, it should be immediately clear which layer objected and what range of commits it was judging. A tool that crashes is a failure, never a shrug.

## Criteria

- **GATE-1**  One local command runs the same gate that CI will run.
- **GATE-2**  The layers run in a fixed order: verification, then contracts, then risk, then provenance.
  - **GATE-2.a**  A failure in an earlier layer stops the run before a later one can paper over it.
- **GATE-3**  The run says which commits it is judging before it starts.
- **GATE-4**  A layer that is switched off says so rather than passing quietly.
  - **GATE-4.a**  The reason recorded for switching that layer off is shown alongside it.
- **GATE-5**  A risk verdict at or above the configured threshold is a hard stop.
- **GATE-6**  The run ends with one line saying whether the gate passed.
  - **GATE-6.a**  A pass that only got there because provenance is still progressive says so rather than claiming a clean pass.
  - **GATE-6.b**  A failure names the layer that objected without my having to read back through the log.
- **GATE-7**  The comparison range comes from my upstream branch when I do not name one.
  - **GATE-7.a**  Trust asks me for a range instead of guessing when there is no upstream to compare with.
- **GATE-8**  Missing configuration for an enabled layer stops the run before any component tool is invoked.
- **GATE-9**  A component that crashes or returns something unreadable fails the gate rather than being excused as a soft degrade.
- **GATE-10**  I can ask for a stricter profile or threshold for a single run without editing the committed policy.
- **GATE-11**  Turning the coverage map on makes the local gate check it too.
- **GATE-12**  Trust finds the repository root itself, wherever inside the repository I happen to be standing.
