---
change: CHG-0006-accept-canonical-windows-file-urls-for-trusted-specsync-mirrors
artifact: testing
---

# Testing

- Reuse the existing cross-platform mirror matrix, which generates its valid
  URL with `Path.as_uri()` and exercises a path containing spaces.
- Preserve negative cases for malformed SemVer, authorities, queries,
  fragments, incomplete escapes, encoded separators and controls, traversal,
  root, sibling, missing path, and symlink escape.
- Run the full Trust release lane locally and require the hosted Windows plugin
  behavior job to pass before merge.
