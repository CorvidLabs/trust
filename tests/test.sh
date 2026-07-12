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

plugin_version="$(python3 - "$ROOT/plugin.toml" <<'PY'
import sys

try:
    import tomllib
except ImportError:
    import tomli as tomllib

with open(sys.argv[1], "rb") as stream:
    print(tomllib.load(stream)["plugin"]["version"])
PY
)"
[ "$("$TRUST" --version)" = "fledge trust $plugin_version" ] || fail "version output does not match plugin manifest"

component_source="$TMP/component-source"
component_bin="$TMP/component-bin"
component_path="$TMP/github-path"
mkdir -p "$component_source"
printf '#!/usr/bin/env bash\nprintf '\''augur-suffixed\\n'\''\n' > "$component_source/augur-linux-x86_64"
printf '#!/usr/bin/env bash\nprintf '\''attest-suffixed\\n'\''\n' > "$component_source/attest-linux-x86_64"
chmod +x "$component_source/augur-linux-x86_64" "$component_source/attest-linux-x86_64"
(
  cd "$component_source"
  GITHUB_PATH="$component_path" \
  COMPONENT_BIN="$component_bin" \
  AUGUR="augur-linux-x86_64" \
  ATTEST="attest-linux-x86_64" \
    bash "$ROOT/scripts/expose_component_binaries.sh"
)
[ "$(cat "$component_path")" = "$component_bin" ] || fail "component bin was not added to GITHUB_PATH"
[ "$("$component_bin/augur")" = "augur-suffixed" ] || fail "augur command link was not exposed"
[ "$("$component_bin/attest")" = "attest-suffixed" ] || fail "attest command link was not exposed"

python3 - "$ROOT" "$TMP" <<'PY'
import importlib.util
import json
from pathlib import Path
import sys

root = Path(sys.argv[1])
temporary = Path(sys.argv[2])
spec = importlib.util.spec_from_file_location(
    "normalize_specsync_cache",
    root / "scripts" / "normalize_specsync_cache.py",
)
if spec is None or spec.loader is None:
    raise RuntimeError("could not load normalize_specsync_cache")
normalizer = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = normalizer
spec.loader.exec_module(normalizer)

cache = temporary / "hashes.json"
cache.write_text('{"hashes":{"z":"2","a":"1"}}', encoding="utf-8")
normalizer.normalize(cache)
if cache.read_text(encoding="utf-8") != '{\n  "hashes": {\n    "a": "1",\n    "z": "2"\n  }\n}\n':
    raise AssertionError("spec-sync cache was not sorted with a trailing newline")

invalid_cases = [
    (temporary / "missing.json", "cannot read spec-sync cache"),
    (temporary / "corrupt.json", "cannot read spec-sync cache"),
    (temporary / "array.json", "root must be an object"),
    (temporary / "invalid-map.json", "hashes must be a string map"),
]
(temporary / "corrupt.json").write_text("{", encoding="utf-8")
(temporary / "array.json").write_text("[]", encoding="utf-8")
(temporary / "invalid-map.json").write_text(json.dumps({"hashes": {"path": 1}}), encoding="utf-8")
for path, expected in invalid_cases:
    try:
        normalizer.normalize(path)
    except SystemExit as error:
        if expected not in str(error):
            raise AssertionError(f"unexpected cache error for {path}: {error}") from error
    else:
        raise AssertionError(f"invalid cache was accepted: {path}")
PY

python3 - "$ROOT" <<'PY'
import importlib.util
from pathlib import Path
import subprocess
import sys
from unittest.mock import patch

root = Path(sys.argv[1])
spec = importlib.util.spec_from_file_location("trust_cli", root / "scripts" / "trust_cli.py")
if spec is None or spec.loader is None:
    raise RuntimeError("could not load trust_cli")
trust_cli = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = trust_cli
spec.loader.exec_module(trust_cli)
completed = subprocess.CompletedProcess(["tool"], 0)
with (
    patch.object(trust_cli.os, "name", "nt"),
    patch.object(trust_cli.shutil, "which", return_value="/usr/bin/bash"),
    patch.object(trust_cli.subprocess, "run", side_effect=[FileNotFoundError(), completed]) as run,
):
    result = trust_cli.run(["tool", "arg with spaces"], cwd=root)
