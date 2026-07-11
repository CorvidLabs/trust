#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path
import sys

import yaml


ROOT = Path(__file__).resolve().parent.parent


def fail(message: str) -> None:
    print(f"validation error: {message}", file=sys.stderr)
    raise SystemExit(1)


for relative in ("action.yml", "templates/trust.yml", ".github/workflows/ci.yml"):
    path = ROOT / relative
    with path.open(encoding="utf-8") as stream:
        document = yaml.safe_load(stream)
    if not isinstance(document, dict):
        fail(f"{relative} must contain a YAML object")

with (ROOT / "templates/attest.json").open(encoding="utf-8") as stream:
    policy = json.load(stream)
if policy.get("requireAttestation") is not True:
    fail("the managed Attest policy must require one attestation")

plugin = (ROOT / "plugin.toml").read_text(encoding="utf-8")
if 'name = "trust"' not in plugin or 'binary = "bin/fledge-trust"' not in plugin:
    fail("plugin.toml does not expose the trust command")

action = (ROOT / "action.yml").read_text(encoding="utf-8")
for dependency in ("CorvidLabs/spec-sync@v4", "CorvidLabs/augur@v1", "CorvidLabs/attest@v1"):
    if dependency not in action:
        fail(f"action.yml does not compose {dependency}")

print("trust validation passed")
