---
change: CHG-0006-accept-canonical-windows-file-urls-for-trusted-specsync-mirrors
artifact: tasks
---

# Tasks

- [x] Inspect the hosted Windows failure and reproduce the URI/native-path mismatch.
- [x] Confirm standard-library `url2pathname` preserves POSIX behavior and restores Windows drive semantics.
- [x] Audit the ordering of URL and filesystem security checks.