if result is not completed:
    raise AssertionError("Windows Bash fallback did not return the command result")
fallback = run.call_args_list[1].args[0]
if fallback != ["/usr/bin/bash", "-c", 'exec "$@"', "trust", "tool", "arg with spaces"]:
    raise AssertionError(f"unexpected Windows Bash fallback: {fallback}")
PY

python3 - "$ROOT" <<'PY'
import importlib.util
from pathlib import Path
import sys

root = Path(sys.argv[1])
spec = importlib.util.spec_from_file_location("release_channel", root / "scripts" / "release_channel.py")
if spec is None or spec.loader is None:
    raise RuntimeError("could not load release_channel")
release_channel = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = release_channel
spec.loader.exec_module(release_channel)

cases = [
    ("v0.1.0", ["v0.1.0", "v0.2.0"], False, "v0"),
    ("v0.3.0-rc.1", ["v0.2.0", "v0.3.0-rc.1"], True, "v0"),
    ("v0.3.0", ["v0.3.0-rc.1", "v0.3.0"], True, "v0"),
    ("v1.0.0-rc.1", ["v1.0.0-rc.1"], False, "v1"),
    ("v1.0.0", ["v1.0.0", "v1.1.0-rc.1"], True, "v1"),
    ("v1.0.0", ["v1.0.0", "v1.1.0"], False, "v1"),
]
for target, tags, expected, major in cases:
    result = release_channel.decision(target, tags)
    if result["promote"] is not expected or result["major"] != major:
        raise AssertionError(f"unexpected release-channel decision for {target}: {result}")
try:
    release_channel.decision("not-a-version", [])
except ValueError:
    pass
else:
    raise AssertionError("invalid release tag was accepted")
try:
    release_channel.decision("v1.0.0+rebuilt", [])
except ValueError:
    pass
else:
    raise AssertionError("ambiguous build-metadata release tag was accepted")
for invalid in ("v01.0.0", "v1.0.0-01", "v1.0.0-rc..1"):
    try:
        release_channel.decision(invalid, [])
    except ValueError:
        continue
    raise AssertionError(f"invalid semantic release tag was accepted: {invalid}")
PY

python3 - "$ROOT" "$TMP" <<'PY'
import importlib.util
import os
from pathlib import Path
import shutil
import subprocess
import sys

root = Path(sys.argv[1])
temporary = Path(sys.argv[2])
scripts = root / "scripts"
sys.path.insert(0, str(scripts))
spec = importlib.util.spec_from_file_location("render_homebrew_formula", scripts / "render_homebrew_formula.py")
if spec is None or spec.loader is None:
    raise RuntimeError("could not load render_homebrew_formula")
renderer = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = renderer
spec.loader.exec_module(renderer)

digest = "a" * 64
formula = renderer.render("0.2.0", digest, "5.0.1")
for expected in ('version "0.2.0"', f'sha256 "{digest}"', 'assert_match "5.0.1"'):
    if expected not in formula:
        raise AssertionError(f"rendered formula is missing: {expected}")
if "@TRUST_" in formula or "@SPECSYNC_" in formula:
    raise AssertionError("rendered formula retained a placeholder")
formula_path = temporary / "corvid-trust.rb"
formula_path.write_text(formula, encoding="utf-8")
if shutil.which("ruby") is not None:
    subprocess.run(["ruby", "-c", str(formula_path)], check=True, capture_output=True, text=True)
if shutil.which("brew") is not None:
    cops = ",".join(
        (
            "FormulaAudit/ComponentsOrder",
            "FormulaAudit/DependencyOrder",
            "Homebrew/FormulaPathMethods",
            "Layout/ArgumentAlignment",
        )
    )
    homebrew_cache = temporary / "homebrew-cache"
    homebrew_cache.mkdir(exist_ok=True)
    environment = dict(os.environ)
    environment.update({"HOMEBREW_CACHE": str(homebrew_cache), "HOMEBREW_NO_AUTO_UPDATE": "1"})
    styled = subprocess.run(
        ["brew", "style", "--only-cops", cops, str(formula_path)],
        check=False,
        capture_output=True,
        text=True,
        env=environment,
    )
    if styled.returncode != 0:
        raise AssertionError(f"Homebrew formula style failed:\n{styled.stdout}{styled.stderr}")

