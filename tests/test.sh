#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TRUST="$ROOT/bin/fledge-trust"
TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT

fail() { echo "test failure: $*" >&2; exit 1; }
contains() { case "$1" in *"$2"*) ;; *) fail "expected output to contain: $2";; esac; }
assert_file() { [ -f "$1" ] || fail "expected file: $1"; }

make_repo() {
  local repo="$1"
  mkdir -p "$repo"
  git -C "$repo" init -q
  git -C "$repo" config user.email test@example.com
  git -C "$repo" config user.name Test
}

repo="$TMP/repo with spaces"
make_repo "$repo"
repo="$(cd "$repo" && pwd -P)"
cat > "$repo/fledge.toml" <<'EOF'
[tasks]
test = "true"

[lanes.verify]
steps = ["test"]
EOF
expected_fledge="$(cat "$repo/fledge.toml")"

dry_output="$(cd "$repo" && "$TRUST" adopt --dry-run)"
contains "$dry_output" "dry run complete"
[ ! -f "$repo/.trust.toml" ] || fail "dry run wrote files"

adopt_output="$(cd "$repo" && "$TRUST" adopt)"
contains "$adopt_output" "trust adoption complete"
for file in .trust.toml .specsync/config.toml .augur.toml .attest.json .atlasignore .github/workflows/trust.yml AGENTS.md; do
  assert_file "$repo/$file"
done
[ "$(cat "$repo/fledge.toml")" = "$expected_fledge" ] || fail "adopt replaced fledge.toml"

mkdir -p "$repo/nested/package"
(cd "$repo/nested/package" && "$TRUST" adopt >/dev/null)
[ "$(grep -c 'CorvidLabs trust toolchain: BEGIN' "$repo/AGENTS.md")" = 1 ] || fail "managed block duplicated"

isolated_bin="$TMP/isolated-bin"
mkdir -p "$isolated_bin"
ln -s "$(command -v python3)" "$isolated_bin/python3"
status_code=0
status_json="$(cd "$repo" && PATH="$isolated_bin:/usr/bin:/bin" "$TRUST" status --json)" || status_code=$?
[ "$status_code" -ne 0 ] || fail "status with missing tools returned success"
STATUS_JSON="$status_json" python3 -c 'import json, os; json.loads(os.environ["STATUS_JSON"])'
contains "$status_json" '"schemaVersion": 1'
contains "$status_json" '"healthy": false'

skip_repo="$TMP/skip"
make_repo "$skip_repo"
cp "$repo/fledge.toml" "$skip_repo/fledge.toml"
(cd "$skip_repo" && "$TRUST" adopt --no-specs "content only" --no-attest "CI only" --no-atlas "Pages disabled" >/dev/null)
grep -Fq 'skip_reason = "content only"' "$skip_repo/.trust.toml" || fail "spec skip reason was not recorded"
grep -Fq 'skip_reason = "CI only"' "$skip_repo/.trust.toml" || fail "attest skip reason was not recorded"
[ ! -e "$skip_repo/.specsync/config.toml" ] || fail "disabled specs were installed"

fresh="$TMP/fresh-python"
make_repo "$fresh"
touch "$fresh/pyproject.toml"
(cd "$fresh" && "$TRUST" adopt >/dev/null)
grep -Fq '[lanes.verify]' "$fresh/fledge.toml" || fail "fresh detected repo has no verify lane"

unknown="$TMP/unknown"
make_repo "$unknown"
if (cd "$unknown" && "$TRUST" adopt >/dev/null 2>&1); then fail "unknown stack adoption succeeded"; fi
[ ! -e "$unknown/.trust.toml" ] || fail "failed adoption wrote files"

malformed="$TMP/malformed"
make_repo "$malformed"
cp "$repo/fledge.toml" "$malformed/fledge.toml"
printf '%s\n' '<!-- CorvidLabs trust toolchain: BEGIN (managed, do not edit inside) -->' > "$malformed/AGENTS.md"
if (cd "$malformed" && "$TRUST" adopt >/dev/null 2>&1); then fail "malformed AGENTS markers succeeded"; fi
[ ! -e "$malformed/.trust.toml" ] || fail "malformed marker failure was not atomic"

fake="$TMP/bin"
log="$TMP/commands.log"
mkdir -p "$fake"
for command in fledge specsync augur attest; do
  printf '#!/usr/bin/env bash\necho "%s $*" >> "%s"\n' "$command" "$log" > "$fake/$command"
  chmod +x "$fake/$command"
done
verify_output="$(cd "$repo" && PATH="$fake:$PATH" "$TRUST" verify --range main..HEAD)"
contains "$verify_output" "progressive provenance"
expected="$(printf 'fledge lanes run verify\nspecsync check\naugur gate --range main..HEAD --threshold block\nattest verify --range main..HEAD --policy %s/.attest.json' "$repo")"
actual="$(cat "$log")"
[ "$actual" = "$expected" ] || { printf 'expected:\n%s\nactual:\n%s\n' "$expected" "$actual" >&2; fail "verification order or arguments differ"; }

strict_repo="$TMP/strict"
cp -R "$repo" "$strict_repo"
sed -i.bak 's/profile = "standard"/profile = "strict"/' "$strict_repo/.trust.toml"
rm -f "$strict_repo/.trust.toml.bak"
if (cd "$strict_repo" && PATH="$fake:$PATH" "$TRUST" verify --range main..HEAD >/dev/null 2>&1); then
  fail "strict provenance without origin succeeded"
fi

doctor_repo="$TMP/doctor"
cp -R "$repo" "$doctor_repo"
rm "$doctor_repo/.attest.json"
if (cd "$doctor_repo" && "$TRUST" doctor --json >/dev/null); then fail "unhealthy JSON doctor returned success"; fi

echo "trust tests passed"
