#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path
import re
import sys
import tomllib

import yaml


__all__ = []

ROOT = Path(__file__).resolve().parent.parent
FULL_ACTION_SHA = re.compile(r"^[^@\s]+@[0-9a-f]{40}$")
ALLOWED_CHANNELS = {"CorvidLabs/trust@v0"}


def fail(message: str) -> None:
    print(f"validation error: {message}", file=sys.stderr)
    raise SystemExit(1)


def action_references(value: object) -> list[str]:
    references: list[str] = []
    if isinstance(value, dict):
        for key, nested in value.items():
            if key == "uses" and isinstance(nested, str):
                references.append(nested)
            else:
                references.extend(action_references(nested))
    elif isinstance(value, list):
        for nested in value:
            references.extend(action_references(nested))
    return references


yaml_documents: dict[str, dict[str, object]] = {}
for relative in (
    "action.yml",
    "templates/trust.yml",
    ".github/workflows/ci.yml",
    ".github/workflows/release.yml",
    ".github/workflows/trust.yml",
):
    path = ROOT / relative
    with path.open(encoding="utf-8") as stream:
        document = yaml.safe_load(stream)
    if not isinstance(document, dict):
        fail(f"{relative} must contain a YAML object")
    yaml_documents[relative] = document

for relative, document in yaml_documents.items():
    for reference in action_references(document):
        if reference.startswith("./") or reference in ALLOWED_CHANNELS:
            continue
        if not FULL_ACTION_SHA.fullmatch(reference):
            fail(f"{relative} must pin external Action reference to a full commit SHA: {reference}")

validation_install = "python3 -m pip install --disable-pip-version-check pyyaml==6.0.3"
for relative in (".github/workflows/ci.yml", ".github/workflows/release.yml", ".github/workflows/trust.yml"):
    workflow = (ROOT / relative).read_text(encoding="utf-8")
    if validation_install not in workflow:
        fail(f"{relative} must install the pinned validation dependency")

self_ci = (ROOT / ".github/workflows/ci.yml").read_text(encoding="utf-8")
for required in (
    "record-provenance:",
    "needs: [validate, plugin-windows, action-smoke, action-provenance, action-atlas, action-fatal-paths]",
    "contents: write",
    "bash scripts/record_provenance.sh",
):
    if required not in self_ci:
        fail(f"CI workflow is missing durable main provenance behavior: {required}")

provenance_script = (ROOT / "scripts/record_provenance.sh").read_text(encoding="utf-8")
for required in (
    'git push origin refs/notes/attest',
    'verify --commit HEAD --policy "$POLICY"',
    "could not publish refs/notes/attest after three verified attempts",
    "git ls-remote --exit-code origin refs/notes/attest",
):
    if required not in provenance_script:
        fail(f"provenance recorder is missing durable publication behavior: {required}")

homebrew_template = (ROOT / "packaging/homebrew/corvid-trust.rb.in").read_text(encoding="utf-8")
for required in (
    '@TRUST_VERSION@',
    '@TRUST_SHA256@',
    '@SPECSYNC_VERSION@',
    'depends_on "corvidlabs/tap/fledge"',
    'depends_on "corvidlabs/tap/spec-sync"',
    'depends_on "corvidlabs/tap/augur"',
    'depends_on "corvidlabs/tap/attest"',
    'bin.write_env_script libexec/"bin/fledge-trust"',
    'formula_opt_libexec("python@3.11")',
    'shell_output("fledge trust --version")',
):
    if required not in homebrew_template:
        fail(f"Homebrew formula template is missing Trust bundle behavior: {required}")

template = (ROOT / "templates/trust.yml").read_text(encoding="utf-8")
for dependency in (
    "CorvidLabs/fledge-plugin-atlas@bfae900492615c6263c5ef431d1326eabb8b0406",
    "actions/upload-pages-artifact@fc324d3547104276b827a68afc52ff2a11cc49c9",
    "actions/deploy-pages@cd2ce8fcbc39b97be8ca5fce6e763baed58fa128",
):
    if dependency not in template:
        fail(f"templates/trust.yml does not compose {dependency}")