invalid = [
    ("not-a-version", digest, "5.0.1"),
    ("0.2.0", "ABC", "5.0.1"),
    ("0.2.0", digest, "not-a-version"),
]
for arguments in invalid:
    try:
        renderer.render(*arguments)
    except ValueError:
        continue
    raise AssertionError(f"invalid Homebrew render arguments were accepted: {arguments}")
PY

provenance_repo="$TMP/provenance-repo"
provenance_origin="$TMP/provenance-origin.git"
provenance_bin="$TMP/provenance-bin"
provenance_log="$TMP/provenance-sign.log"
mkdir -p "$provenance_bin"
make_repo "$provenance_repo"
printf '%s\n' initial > "$provenance_repo/source.txt"
git -C "$provenance_repo" add source.txt
git -C "$provenance_repo" commit -qm initial
printf '%s\n' changed >> "$provenance_repo/source.txt"
git -C "$provenance_repo" add source.txt
git -C "$provenance_repo" commit -qm change
git init --bare -q "$provenance_origin"
git -C "$provenance_repo" remote add origin "$provenance_origin"
git -C "$provenance_repo" push -q -u origin HEAD:main
printf '%s\n' '{"requireAttestation":true,"requireTestsPassed":true}' > "$provenance_repo/.attest.json"
printf '#!/usr/bin/env bash\nset -euo pipefail\ncase "$1" in\n  check) echo '\''{"verdict":"proceed","riskScore":12}'\'' ;;\n  *) exit 2 ;;\nesac\n' > "$provenance_bin/augur"
printf '#!/usr/bin/env bash\nset -euo pipefail\ncommand="$1"; shift\ncase "$command" in\n  sign)\n    commit="HEAD"\n    while [ "$#" -gt 0 ]; do\n      if [ "$1" = --commit ]; then commit="$2"; shift 2; else shift; fi\n    done\n    git notes --ref=attest append -m '\''{"testsPassed":true}'\'' "$commit"\n    printf '\''signed\\n'\'' >> "%s"\n    ;;\n  verify) git notes --ref=attest show HEAD | grep -q '\''"testsPassed":true'\'' ;;\n  *) exit 2 ;;\nesac\n' "$provenance_log" > "$provenance_bin/attest"
chmod +x "$provenance_bin/augur" "$provenance_bin/attest"
git -C "$provenance_repo" notes --ref=attest add -m '{"testsPassed":false}' HEAD
git -C "$provenance_repo" push -q origin refs/notes/attest
(
  cd "$provenance_repo"
  ATTEST="$provenance_bin/attest" \
  AUGUR="$provenance_bin/augur" \
  RANGE="HEAD~1..HEAD" \
  REPORT="$TMP/provenance-augur.json" \
  bash "$ROOT/scripts/record_provenance.sh"
  ATTEST="$provenance_bin/attest" \
  AUGUR="$provenance_bin/augur" \
  RANGE="HEAD~1..HEAD" \
  REPORT="$TMP/provenance-augur.json" \
  bash "$ROOT/scripts/record_provenance.sh"
)
git --git-dir="$provenance_origin" show-ref --verify --quiet refs/notes/attest || \
  fail "provenance recorder did not publish the remote ledger"
[ "$(wc -l < "$provenance_log" | tr -d ' ')" = 1 ] || fail "provenance recorder was not idempotent"

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
for file in .trust.toml .specsync/config.toml .augur.toml .attest.json .github/workflows/trust.yml AGENTS.md; do
  assert_file "$repo/$file"
done
[ ! -e "$repo/.atlasignore" ] || fail "default adoption enabled Atlas without opt-in"
grep -Fq 'enabled = false' "$repo/.trust.toml" || fail "default adoption did not record Atlas disabled"
[ "$(cat "$repo/fledge.toml")" = "$expected_fledge" ] || fail "adopt replaced fledge.toml"

mkdir -p "$repo/nested/package"
(cd "$repo/nested/package" && "$TRUST" adopt >/dev/null)
[ "$(grep -c 'CorvidLabs trust toolchain: BEGIN' "$repo/AGENTS.md")" = 1 ] || fail "managed block duplicated"

