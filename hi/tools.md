---
hi: 1
families: [TOOLS]
---

# Getting the toolchain, pinned

## Intent

Trust is worth nothing if the tools it composes drift underneath it, so every version it runs is one it was proven against, and everything it downloads is checked against a recorded digest before it is allowed to run. Installing should be one step that leaves the command on your path with no shim inside your repository. On a runner, Trust decides which contract tool is used — not whatever happens to be on PATH already. The one deliberate escape hatch is for a team releasing the contract tool itself, and it is narrow on purpose: a locally built copy, confined to the runner, re-checked right before it is used.

## Criteria

- **TOOLS-1**  One install brings the whole toolchain: Trust and the four tools it composes.
  - **TOOLS-1.a**  After installing, the trust command is discoverable with no shim inside my repository.
- **TOOLS-2**  Trust reports the version that is actually installed, not one from a checkout that happens to be nearby.
- **TOOLS-3**  Running Trust through fledge passes my arguments through untouched.
  - **TOOLS-3.a**  The exit status I get back is the gate's own, never one the wrapper invented.
- **TOOLS-4**  CI installs exactly the component versions this release of Trust was proven against.
  - **TOOLS-4.a**  Every downloaded tool is checked against a recorded digest before it is allowed to run.
  - **TOOLS-4.b**  Every composed action is pinned to an exact reviewed commit rather than a moving tag.
  - **TOOLS-4.c**  A tool that will not install fails the run rather than being reported as a policy problem.
- **TOOLS-5**  The contract tool is installed before verification runs, so verification and the contract layer use the same one.
  - **TOOLS-5.a**  A different copy already on the runner's path is ignored.
  - **TOOLS-5.b**  The run says plainly which copy of the contract tool it used.
- **TOOLS-6**  A team releasing the contract tool itself can point Trust at a locally built copy without loosening anything else.
  - **TOOLS-6.a**  A version is accepted only as an exact semantic version.
  - **TOOLS-6.b**  A local copy must be a plain path on the runner, never somewhere on the network.
  - **TOOLS-6.c**  A local copy must sit inside the runner's temporary directory.
  - **TOOLS-6.d**  Everything that copy leads to must stay inside that same directory.
  - **TOOLS-6.e**  Paths that climb out, hide encoded separators, or lead through symlinks are refused.
  - **TOOLS-6.f**  The local copy is checked again immediately before the contract layer consumes it.
