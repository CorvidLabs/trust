---
change: CHG-0003-add-trusted-specsync-self-host-artifact-inputs
artifact: testing
---

# Testing

- Verify defaults resolve to version 5.0.1 and an empty mirror.
- Verify a real directory beneath `RUNNER_TEMP` resolves to a canonical authority-free file URL.
- Reject HTTPS, remote file authority, relative paths, missing paths, direct `RUNNER_TEMP`, sibling paths, plain and percent-encoded traversal, query/fragment data, and symlink escape.
- Assert action.yml passes resolver outputs to the pinned nested SpecSync action.
- Run shell tests, Python compilation, manifest validation, strict SpecSync, and Trust verification.
