## MODIFIED

### REQUIREMENT REQ-trust-policy-007

The Trust CLI SHALL emit versioned, valid configuration-health JSON.

Acceptance Criteria

- Consumers can parse overall readiness, tool availability, managed-file state, profile, and errors without scraping logs.
- Composite Action outputs remain the public source for lifecycle, contract, risk, and provenance gate results.
- Internal Action resolution emits canonical component settings without being presented as a public CLI command.

### SPEC SECTION Public API

The policy surface provides adoption, status, doctor, local verification, and
internal composite-action resolution. It accepts a committed policy path,
optional explicit range, and only stricter profile or risk overrides. Machine
status is schema-versioned configuration health; composite Action outputs expose
gate component results.

### SPEC SECTION Change Log

| Date | Change |
| --- | --- |
| 2026-07-12 | Stable Trust 1.0 policy contract. |
| 2026-07-13 | Map committed policies, generated defaults, managed rules, and status JSON to policy resolution. |
