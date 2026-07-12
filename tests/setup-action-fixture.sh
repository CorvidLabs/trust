#!/usr/bin/env bash
set -euo pipefail

root="$1"
rm -rf "$root"
mkdir -p "$root/src" "$root/specs/example" "$root/.specsync"
git -C "$root" init -q
git -C "$root" config user.email test@example.com
git -C "$root" config user.name "Trust CI"

cat > "$root/fledge.toml" <<'EOF'
[tasks]
test = "python3 -m py_compile src/example.py"

[lanes.verify]
steps = ["test"]
EOF

cat > "$root/.trust.toml" <<'EOF'
schema_version = 1
profile = "standard"

[lifecycle]
command = ["fledge", "lanes", "run", "verify"]

[contract]
enabled = true
require_coverage = 100
skip_reason = ""

[risk]
threshold = "block"

[provenance]
mode = "soft"
scope = "changes"
policy = ".attest.json"
skip_reason = ""

[atlas]
enabled = false
skip_reason = "fixture does not publish Pages"
EOF

cat > "$root/.attest.json" <<'EOF'
{"requireAttestation": true, "requireTestsPassed": true}
EOF

cat > "$root/.augur.toml" <<'EOF'
[thresholds]
review = 35
block = 65
EOF

cat > "$root/.specsync/config.toml" <<'EOF'
specs_dir = "specs"
source_dirs = ["src"]
exclude_dirs = []
required_sections = ["Purpose", "Public API", "Invariants", "Behavioral Examples", "Error Cases", "Dependencies", "Change Log"]
enforcement = "strict"
EOF

cat > "$root/src/example.py" <<'EOF'
def greet(name: str) -> str:
    return f"hello {name}"
EOF

cat > "$root/specs/example/example.spec.md" <<'EOF'
---
module: example
version: 1
status: active
files:
  - src/example.py
db_tables: []
depends_on: []
---

# Example

## Purpose
Provide a deterministic fixture API.

## Public API
| Export | Description |
| --- | --- |
| `greet` | Return a greeting for a name. |

## Invariants
1. Output includes the supplied name.

## Behavioral Examples
Given `Ada`, `greet` returns `hello Ada`.

## Error Cases
There are no expected errors for string input.

## Dependencies
No external dependencies.

## Change Log
| Version | Changes |
| --- | --- |
| 1 | Initial fixture. |
EOF

cat > "$root/specs/example/requirements.md" <<'EOF'
---
spec: example.spec.md
---

## User Stories

- As a consumer, I want a deterministic greeting so the Trust fixture can verify an exported API.

## Acceptance Criteria

- `greet` returns a string containing the supplied name.
- The lifecycle verification command compiles the source file.

## Constraints

- The fixture has no external runtime dependencies.

## Out of Scope

- Input validation beyond the string type annotation.
EOF

git -C "$root" add .
git -C "$root" commit -qm initial
printf '\n# second commit\n' >> "$root/src/example.py"
git -C "$root" add src/example.py
git -C "$root" commit -qm change
