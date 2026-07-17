## MODIFIED

### SPEC SECTION Public API

The plugin registers the public `trust` command and exposes adopt, status,
doctor, verify, and version reporting. Suppressed action-resolution and
lifecycle-execution subcommands are internal composite-action plumbing and are
not supported as public CLI interfaces.

### SPEC SECTION Change Log

| Date | Change |
| --- | --- |
| 2026-07-12 | Stable Trust 1.0 plugin contract. |
| 2026-07-13 | Map CLI adoption, status, and version behavior to its implementation. |