python3 - "$repo/AGENTS.md" <<'PY'
from pathlib import Path
import sys

path = Path(sys.argv[1])
begin = "<!-- CorvidLabs trust toolchain: BEGIN (managed, do not edit inside) -->"
end = "<!-- CorvidLabs trust toolchain: END -->"
path.write_text(f"Project preface\n\n{begin}\nobsolete managed rules\n{end}\n\nProject suffix\n", encoding="utf-8")
PY
(cd "$repo" && "$TRUST" adopt >/dev/null)
grep -Fq 'Project preface' "$repo/AGENTS.md" || fail "managed update removed AGENTS.md prefix"
grep -Fq 'Project suffix' "$repo/AGENTS.md" || fail "managed update removed AGENTS.md suffix"
if grep -Fq 'obsolete managed rules' "$repo/AGENTS.md"; then fail "managed update preserved obsolete block"; fi
[ "$(grep -c 'CorvidLabs trust toolchain: BEGIN' "$repo/AGENTS.md")" = 1 ] || fail "managed update duplicated block"

isolated_bin="$TMP/isolated-bin"
mkdir -p "$isolated_bin"
ln -s "$(command -v python3)" "$isolated_bin/python3"
git_bin="$(dirname "$(command -v git)")"
status_code=0
status_json="$(cd "$repo" && PATH="$isolated_bin:$git_bin:/usr/bin:/bin" "$TRUST" status --json)" || status_code=$?
[ "$status_code" -eq 0 ] || fail "status diagnostic returned failure"
STATUS_JSON="$status_json" python3 -c 'import json, os; json.loads(os.environ["STATUS_JSON"])'
contains "$status_json" '"schemaVersion": 1'
contains "$status_json" "\"version\": \"$plugin_version\""
contains "$status_json" '"healthy": false'

skip_repo="$TMP/skip"
make_repo "$skip_repo"
cp "$repo/fledge.toml" "$skip_repo/fledge.toml"
(cd "$skip_repo" && "$TRUST" adopt --no-specs "content only" --no-attest "CI only" --no-atlas "Pages disabled" >/dev/null)
grep -Fq 'skip_reason = "content only"' "$skip_repo/.trust.toml" || fail "spec skip reason was not recorded"
grep -Fq 'skip_reason = "CI only"' "$skip_repo/.trust.toml" || fail "attest skip reason was not recorded"
[ ! -e "$skip_repo/.specsync/config.toml" ] || fail "disabled specs were installed"
if "$TRUST" action-resolve --working-directory "$skip_repo" --range HEAD~1..HEAD --profile strict >/dev/null 2>&1; then
  fail "strict override accepted a disabled contract layer"
fi

atlas_repo="$TMP/atlas-opt-in"
make_repo "$atlas_repo"
cp "$repo/fledge.toml" "$atlas_repo/fledge.toml"
(cd "$atlas_repo" && "$TRUST" adopt --atlas >/dev/null)
assert_file "$atlas_repo/.atlasignore"
grep -Fq 'enabled = true' "$atlas_repo/.trust.toml" || fail "Atlas opt-in was not recorded"
atlas_outputs="$TMP/atlas-action-outputs"
GITHUB_OUTPUT="$atlas_outputs" "$TRUST" action-resolve \
  --working-directory "$atlas_repo" --range HEAD~1..HEAD
grep -Fxq 'true' "$atlas_outputs" || fail "Action resolution did not expose enabled Atlas"

preserve_repo="$TMP/preserve-policy"
cp -R "$repo" "$preserve_repo"
sed -i.bak 's/threshold = "block"/threshold = "review"/' "$preserve_repo/.trust.toml"
rm -f "$preserve_repo/.trust.toml.bak"
preserved="$(cat "$preserve_repo/.trust.toml")"
(cd "$preserve_repo" && "$TRUST" adopt >/dev/null)
[ "$(cat "$preserve_repo/.trust.toml")" = "$preserved" ] || fail "adopt overwrote committed Trust policy"
(cd "$preserve_repo" && "$TRUST" adopt --force >/dev/null)
grep -Fq 'threshold = "block"' "$preserve_repo/.trust.toml" || fail "force did not replace Trust policy"

