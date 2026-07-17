---
change: CHG-0006-accept-canonical-windows-file-urls-for-trusted-specsync-mirrors
artifact: design
---

# Design

Replace direct percent decoding with `url2pathname(parsed.path)`. Keep every
pre-conversion structural and encoding check unchanged, then construct `Path`
from the native result and retain absolute/traversal, strict resolution,
directory, child-boundary, and symlink checks. Return `mirror.as_uri()` so the
nested Action still receives a canonical file URL.
