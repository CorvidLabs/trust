---
change: CHG-0004-document-trusted-specsync-self-host-inputs-in-the-provenance-contract
artifact: docs
---

# Docs

Add `inputs.specsync-version` and `inputs.specsync-download-base-url` to the
`trust-provenance` Public API table. Their descriptions must match the existing
action contract: normal consumers receive released SpecSync 5.0.1, while a
governed self-hosting workflow may provide only an authority-free runner-local
mirror URL. This change documents existing behavior and does not add or alter an
action input.
