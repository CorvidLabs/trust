---
change: CHG-0007-harden-trusted-specsync-mirror-validation-before-lifecycle-execution
artifact: research
---

# Research

`urllib.parse.urlsplit` raises `ValueError` for malformed bracketed IPv6 authorities. `Path.resolve(strict=True)` confines resolved targets but erases whether a path component was originally a symlink. Therefore URL parsing needs an explicit error boundary and mirror validation needs both a symlink check and a resolved-boundary check for each entry.

The immutable nested SpecSync action already owns released artifact download behavior. Trust only needs the local override for testing an unreleased exact version, so omitting the override is intentionally limited to the released default `5.0.1`.
