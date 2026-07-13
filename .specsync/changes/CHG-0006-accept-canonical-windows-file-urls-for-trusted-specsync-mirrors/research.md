---
change: CHG-0006-accept-canonical-windows-file-urls-for-trusted-specsync-mirrors
artifact: research
---

# Research

`urllib.request.url2pathname` is the standard-library platform adapter for a URL
path. On Windows it converts `/D:/...` into a drive-qualified native path; on
POSIX it performs the same percent decoding required for spaces. Authority,
query, fragment, encoded separator, and malformed escape rejection remains in
Trust before this conversion.
