---
change: pin-one-specsync-for-lifecycle-and-contract-and-allow-github-released-specsync-version-without-a-mirror
artifact: research
---

# Research

- The nested SpecSync action already downloads `specsync-{os}-{arch}.tar.gz`
  plus an adjacent SHA-256 sidecar from GitHub releases or a `file://` mirror.
  Lifecycle never ran that installer.
- `GITHUB_PATH` only affects later steps, so SpecSync must be installed in a
  step before lifecycle, then prepended again in the lifecycle process.
- SpecSync 6 publishes no Windows asset; the nested action already fails
  closed on Windows. Lifecycle install must do the same.
- The mirror requirement on non-default versions blocked GitHub-released
  binaries that the contract step can already checksum. Keep mirrors for
  self-host; allow any exact SemVer from GitHub releases.
