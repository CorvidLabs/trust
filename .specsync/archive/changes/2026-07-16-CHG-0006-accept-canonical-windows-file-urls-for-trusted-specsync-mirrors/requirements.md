---
change: CHG-0006-accept-canonical-windows-file-urls-for-trusted-specsync-mirrors
artifact: requirements
---

# Requirements

- Canonical authority-free file URLs resolve to native absolute paths on
  Windows, Linux, and macOS.
- URL structure and encoding checks occur before native path conversion.
- Native paths remain existing directories strictly beneath resolved
  `RUNNER_TEMP`; root, sibling, missing, and symlink escapes remain rejected.
