---
change: pin-one-specsync-for-lifecycle-and-contract-and-allow-github-released-specsync-version-without-a-mirror
artifact: testing
---

# Testing

- `tests/test.sh` accepts exact SemVer SpecSync versions with an empty
  download URL, including former default `5.2.0` and `5.0.1`.
- A local `file://` mirror tarball installs to
  `$RUNNER_TEMP/corvid-trust-specsync/bin/specsync` and checksum-mismatch
  still fails.
- `action.yml` runs `action-install-specsync` after Fledge and before
  lifecycle, and lifecycle receives `SPECSYNC_PINNED_BIN`.
- Evidence for REQ-trust-action-010 and REQ-trust-action-011 is `tests/test.sh`.
