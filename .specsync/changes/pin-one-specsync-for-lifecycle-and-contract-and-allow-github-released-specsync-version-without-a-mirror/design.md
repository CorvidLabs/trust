---
change: pin-one-specsync-for-lifecycle-and-contract-and-allow-github-released-specsync-version-without-a-mirror
artifact: design
---

# Design

- `action-install-specsync` downloads the resolved version the same way the
  nested SpecSync action does (archive + sidecar checksum) into
  `$RUNNER_TEMP/corvid-trust-specsync/bin/specsync`.
- That step runs after Fledge install and before lifecycle. It appends the
  bin directory to `GITHUB_PATH`.
- Lifecycle prepends that directory to `PATH` and warns if `command -v specsync`
  would have resolved to a different binary.
- `resolve_specsync_inputs` accepts any exact SemVer without a mirror. A
  `file://` mirror remains the self-host override and is still validated
  before lifecycle.
