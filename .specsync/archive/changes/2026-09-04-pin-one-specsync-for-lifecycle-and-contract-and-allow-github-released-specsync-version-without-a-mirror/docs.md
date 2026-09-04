---
change: pin-one-specsync-for-lifecycle-and-contract-and-allow-github-released-specsync-version-without-a-mirror
artifact: docs
---

# Docs

- README: consumers may set `specsync-version` to any exact GitHub-released
  SpecSync version without a mirror. The `file://` mirror remains for
  governed self-host artifacts.
- README: Trust installs that SpecSync before lifecycle so runner PATH
  cannot pick another binary.
