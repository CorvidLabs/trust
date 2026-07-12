#!/usr/bin/env python3
from __future__ import annotations

from dataclasses import dataclass
import json
import re
import sys


__all__ = []

SEMVER = re.compile(
    r"^v(?P<major>0|[1-9][0-9]*)\."
    r"(?P<minor>0|[1-9][0-9]*)\."
    r"(?P<patch>0|[1-9][0-9]*)"
    r"(?:-(?P<prerelease>[0-9A-Za-z.-]+))?"
    r"$"
)


@dataclass(frozen=True)
class Version:
    tag: str
    major: int
    minor: int
    patch: int
    prerelease: tuple[str, ...]

    @property
    def stable(self) -> bool:
        return not self.prerelease

    def precedence(self) -> tuple[int, int, int, int, tuple[tuple[int, int | str], ...]]:
        identifiers: list[tuple[int, int | str]] = []
        for identifier in self.prerelease:
            if identifier.isdigit():
                identifiers.append((0, int(identifier)))
            else:
                identifiers.append((1, identifier))
        return self.major, self.minor, self.patch, int(self.stable), tuple(identifiers)


def parse(tag: str) -> Version | None:
    match = SEMVER.fullmatch(tag)
    if match is None:
        return None
    prerelease = tuple(match.group("prerelease").split(".")) if match.group("prerelease") else ()
    invalid_prerelease = any(
        not identifier or (len(identifier) > 1 and identifier.startswith("0") and identifier.isdigit())
        for identifier in prerelease
    )
    if invalid_prerelease:
        return None
    return Version(
        tag=tag,
        major=int(match.group("major")),
        minor=int(match.group("minor")),
        patch=int(match.group("patch")),
        prerelease=prerelease,
    )


def decision(target_tag: str, tags: list[str]) -> dict[str, object]:
    target = parse(target_tag)
    if target is None:
        raise ValueError(f"invalid semantic release tag: {target_tag}")
    major_tag = f"v{target.major}"
    if target.major != 0 and not target.stable:
        return {
            "major": major_tag,
            "promote": False,
            "reason": f"{target_tag} is a prerelease and cannot move stable channel {major_tag}",
        }
    eligible = []
    for tag in tags:
        version = parse(tag)
        if version is None or version.major != target.major:
            continue
        if target.major != 0 and not version.stable:
            continue
        eligible.append(version)
    if not any(version.tag == target_tag for version in eligible):
        eligible.append(target)
    latest = max(eligible, key=Version.precedence)
    promote = target.precedence() == latest.precedence()
    reason = (
        f"{target_tag} is the newest eligible {major_tag} release"
        if promote
        else f"{target_tag} is older than {latest.tag}"
    )
    return {"major": major_tag, "promote": promote, "reason": reason}


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: release_channel.py TAG", file=sys.stderr)
        return 2
    try:
        result = decision(sys.argv[1], [line.strip() for line in sys.stdin if line.strip()])
    except ValueError as error:
        print(error, file=sys.stderr)
        return 2
    print(json.dumps(result, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