fresh="$TMP/fresh-python"
make_repo "$fresh"
touch "$fresh/pyproject.toml"
(cd "$fresh" && "$TRUST" adopt >/dev/null)
grep -Fq '[lanes.verify]' "$fresh/fledge.toml" || fail "fresh detected repo has no verify lane"

fresh_go="$TMP/fresh-go"
make_repo "$fresh_go"
touch "$fresh_go/go.mod"
(cd "$fresh_go" && "$TRUST" adopt >/dev/null)
grep -Fq 'fmt = "test -z \"$(gofmt -l .)\""' "$fresh_go/fledge.toml" || fail "Go format lane does not fail on unformatted files"

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
for command in fledge specsync augur; do
  printf '#!/usr/bin/env bash\necho "%s $*" >> "%s"\n' "$command" "$log" > "$fake/$command"
  chmod +x "$fake/$command"
done
printf '#!/usr/bin/env bash\necho "attest $*" >> "%s"\ncase "$*" in *unknown-policy.json*) echo "unknown policy key" >&2; exit 2;; esac\necho '\''{"checkedCommits":1,"passed":true,"violations":[]}'\''\n' "$log" > "$fake/attest"
chmod +x "$fake/attest"
printf '#!/usr/bin/env bash\necho "fledge-atlas $*" >> "%s"\necho '\''{"verdict":"all governed","stats":{"coverage_pct":100}}'\''\n' "$log" > "$fake/fledge-atlas"
chmod +x "$fake/fledge-atlas"
verify_output="$(cd "$repo" && PATH="$fake:$PATH" "$TRUST" verify --range main..HEAD)"
contains "$verify_output" "progressive provenance"
policy_path="$(cd "$repo" && python3 -c 'from pathlib import Path; print(Path(".attest.json").resolve())')"
expected="$(printf 'fledge lanes run verify\nspecsync check\naugur gate --range main..HEAD --threshold block\nattest verify --range main..HEAD --policy %s --json' "$policy_path")"
actual="$(cat "$log")"
[ "$actual" = "$expected" ] || { printf 'expected:\n%s\nactual:\n%s\n' "$expected" "$actual" >&2; fail "verification order or arguments differ"; }

atlas_verify_repo="$TMP/atlas-verify"
cp -R "$repo" "$atlas_verify_repo"
sed -i.bak '/^\[atlas\]/,/^$/ { s/enabled = false/enabled = true/; s/skip_reason = .*/skip_reason = ""/; }' \
  "$atlas_verify_repo/.trust.toml"
rm -f "$atlas_verify_repo/.trust.toml.bak"
cp "$ROOT/templates/atlasignore" "$atlas_verify_repo/.atlasignore"
: > "$log"
atlas_verify_output="$(cd "$atlas_verify_repo" && PATH="$fake:$PATH" "$TRUST" verify --range main..HEAD)"
contains "$atlas_verify_output" "atlas: all governed"
contains "$(cat "$log")" "fledge-atlas "
contains "$(cat "$log")" " --json"

attest_runtime_repo="$TMP/attest-runtime"
cp -R "$repo" "$attest_runtime_repo"
sed -i.bak 's/policy = ".attest.json"/policy = "unknown-policy.json"/' "$attest_runtime_repo/.trust.toml"
rm -f "$attest_runtime_repo/.trust.toml.bak"
printf '%s\n' '{"unknownPolicy": true}' > "$attest_runtime_repo/unknown-policy.json"
if (cd "$attest_runtime_repo" && PATH="$fake:$PATH" "$TRUST" verify --range main..HEAD >/dev/null 2>&1); then
  fail "Attest runtime failure was softened"
fi

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

printf '%s\n' '{' > "$doctor_repo/.attest.json"
if (cd "$doctor_repo" && "$TRUST" doctor --json >/dev/null); then fail "malformed policy returned success"; fi

risk_repo="$TMP/missing-risk"
cp -R "$repo" "$risk_repo"
rm "$risk_repo/.augur.toml"
if (cd "$risk_repo" && "$TRUST" doctor --json >/dev/null); then fail "missing Augur config returned success"; fi

