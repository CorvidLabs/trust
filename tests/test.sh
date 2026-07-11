#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TRUST="$ROOT/bin/fledge-trust"
TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT

assert_contains() {
  local haystack="$1" needle="$2"
  case "$haystack" in
    *"$needle"*) ;;
    *) echo "expected output to contain: $needle" >&2; exit 1 ;;
  esac
}

assert_file() {
  [ -f "$1" ] || { echo "expected file: $1" >&2; exit 1; }
}

repo="$TMP/repo"
mkdir -p "$repo"
git -C "$repo" init -q
expected_fledge="$(printf '[tasks]\ntest = "true"\n\n[lanes.verify]\nsteps = ["test"]')"
printf '%s\n' "$expected_fledge" > "$repo/fledge.toml"

help_output="$($TRUST --help)"
assert_contains "$help_output" "fledge trust"

dry_output="$(cd "$repo" && "$TRUST" adopt --dry-run)"
assert_contains "$dry_output" "dry run complete"
[ ! -f "$repo/.attest.json" ] || { echo "dry run wrote files" >&2; exit 1; }

adopt_output="$(cd "$repo" && "$TRUST" adopt)"
assert_contains "$adopt_output" "trust adoption complete"
assert_file "$repo/fledge.toml"
assert_file "$repo/.specsync/config.toml"
assert_file "$repo/.augur.toml"
assert_file "$repo/.attest.json"
assert_file "$repo/.atlasignore"
assert_file "$repo/.github/workflows/trust.yml"
assert_file "$repo/AGENTS.md"
[ "$(cat "$repo/fledge.toml")" = "$expected_fledge" ] || { echo "adopt replaced fledge.toml" >&2; exit 1; }

second_output="$(cd "$repo" && "$TRUST" adopt)"
assert_contains "$second_output" "already exists"

status_json="$(cd "$repo" && "$TRUST" status --json)"
STATUS_JSON="$status_json" python3 -c 'import json, os; json.loads(os.environ["STATUS_JSON"])'
assert_contains "$status_json" '"workflow": true'
assert_contains "$status_json" '"rules": true'

fake="$TMP/bin"
log="$TMP/commands.log"
mkdir -p "$fake"
for command in fledge specsync augur attest; do
  printf '#!/usr/bin/env bash\necho "%s $*" >> "%s"\n' "$command" "$log" > "$fake/$command"
  chmod +x "$fake/$command"
done

verify_output="$(cd "$repo" && PATH="$fake:$PATH" "$TRUST" verify --range main..HEAD)"
assert_contains "$verify_output" "trust gate passed"
expected="$(printf 'fledge lanes run verify\nspecsync check\naugur gate --range main..HEAD --threshold block\nattest verify --range main..HEAD --policy .attest.json')"
actual="$(cat "$log")"
[ "$actual" = "$expected" ] || { printf 'unexpected command order:\n%s\n' "$actual" >&2; exit 1; }

echo "trust tests passed"
