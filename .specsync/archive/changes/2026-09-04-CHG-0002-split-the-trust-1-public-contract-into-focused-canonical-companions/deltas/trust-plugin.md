## MODIFIED

### REQUIREMENT REQ-trust-plugin-001

The plugin SHALL expose Trust through the Fledge command registry.

Acceptance Criteria

- A fresh tagged installation makes fledge trust available.

### REQUIREMENT REQ-trust-plugin-002

The launcher SHALL forward arguments and exit status without reinterpretation.

Acceptance Criteria

- Plugin behavior tests cover success, invalid input, and missing dependency paths.

### REQUIREMENT REQ-trust-plugin-003

Adoption dry-run SHALL report planned changes and write nothing.

Acceptance Criteria

- A dry-run leaves the governed worktree byte-for-byte unchanged.

### REQUIREMENT REQ-trust-plugin-004

Repeated adoption SHALL be idempotent.

Acceptance Criteria

- A second adoption reports no additional managed changes.

### REQUIREMENT REQ-trust-plugin-005

Adoption SHALL preserve existing files unless `--force` is passed.

Acceptance Criteria

- Unmanaged content is never overwritten implicitly.

### REQUIREMENT REQ-trust-plugin-006

The managed AGENTS block SHALL be present exactly once.

Acceptance Criteria

- Adoption updates its owned block without duplicating surrounding instructions.

### REQUIREMENT REQ-trust-plugin-007

CLI and status output SHALL report the plugin manifest version.

Acceptance Criteria

- Installed-version diagnostics agree with `plugin.toml`.
