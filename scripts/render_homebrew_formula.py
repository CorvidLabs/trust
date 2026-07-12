#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path
import re

from release_channel import parse


__all__ = []

ROOT = Path(__file__).resolve().parent.parent
TEMPLATE = ROOT / "packaging/homebrew/corvid-trust.rb.in"
SHA256 = re.compile(r"^[0-9a-f]{64}$")


def render(version: str, sha256: str, specsync_version: str) -> str:
    if parse(f"v{version}") is None:
        raise ValueError(f"invalid Trust semantic version: {version}")
    if not SHA256.fullmatch(sha256):
        raise ValueError("Trust source SHA-256 must be exactly 64 lowercase hexadecimal characters")
    if parse(f"v{specsync_version}") is None:
        raise ValueError(f"invalid SpecSync semantic version: {specsync_version}")
    formula = TEMPLATE.read_text(encoding="utf-8")
    replacements = {
        "@TRUST_VERSION@": version,
        "@TRUST_SHA256@": sha256,
        "@SPECSYNC_VERSION@": specsync_version,
    }
    for placeholder, value in replacements.items():
        formula = formula.replace(placeholder, value)
    if any(placeholder in formula for placeholder in replacements):
        raise ValueError("Homebrew formula template contains unresolved placeholders")
    return formula


def parser() -> argparse.ArgumentParser:
    argument_parser = argparse.ArgumentParser(description="Render the immutable Corvid Trust Homebrew formula")
    argument_parser.add_argument("version", help="Trust release version without the v prefix")
    argument_parser.add_argument("sha256", help="SHA-256 of the GitHub source archive")
    argument_parser.add_argument("--specsync-version", required=True, help="Expected SpecSync dependency version")
    return argument_parser


def main() -> int:
    arguments = parser().parse_args()
    try:
        print(render(arguments.version, arguments.sha256, arguments.specsync_version), end="")
    except (OSError, ValueError) as error:
        raise SystemExit(f"cannot render Homebrew formula: {error}") from error
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