unknown_nested_repo="$TMP/unknown-nested"
cp -R "$repo" "$unknown_nested_repo"
sed -i.bak '/^\[provenance\]/a\
mdoe = "soft"
' "$unknown_nested_repo/.trust.toml"
rm -f "$unknown_nested_repo/.trust.toml.bak"
if (cd "$unknown_nested_repo" && "$TRUST" doctor --json >/dev/null 2>&1); then
  fail "unknown nested policy key was accepted"
fi

override_repo="$TMP/overrides"
cp -R "$repo" "$override_repo"
sed -i.bak 's/profile = "standard"/profile = "strict"/' "$override_repo/.trust.toml"
rm -f "$override_repo/.trust.toml.bak"
if "$TRUST" action-resolve --working-directory "$override_repo" --range HEAD~1..HEAD --profile standard >/dev/null 2>&1; then
  fail "workflow override downgraded strict profile"
fi
sed -i.bak 's/profile = "strict"/profile = "standard"/; s/threshold = "block"/threshold = "review"/' "$override_repo/.trust.toml"
rm -f "$override_repo/.trust.toml.bak"
if "$TRUST" action-resolve --working-directory "$override_repo" --range HEAD~1..HEAD --threshold block >/dev/null 2>&1; then
  fail "workflow override weakened Augur threshold"
fi
if env -u GITHUB_EVENT_NAME -u GITHUB_EVENT_PATH -u GITHUB_SHA \
  "$TRUST" action-resolve --working-directory "$override_repo" >/dev/null 2>&1; then
  fail "manual Action resolution without range or upstream succeeded"
fi

event_repo="$TMP/event-ranges"
"$ROOT/tests/setup-action-fixture.sh" "$event_repo"
base="$(git -C "$event_repo" rev-parse HEAD~1)"
head="$(git -C "$event_repo" rev-parse HEAD)"
event="$TMP/event.json"
outputs="$TMP/action-outputs"
printf '{"pull_request":{"base":{"sha":"%s"},"head":{"sha":"%s"}}}\n' "$base" "$head" > "$event"
GITHUB_EVENT_NAME=pull_request GITHUB_EVENT_PATH="$event" GITHUB_OUTPUT="$outputs" \
  "$TRUST" action-resolve --working-directory "$event_repo"
grep -Fxq "$base..$head" "$outputs" || fail "pull request range was not resolved"

cp "$event_repo/.trust.toml" "$TMP/event-trust.toml"
sed -i.bak '/^\[contract\]/,/^\[risk\]/ { s/enabled = true/enabled = false/; s/skip_reason = ""/skip_reason = "weakened in PR"/; }' "$event_repo/.trust.toml"
rm -f "$event_repo/.trust.toml.bak"
if GITHUB_EVENT_NAME=pull_request GITHUB_EVENT_PATH="$event" \
  "$TRUST" action-resolve --working-directory "$event_repo" >/dev/null 2>&1; then
  fail "pull request policy disabled a committed gate"
fi
cp "$TMP/event-trust.toml" "$event_repo/.trust.toml"

mv "$event_repo/.attest.json" "$event_repo/.attest.json.saved"
if GITHUB_EVENT_NAME=pull_request GITHUB_EVENT_PATH="$event" \
  "$TRUST" action-resolve --working-directory "$event_repo" >/dev/null 2>&1; then
  fail "Action accepted a missing enabled layer configuration"
fi
mv "$event_repo/.attest.json.saved" "$event_repo/.attest.json"

: > "$outputs"
printf '{"before":"%s","after":"%s"}\n' "$base" "$head" > "$event"
GITHUB_EVENT_NAME=push GITHUB_EVENT_PATH="$event" GITHUB_OUTPUT="$outputs" \
  "$TRUST" action-resolve --working-directory "$event_repo"
grep -Fxq "$base..$head" "$outputs" || fail "push range was not resolved"

: > "$outputs"
printf '{"before":"0000000000000000000000000000000000000000","after":"%s"}\n' "$head" > "$event"
GITHUB_EVENT_NAME=push GITHUB_EVENT_PATH="$event" GITHUB_OUTPUT="$outputs" \
  "$TRUST" action-resolve --working-directory "$event_repo"
grep -Fxq "commit" "$outputs" || fail "initial push did not select commit verification"
grep -Fxq "$head" "$outputs" || fail "initial push selected the wrong commit"

echo "trust tests passed"
