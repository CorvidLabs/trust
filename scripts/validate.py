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
for dependency in (
    "CorvidLabs/spec-sync@0cb1a57cf56105e28fea1288db698ff94d9b9f61",
    "CorvidLabs/augur@25ef933988d41c7051c7dadd4b303eb9c8d6c2e0",
    "CorvidLabs/attest@e8a2d928eb4b9a33185c32ba7b8e9b3a985987f2",
):
    if dependency not in action:
        fail(f"action.yml does not compose {dependency}")

print("trust validation passed")
