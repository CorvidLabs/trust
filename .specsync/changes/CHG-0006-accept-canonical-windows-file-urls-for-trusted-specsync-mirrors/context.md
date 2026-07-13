---
change: CHG-0006-accept-canonical-windows-file-urls-for-trusted-specsync-mirrors
artifact: context
---

# Context

Trust PR #12 passed every Linux and macOS Action case but failed the Windows
plugin matrix on its first valid mirror. `Path.as_uri()` emits
`file:///D:/...`; URL parsing returns `/D:/...`, which `WindowsPath` correctly
treats as rooted without a drive and therefore not absolute. The URL must be
converted to an operating-system-native filename before applying the existing
filesystem security boundary.