if "github.event_name == 'push'" not in template:
    fail("templates/trust.yml must limit Atlas publication to push events")
if "pages: write" not in template or "id-token: write" not in template:
    fail("templates/trust.yml must scope Pages deployment permissions")

with (ROOT / "templates/trust.toml").open("rb") as stream:
    template_policy = tomllib.load(stream)
if template_policy.get("atlas") != {
    "enabled": False,
    "skip_reason": "Atlas publication was not enabled during adoption",
}:
    fail("templates/trust.toml must keep Atlas disabled by default")

with (ROOT / "templates/attest.json").open(encoding="utf-8") as stream:
    policy = json.load(stream)
if policy.get("requireAttestation") is not True:
    fail("the managed Attest policy must require one attestation")

with (ROOT / ".attest.json").open(encoding="utf-8") as stream:
    self_policy = json.load(stream)
if self_policy != {"requireAttestation": True, "requireTestsPassed": True}:
    fail("Trust must require a tests-passed attestation for its own landed commits")

with (ROOT / ".trust.toml").open("rb") as stream:
    self_trust = tomllib.load(stream)
if self_trust.get("provenance") != {"mode": "soft", "policy": ".attest.json", "skip_reason": ""}:
    fail("Trust self-provenance must remain enabled in bootstrap-safe soft mode until the ledger exists")

plugin = (ROOT / "plugin.toml").read_text(encoding="utf-8")
if 'name = "trust"' not in plugin or 'binary = "bin/fledge-trust"' not in plugin:
    fail("plugin.toml does not expose the trust command")

with (ROOT / "fledge.toml").open("rb") as stream:
    fledge = tomllib.load(stream)
release_lane = fledge.get("lanes", {}).get("release", {})
if release_lane.get("steps") != ["fmt", "lint", "test", "spec"]:
    fail("fledge.toml release lane must run code checks before the spec contract gate")

release_workflow = (ROOT / ".github/workflows/release.yml").read_text(encoding="utf-8")
for required in (
    'tags: ["v*.*.*"]',
    'fledge plugins install "$REPOSITORY@$REF_NAME"',
    'fledge trust doctor --root "$FIXTURE"',
    'fledge trust verify --root "$FIXTURE" --range HEAD~1..HEAD',
    "needs: exact-tag-dogfood",
    "args=(release create",
    'python3 scripts/release_channel.py "$REF_NAME"',
    "Protected channel promotion",
    "GITHUB_STEP_SUMMARY",
):
    if required not in release_workflow:
        fail(f"release workflow is missing gated publication behavior: {required}")

action = (ROOT / "action.yml").read_text(encoding="utf-8")
if "atlas-enabled:" not in action:
    fail("action.yml must expose the committed Atlas publication decision")
dependencies = {
    "CorvidLabs/spec-sync@d6d8512f9a1d75f308df1e9a8f52b47ca9e839ee": "5.0.0",
    "CorvidLabs/augur@25ef933988d41c7051c7dadd4b303eb9c8d6c2e0": "1.0.0",
    "CorvidLabs/attest@e8a2d928eb4b9a33185c32ba7b8e9b3a985987f2": "1.0.0",
}
for dependency in dependencies:
    if dependency not in action:
        fail(f"action.yml does not compose {dependency}")

action_runs = yaml_documents["action.yml"].get("runs")
if not isinstance(action_runs, dict):
    fail("action.yml runs must be a YAML object")
action_steps = action_runs.get("steps")
if not isinstance(action_steps, list):
    fail("action.yml runs.steps must be a YAML list")
for step in action_steps:
    if not isinstance(step, dict) or step.get("uses") not in dependencies:
        continue
    expected_version = dependencies[step["uses"]]
    inputs = step.get("with", {})
    if not isinstance(inputs, dict) or inputs.get("version") != expected_version:
        fail(f"action.yml must pair {step['uses']} with binary version {expected_version}")

print("trust validation passed")
