---
change: CHG-0007-harden-trusted-specsync-mirror-validation-before-lifecycle-execution
artifact: context
---

# Context

Trust accepts a local SpecSync mirror only for governed self-hosting validation. Review found three gaps in the resolver: malformed authority syntax could escape as a raw `ValueError`, an exact non-default version could use the released download channel without a reviewed local mirror, and files inside an otherwise confined mirror were not inspected for symlinks or boundary escape.

The correction must fail before lifecycle execution while preserving exact SemVer validation, canonical local file URLs, Windows path conversion, and the existing `RUNNER_TEMP` boundary.
