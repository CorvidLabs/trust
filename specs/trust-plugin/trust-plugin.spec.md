---
module: trust-plugin
version: 11
status: stable
files:
  - bin/fledge-trust
  - plugin.toml
db_tables: []
depends_on: [trust-policy]
---

# Trust Fledge Plugin

## Purpose

The Trust plugin exposes the released Trust CLI through Fledge and delegates all
behavior to the Python implementation without changing arguments or exit codes.

## Public API

The plugin registers the public `trust` command and exposes adopt, status,
doctor, verify, and version reporting. Suppressed action-resolution and
lifecycle-execution subcommands are internal composite-action plumbing and are
not supported as public CLI interfaces.

## Invariants

1. The launcher resolves symlinks before locating the implementation.
2. Every argument and exit code is forwarded unchanged.
3. The plugin manifest version is the user-visible Trust version.
4. Tagged plugin installation exposes the fledge trust command.

## Behavioral Examples

```text
Given Trust 1.2.0 is installed as a tagged Fledge plugin
When fledge trust doctor runs
Then the launcher executes the bundled implementation
And returns its exact exit status
```

## Error Cases

| Error | Behavior |
| --- | --- |
| Missing Python | The launcher exits non-zero. |
| Missing implementation | The launcher fails without falling back to another checkout. |

## Dependencies

- Fledge plugin host
- Python 3

## Change Log

| Date | Change |
| --- | --- |
| 2026-07-12 | Stable Trust 1.0 plugin contract. |
| 2026-07-13 | Map CLI adoption, status, and version behavior to its implementation. |
| 2026-07-13 | CHG-0005-close-trust-1-0-1-contract-validation-and-canonical-quality-gaps: Close Trust 1.0.1 contract validation and canonical quality gaps |
| 2026-08-27 | pin-specsync-6-0-0-rc-9-as-the-trust-1-2-0-rc-1-contract-toolchain: Pin SpecSync 6.0.0-rc.9 as the Trust 1.2.0-rc.2 contract toolchain |
| 2026-09-01 | pin-specsync-6-0-0-rc-11-as-the-trust-1-2-0-rc-3-contract-toolchain: Pin SpecSync 6.0.0-rc.11 as the Trust 1.2.0-rc.3 contract toolchain |
| 2026-09-02 | pin-specsync-6-0-0-rc-12-as-the-trust-1-2-0-rc-4-contract-toolchain: Pin SpecSync 6.0.0-rc.12 as the Trust 1.2.0-rc.4 contract toolchain |
| 2026-09-02 | pin-specsync-6-0-0-rc-12-as-the-trust-1-2-0-rc-4-contract-toolchain: Pin SpecSync 6.0.0-rc.12 as the Trust 1.2.0-rc.4 contract toolchain |
| 2026-09-09 | pin-specsync-6-0-0-as-the-trust-1-2-0-contract-toolchain: Pin SpecSync 6.0.0 as the Trust 1.2.0 contract toolchain |
| 2026-09-09 | Release Trust 1.2.0 |

