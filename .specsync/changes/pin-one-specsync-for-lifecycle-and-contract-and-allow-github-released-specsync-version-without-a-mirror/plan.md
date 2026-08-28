---
change: pin-one-specsync-for-lifecycle-and-contract-and-allow-github-released-specsync-version-without-a-mirror
artifact: plan
---

# Plan

1. Relax the non-default SpecSync version mirror requirement.
2. Add `action-install-specsync` and run it before lifecycle.
3. Prepend the pinned binary to PATH for lifecycle and warn on PATH mismatch.
4. Cover resolver, local-mirror install, and action step order in tests.
5. Document the GitHub-release path in README and REQ-trust-action-010/011.
