#!/usr/bin/env python3
from __future__ import annotations

import argparse
from dataclasses import asdict, dataclass
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
from typing import Any
import uuid


__all__ = []

try:
    import tomllib
except ImportError:
    try:
        import tomli as tomllib
    except ImportError:
        print("fledge trust: Python 3.11+ or the 'tomli' package is required", file=sys.stderr)
        raise SystemExit(1)


ROOT = Path(__file__).resolve().parent.parent
TEMPLATES = ROOT / "templates"
BEGIN = "<!-- CorvidLabs trust toolchain: BEGIN (managed, do not edit inside) -->"
END = "<!-- CorvidLabs trust toolchain: END -->"
RISK_ORDER = {"proceed": 0, "review": 1, "block": 2}
PROVENANCE_ORDER = {"off": 0, "soft": 1, "enforce": 2}
PROVENANCE_SCOPE_ORDER = {"changes": 0, "baseline": 1}
DEFAULT_ATLAS_SKIP_REASON = "Atlas publication was not enabled during adoption"


class TrustError(RuntimeError):
    pass


def trust_version() -> str:
    manifest = ROOT / "plugin.toml"
    try:
        with manifest.open("rb") as stream:
            document = tomllib.load(stream)
    except (OSError, tomllib.TOMLDecodeError) as error:
        raise TrustError(f"cannot read Trust plugin version: {error}") from error
    plugin = document.get("plugin")
    version = plugin.get("version") if isinstance(plugin, dict) else None
    if not isinstance(version, str) or not version:
        raise TrustError("plugin.toml is missing plugin.version")
    return version


@dataclass(frozen=True)
class TrustConfig:
    schema_version: int
    profile: str
    lifecycle_command: list[str]
    contract_enabled: bool
    contract_require_coverage: int
    contract_skip_reason: str
    risk_threshold: str
    provenance_mode: str
    provenance_scope: str
    provenance_policy: str
    provenance_skip_reason: str
    atlas_enabled: bool
    atlas_skip_reason: str

    @property
    def strict(self) -> bool:
        return self.profile == "strict"

    @property
    def effective_contract_coverage(self) -> int:
        return 100 if self.strict else self.contract_require_coverage

    @property
    def effective_provenance_mode(self) -> str:
        return "enforce" if self.strict else self.provenance_mode


def run(
    arguments: list[str],
    *,
    cwd: Path,
    check: bool = True,
    capture: bool = False,
) -> subprocess.CompletedProcess[str]:
    run_arguments = arguments
    try:
        result = subprocess.run(
            run_arguments,
            cwd=cwd,
            check=False,
            text=True,
            stdout=subprocess.PIPE if capture else None,
            stderr=subprocess.PIPE if capture else None,
        )
    except FileNotFoundError:
        bash = shutil.which("bash") if os.name == "nt" else None
        if bash is None:
            raise
        run_arguments = [bash, "-c", 'exec "$@"', "trust", *arguments]
        result = subprocess.run(
            run_arguments,
            cwd=cwd,
            check=False,
            text=True,
            stdout=subprocess.PIPE if capture else None,
            stderr=subprocess.PIPE if capture else None,
        )
    if check and result.returncode != 0:
        detail = (result.stderr or result.stdout or "").strip()
        suffix = f": {detail}" if detail else ""
        raise TrustError(f"{' '.join(arguments)} failed with exit {result.returncode}{suffix}")
    return result


def command_exists(command: str) -> bool:
    return shutil.which(command) is not None


def git_root(explicit: str | None) -> Path:
    start = Path(explicit or ".").expanduser().resolve()
    result = run(["git", "rev-parse", "--show-toplevel"], cwd=start, capture=True)
    return Path(result.stdout.strip()).resolve()


def table(document: dict[str, Any], key: str) -> dict[str, Any]:
    value = document.get(key, {})
    if not isinstance(value, dict):
        raise TrustError(f"[{key}] must be a TOML table")
    return value


def text(value: Any, field: str) -> str:
    if not isinstance(value, str):
        raise TrustError(f"{field} must be a string")
    return value


def boolean(value: Any, field: str) -> bool:
    if not isinstance(value, bool):
        raise TrustError(f"{field} must be true or false")
    return value


def reject_unknown_keys(section: dict[str, Any], name: str, allowed: set[str]) -> None:
    unknown = sorted(set(section) - allowed)
    if unknown:
        raise TrustError(f"unknown [{name}] key(s): {', '.join(unknown)}")


def load_config(path: Path) -> TrustConfig:
    if not path.is_file():
        raise TrustError(f"missing Trust configuration: {path}")
    try:
        with path.open("rb") as stream:
            document = tomllib.load(stream)
    except (OSError, tomllib.TOMLDecodeError) as error:
        raise TrustError(f"invalid Trust configuration {path}: {error}") from error

    allowed_root = {"schema_version", "profile", "lifecycle", "contract", "risk", "provenance", "atlas"}
    unknown_root = sorted(set(document) - allowed_root)
    if unknown_root:
        raise TrustError(f"unknown Trust configuration key(s): {', '.join(unknown_root)}")

    schema_version = document.get("schema_version")
    if schema_version != 1:
        raise TrustError("schema_version must be 1")
    profile = text(document.get("profile", "standard"), "profile")
    if profile not in {"standard", "strict"}:
        raise TrustError("profile must be standard or strict")

    lifecycle = table(document, "lifecycle")
    reject_unknown_keys(lifecycle, "lifecycle", {"command"})
    command = lifecycle.get("command")
    if not isinstance(command, list) or not command or not all(isinstance(item, str) and item for item in command):
        raise TrustError("lifecycle.command must be a nonempty string array")

    contract = table(document, "contract")
    reject_unknown_keys(contract, "contract", {"enabled", "require_coverage", "skip_reason"})
    contract_enabled = boolean(contract.get("enabled", True), "contract.enabled")
    coverage = contract.get("require_coverage", 0)
    if not isinstance(coverage, int) or isinstance(coverage, bool) or not 0 <= coverage <= 100:
        raise TrustError("contract.require_coverage must be an integer from 0 through 100")
    contract_reason = text(contract.get("skip_reason", ""), "contract.skip_reason").strip()
    if not contract_enabled and not contract_reason:
        raise TrustError("disabled contract layer requires contract.skip_reason")

    risk = table(document, "risk")
    reject_unknown_keys(risk, "risk", {"threshold"})
    threshold = text(risk.get("threshold", "block"), "risk.threshold")
    if threshold not in RISK_ORDER:
        raise TrustError("risk.threshold must be proceed, review, or block")

    provenance = table(document, "provenance")
    reject_unknown_keys(provenance, "provenance", {"mode", "scope", "policy", "skip_reason"})
    provenance_mode = text(provenance.get("mode", "soft"), "provenance.mode")
    if provenance_mode not in {"soft", "enforce", "off"}:
        raise TrustError("provenance.mode must be soft, enforce, or off")
    provenance_scope = text(provenance.get("scope", "changes"), "provenance.scope")
    if provenance_scope not in {"changes", "baseline"}:
        raise TrustError("provenance.scope must be changes or baseline")
    policy = text(provenance.get("policy", ".attest.json"), "provenance.policy")
    if provenance_mode != "off" and not policy:
        raise TrustError("provenance.policy must be nonempty when provenance is enabled")
    provenance_reason = text(provenance.get("skip_reason", ""), "provenance.skip_reason").strip()
    if provenance_mode == "off" and not provenance_reason:
        raise TrustError("disabled provenance layer requires provenance.skip_reason")

    atlas = table(document, "atlas")
    reject_unknown_keys(atlas, "atlas", {"enabled", "skip_reason"})
    atlas_enabled = boolean(atlas.get("enabled", True), "atlas.enabled")
    atlas_reason = text(atlas.get("skip_reason", ""), "atlas.skip_reason").strip()
    if not atlas_enabled and not atlas_reason:
        raise TrustError("disabled Atlas layer requires atlas.skip_reason")

    if profile == "strict" and (not contract_enabled or provenance_mode == "off"):
        raise TrustError("strict profile cannot disable contract or provenance")

    return TrustConfig(
        schema_version=1,
        profile=profile,
        lifecycle_command=list(command),
        contract_enabled=contract_enabled,
        contract_require_coverage=coverage,
        contract_skip_reason=contract_reason,
        risk_threshold=threshold,
        provenance_mode=provenance_mode,
        provenance_scope=provenance_scope,
        provenance_policy=policy,
        provenance_skip_reason=provenance_reason,
        atlas_enabled=atlas_enabled,
        atlas_skip_reason=atlas_reason,
    )


def render_config(
    profile: str,
    no_specs: str,
    no_attest: str,
    atlas_enabled: bool,
    atlas_skip_reason: str,
) -> str:
    return f'''schema_version = 1
profile = "{profile}"

[lifecycle]
command = ["fledge", "lanes", "run", "verify"]

[contract]
enabled = {str(not bool(no_specs)).lower()}
require_coverage = 0
skip_reason = {json.dumps(no_specs)}

[risk]
threshold = "block"

[provenance]
mode = "{'off' if no_attest else 'soft'}"
scope = "changes"
policy = ".attest.json"
skip_reason = {json.dumps(no_attest)}

[atlas]
enabled = {str(atlas_enabled).lower()}
skip_reason = {json.dumps("" if atlas_enabled else atlas_skip_reason)}
'''


def managed_agents(existing: str) -> str:
    begins = existing.count(BEGIN)
    ends = existing.count(END)
    if begins != ends or begins > 1:
        raise TrustError("AGENTS.md has malformed or duplicate CorvidLabs trust markers")
    block = (TEMPLATES / "agents-rules.md").read_text(encoding="utf-8").strip()
    if begins == 0:
        prefix = existing.rstrip()
        return f"{prefix}\n\n{block}\n" if prefix else f"{block}\n"
    start = existing.index(BEGIN)
    finish = existing.index(END, start) + len(END)
    return f"{existing[:start]}{block}{existing[finish:]}"


def detected_fledge(root: Path) -> str:
    package_json = root / "package.json"
    if (root / "Cargo.toml").is_file():
        tasks = {'build': 'cargo build', 'test': 'cargo test', 'lint': 'cargo clippy -- -D warnings', 'fmt': 'cargo fmt --check'}
    elif (root / "Package.swift").is_file():
        tasks = {'build': 'swift build', 'test': 'swift test'}
    elif (root / "go.mod").is_file():
        tasks = {
            'build': 'go build ./...',
            'test': 'go test ./...',
            'lint': 'go vet ./...',
            'fmt': 'test -z "$(gofmt -l .)"',
        }
    elif any((root / marker).is_file() for marker in ("pyproject.toml", "setup.py", "requirements.txt")):
        tasks = {'test': 'pytest', 'lint': 'ruff check .', 'fmt': 'ruff format --check .'}
    elif package_json.is_file():
        try:
            package = json.loads(package_json.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as error:
            raise TrustError(f"cannot inspect package.json: {error}") from error
        if not isinstance(package, dict):
            raise TrustError("cannot inspect package.json: root value must be an object")
        scripts = package.get("scripts", {})
        if not isinstance(scripts, dict):
            raise TrustError("cannot inspect package.json: scripts must be an object")
        runner = "bun run" if (root / "bun.lock").exists() or (root / "bun.lockb").exists() else "npm run"
        tasks = {name: f"{runner} {name}" for name in ("fmt", "lint", "test", "build") if name in scripts}
    else:
        raise TrustError("Fledge could not infer a real verification lane; configure fledge.toml and rerun adopt")
    if "test" not in tasks:
        raise TrustError("detected project has no test task; configure fledge.toml and rerun adopt")
    lines = ["[tasks]"] + [f'{name} = {json.dumps(command)}' for name, command in tasks.items()]
    lines += ["", "[lanes.verify]", 'description = "The single project verification gate"', f"steps = {json.dumps(list(tasks))}"]
    return "\n".join(lines) + "\n"


def validate_fledge(content: str) -> None:
    try:
        parsed = tomllib.loads(content)
    except tomllib.TOMLDecodeError as error:
        raise TrustError(f"invalid fledge.toml: {error}") from error
    lanes = parsed.get("lanes", {})
    verify = lanes.get("verify") if isinstance(lanes, dict) else None
    if not isinstance(verify, dict) or not verify.get("steps"):
        raise TrustError("fledge.toml must define a nonempty [lanes.verify] lane")


def validate_toml_file(path: Path, label: str) -> None:
    if not path.is_file():
        raise TrustError(f"missing {label} configuration: {path.relative_to(path.parent.parent)}")
    try:
        with path.open("rb") as stream:
            document = tomllib.load(stream)
    except (OSError, tomllib.TOMLDecodeError) as error:
        raise TrustError(f"invalid {label} configuration {path}: {error}") from error
    if not isinstance(document, dict) or not document:
        raise TrustError(f"invalid {label} configuration {path}: expected a nonempty TOML table")


def validate_layer_files(root: Path, config: TrustConfig) -> None:
    validate_toml_file(root / ".augur.toml", "Augur")
    if config.contract_enabled:
        validate_toml_file(root / ".specsync/config.toml", "SpecSync")
    if config.effective_provenance_mode != "off":
        policy = root / config.provenance_policy
        if not policy.is_file():
            raise TrustError(f"provenance policy is missing: {config.provenance_policy}")
        try:
            document = json.loads(policy.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as error:
            raise TrustError(f"invalid provenance policy {policy}: {error}") from error
        if not isinstance(document, dict) or not document:
            raise TrustError(f"invalid provenance policy {policy}: expected a nonempty JSON object")
    if config.atlas_enabled and not (root / ".atlasignore").is_file():
        raise TrustError("Atlas is enabled but .atlasignore is missing")


def validate_generated_files(writes: dict[Path, str]) -> None:
    for path, content in writes.items():
        if path.name in {"fledge.toml", "config.toml", ".augur.toml"}:
            try:
                document = tomllib.loads(content)
            except tomllib.TOMLDecodeError as error:
                raise TrustError(f"generated configuration is invalid for {path}: {error}") from error
            if not isinstance(document, dict) or not document:
                raise TrustError(f"generated configuration is empty for {path}")
        elif path.suffix == ".json":
            try:
                document = json.loads(content)
            except json.JSONDecodeError as error:
                raise TrustError(f"generated configuration is invalid for {path}: {error}") from error
            if not isinstance(document, dict) or not document:
                raise TrustError(f"generated configuration is empty for {path}")


def atomic_writes(writes: dict[Path, str]) -> None:
    originals: dict[Path, bytes | None] = {}
    written: list[Path] = []
    temporary: Path | None = None
    try:
        for path, content in writes.items():
            originals[path] = path.read_bytes() if path.exists() else None
            path.parent.mkdir(parents=True, exist_ok=True)
            with tempfile.NamedTemporaryFile("w", encoding="utf-8", dir=path.parent, delete=False) as stream:
                stream.write(content)
                temporary = Path(stream.name)
            os.replace(temporary, path)
            temporary = None
            written.append(path)
    except Exception:
        if temporary is not None:
            temporary.unlink(missing_ok=True)
        for path in reversed(written):
            original = originals[path]
            if original is None:
                path.unlink(missing_ok=True)
            else:
                path.write_bytes(original)
        raise


def adopt(arguments: argparse.Namespace) -> int:
    root = git_root(arguments.root)
    profile = arguments.profile
    trust_path = root / ".trust.toml"
    fledge_path = root / "fledge.toml"
    if fledge_path.exists():
        fledge_content = fledge_path.read_text(encoding="utf-8")
    else:
        fledge_content = detected_fledge(root)
    validate_fledge(fledge_content)

    if trust_path.exists() and not arguments.force:
        config_content = trust_path.read_text(encoding="utf-8")
    else:
        atlas_reason = arguments.no_atlas or DEFAULT_ATLAS_SKIP_REASON
        config_content = render_config(
            profile,
            arguments.no_specs or "",
            arguments.no_attest or "",
            arguments.atlas,
            atlas_reason,
        )
    with tempfile.NamedTemporaryFile("w", suffix=".toml", delete=False) as stream:
        stream.write(config_content)
        config_temp = Path(stream.name)
    try:
        adoption_config = load_config(config_temp)
    finally:
        config_temp.unlink(missing_ok=True)

    existing_agents = (root / "AGENTS.md").read_text(encoding="utf-8") if (root / "AGENTS.md").exists() else ""
    writes: dict[Path, str] = {
        root / "AGENTS.md": managed_agents(existing_agents),
        root / ".github/workflows/trust.yml": (TEMPLATES / "trust.yml").read_text(encoding="utf-8"),
    }
    if arguments.force or not trust_path.exists():
        writes[trust_path] = config_content
    if not fledge_path.exists():
        writes[fledge_path] = fledge_content
    if adoption_config.contract_enabled:
        writes[root / ".specsync/config.toml"] = (TEMPLATES / "specsync.toml").read_text(encoding="utf-8")
    writes[root / ".augur.toml"] = (TEMPLATES / "augur.toml").read_text(encoding="utf-8")
    if adoption_config.effective_provenance_mode != "off":
        writes[root / ".attest.json"] = (TEMPLATES / "attest.json").read_text(encoding="utf-8")
    if adoption_config.atlas_enabled:
        writes[root / ".atlasignore"] = (TEMPLATES / "atlasignore").read_text(encoding="utf-8")

    if not arguments.force:
        protected = {path: content for path, content in writes.items() if path.exists() and path.name != "AGENTS.md"}
        for path in protected:
            writes.pop(path)

    validate_generated_files(writes)

    for path in writes:
        print(f"{'write' if not path.exists() else 'update'} {path.relative_to(root)}")
    if arguments.dry_run:
        print("dry run complete; no files changed")
        return 0
    atomic_writes(writes)
    print("trust adoption complete; run: fledge trust doctor")
    return 0


def apply_overrides(config: TrustConfig, profile: str | None, threshold: str | None) -> TrustConfig:
    values = asdict(config)
    if profile:
        if profile not in {"standard", "strict"}:
            raise TrustError("profile override must be standard or strict")
        if config.strict and profile != "strict":
            raise TrustError("workflow or CLI override cannot weaken strict profile")
        if profile == "strict" and (not config.contract_enabled or config.provenance_mode == "off"):
            raise TrustError("strict profile override requires enabled contract and provenance layers")
        values["profile"] = profile
    if threshold:
        if threshold not in RISK_ORDER:
            raise TrustError("threshold override must be proceed, review, or block")
        if RISK_ORDER[threshold] > RISK_ORDER[config.risk_threshold]:
            raise TrustError("threshold override cannot weaken committed risk policy")
        values["risk_threshold"] = threshold
    return TrustConfig(**values)


def load_config_text(content: str) -> TrustConfig:
    with tempfile.NamedTemporaryFile("w", suffix=".toml", encoding="utf-8", delete=False) as stream:
        stream.write(content)
        path = Path(stream.name)
    try:
        return load_config(path)
    finally:
        path.unlink(missing_ok=True)


def pull_request_base_config(root: Path, config_path: str) -> TrustConfig | None:
    if os.environ.get("GITHUB_EVENT_NAME") != "pull_request":
        return None
    event_path = os.environ.get("GITHUB_EVENT_PATH", "")
    if not event_path or not Path(event_path).is_file():
        raise TrustError("pull_request execution requires a readable GITHUB_EVENT_PATH")
    try:
        event = json.loads(Path(event_path).read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        raise TrustError(f"cannot parse GitHub event payload: {error}") from error
    base = event.get("pull_request", {}).get("base", {}).get("sha")
    if not isinstance(base, str) or not base:
        raise TrustError("pull_request event is missing the base commit SHA")
    repository_root = git_root(str(root))
    policy_path = (root / config_path).resolve()
    try:
        relative = policy_path.relative_to(repository_root).as_posix()
    except ValueError as error:
        raise TrustError("Trust configuration must be inside the Git worktree") from error
    result = run(["git", "show", f"{base}:{relative}"], cwd=repository_root, check=False, capture=True)
    if result.returncode != 0:
        # Initial Trust adoption has no policy on the base branch. After adoption,
        # the base policy is authoritative for every pull request.
        return None
    return load_config_text(result.stdout)


def validate_policy_strength(base: TrustConfig, proposed: TrustConfig) -> None:
    if base.strict and not proposed.strict:
        raise TrustError("pull request policy cannot downgrade strict profile")
    if base.lifecycle_command != proposed.lifecycle_command:
        raise TrustError("pull request policy cannot change lifecycle.command")
    if base.contract_enabled and not proposed.contract_enabled:
        raise TrustError("pull request policy cannot disable the contract layer")
    if proposed.effective_contract_coverage < base.effective_contract_coverage:
        raise TrustError("pull request policy cannot reduce contract coverage")
    if RISK_ORDER[proposed.risk_threshold] > RISK_ORDER[base.risk_threshold]:
        raise TrustError("pull request policy cannot weaken the Augur threshold")
    if PROVENANCE_ORDER[proposed.effective_provenance_mode] < PROVENANCE_ORDER[base.effective_provenance_mode]:
        raise TrustError("pull request policy cannot soften provenance")
    if base.provenance_policy != proposed.provenance_policy:
        raise TrustError("pull request policy cannot change the provenance policy path")
    if PROVENANCE_SCOPE_ORDER[proposed.provenance_scope] < PROVENANCE_SCOPE_ORDER[base.provenance_scope]:
        raise TrustError("pull request policy cannot weaken the provenance verification scope")
    if base.atlas_enabled and not proposed.atlas_enabled:
        raise TrustError("pull request policy cannot disable Atlas")


def derive_range(root: Path, explicit: str | None) -> str:
    if explicit:
        return explicit
    upstream = run(["git", "rev-parse", "--abbrev-ref", "@{upstream}"], cwd=root, check=False, capture=True)
    if upstream.returncode == 0 and upstream.stdout.strip():
        return f"{upstream.stdout.strip()}..HEAD"
    raise TrustError("cannot infer a comparison range; pass --range or configure an upstream branch")


def baseline_commit(root: Path, comparison: str) -> str:
    if "..." in comparison:
        left, right = comparison.split("...", 1)
        if not left.strip() or not right.strip():
            raise TrustError("baseline provenance requires two nonempty range endpoints")
        result = run(["git", "merge-base", left.strip(), right.strip()], cwd=root, capture=True)
        return result.stdout.strip()
    if ".." not in comparison:
        raise TrustError("baseline provenance requires a comparison range")
    base = comparison.split("..", 1)[0].strip()
    if not base:
        raise TrustError("baseline provenance requires a nonempty range base")
    result = run(["git", "rev-parse", f"{base}^{{commit}}"], cwd=root, capture=True)
    return result.stdout.strip()


def provenance_target(root: Path, comparison: str, scope: str) -> tuple[str, str]:
    if scope == "baseline":
        return "commit", baseline_commit(root, comparison)
    return "range", comparison


def action_range(
    root: Path,
    explicit: str | None,
    provenance_scope: str,
) -> tuple[str, str, str]:
    if explicit:
        target, value = provenance_target(root, explicit, provenance_scope)
        return explicit, target, value
    event_name = os.environ.get("GITHUB_EVENT_NAME", "")
    event_path = os.environ.get("GITHUB_EVENT_PATH", "")
    event: dict[str, Any] = {}
    if event_path and Path(event_path).is_file():
        try:
            event = json.loads(Path(event_path).read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as error:
            raise TrustError(f"cannot parse GitHub event payload: {error}") from error
    if event_name == "pull_request":
        pull = event.get("pull_request", {})
        base = pull.get("base", {}).get("sha")
        head = pull.get("head", {}).get("sha")
        if base and head:
            comparison = f"{base}..{head}"
            target, value = provenance_target(root, comparison, provenance_scope)
            return comparison, target, value
    if event_name == "push":
        before = str(event.get("before", ""))
        current = str(event.get("after") or os.environ.get("GITHUB_SHA", "HEAD"))
        if before and set(before) != {"0"}:
            comparison = f"{before}..{current}"
            target, value = provenance_target(root, comparison, provenance_scope)
            return comparison, target, value
        empty_tree = run(["git", "hash-object", "-t", "tree", "/dev/null"], cwd=root, capture=True).stdout.strip()
        return f"{empty_tree}..{current}", "commit", current
    comparison = derive_range(root, None)
    target, value = provenance_target(root, comparison, provenance_scope)
    return comparison, target, value


def write_github_outputs(values: dict[str, str]) -> None:
    output_path = os.environ.get("GITHUB_OUTPUT")
    if output_path:
        with Path(output_path).open("a", encoding="utf-8") as stream:
            for key, value in values.items():
                delimiter = f"TRUST_{uuid.uuid4().hex}"
                stream.write(f"{key}<<{delimiter}\n{value}\n{delimiter}\n")
    else:
        for key, value in values.items():
            print(f"{key}={value}")


def action_resolve(arguments: argparse.Namespace) -> int:
    root = Path(arguments.working_directory).resolve()
    committed = load_config(root / arguments.config)
    validate_layer_files(root, committed)
    base = pull_request_base_config(root, arguments.config)
    if base is not None:
        validate_policy_strength(base, committed)
    config = apply_overrides(committed, arguments.profile or None, arguments.threshold or None)
    comparison, attest_target, attest_value = action_range(
        root,
        arguments.range or None,
        config.provenance_scope,
    )
    outputs = {
        "profile": config.profile,
        "strict": str(config.strict).lower(),
        "contract_enabled": str(config.contract_enabled).lower(),
        "contract_coverage": str(config.effective_contract_coverage),
        "risk_threshold": config.risk_threshold,
        "provenance_mode": config.effective_provenance_mode,
        "provenance_scope": config.provenance_scope,
        "provenance_policy": config.provenance_policy,
        "atlas_enabled": str(config.atlas_enabled).lower(),
        "range": comparison,
        "attest_target": attest_target,
        "attest_value": attest_value,
    }
    write_github_outputs(outputs)
    return 0


def status_document(root: Path, config_path: Path) -> tuple[dict[str, Any], bool]:
    errors: list[str] = []
    try:
        config = load_config(config_path)
    except TrustError as error:
        config = None
        errors.append(str(error))
    tool_commands = {
        "fledge": "fledge",
        "specsync": "specsync",
        "augur": "augur",
        "attest": "attest",
        "atlas": "fledge-atlas",
    }
    tools = {name: command_exists(command) for name, command in tool_commands.items()}
    files = {
        "fledge": (root / "fledge.toml").is_file(),
        "workflow": (root / ".github/workflows/trust.yml").is_file(),
        "rules": BEGIN in ((root / "AGENTS.md").read_text(encoding="utf-8") if (root / "AGENTS.md").is_file() else ""),
    }
    if config:
        try:
            validate_fledge((root / "fledge.toml").read_text(encoding="utf-8"))
        except (OSError, TrustError) as error:
            errors.append(str(error))
        try:
            validate_layer_files(root, config)
        except TrustError as error:
            errors.append(str(error))
        required = ["fledge", "augur"]
        if config.contract_enabled:
            required.append("specsync")
        if config.effective_provenance_mode != "off":
            required.append("attest")
        if config.atlas_enabled:
            required.append("atlas")
        for command in required:
            if not tools[command]:
                errors.append(f"required command is not installed: {command}")
    if not files["workflow"]:
        errors.append("missing .github/workflows/trust.yml")
    if not files["rules"]:
        errors.append("missing managed trust rules in AGENTS.md")
    document = {
        "schemaVersion": 1,
        "version": trust_version(),
        "healthy": not errors,
        "profile": config.profile if config else None,
        "tools": tools,
        "files": files,
        "errors": errors,
    }
    return document, not errors


def doctor(arguments: argparse.Namespace) -> int:
    root = git_root(arguments.root)
    document, healthy = status_document(root, root / arguments.config)
    if arguments.json:
        print(json.dumps(document, indent=2, sort_keys=True))
    else:
        print(f"CorvidLabs Trust: {'healthy' if healthy else 'unhealthy'}")
        for error in document["errors"]:
            print(f"  x {error}", file=sys.stderr)
    return 0 if healthy else 1


def status(arguments: argparse.Namespace) -> int:
    root = git_root(arguments.root)
    document, _ = status_document(root, root / arguments.config)
    if arguments.json:
        print(json.dumps(document, indent=2, sort_keys=True))
    else:
        print(f"CorvidLabs Trust: {'healthy' if document['healthy'] else 'unhealthy'}")
        for error in document["errors"]:
            print(f"  x {error}")
    return 0


def action_lifecycle(arguments: argparse.Namespace) -> int:
    root = Path(arguments.working_directory).resolve()
    config = load_config(root / arguments.config)
    run(config.lifecycle_command, cwd=root)
    return 0


def fetch_notes(root: Path, mode: str) -> None:
    remote = run(["git", "remote", "get-url", "origin"], cwd=root, check=False, capture=True)
    if remote.returncode != 0:
        if mode == "soft":
            print("provenance degraded: no origin remote")
            return
        raise TrustError("provenance is enforced but origin remote is unavailable")
    lookup = run(["git", "ls-remote", "origin", "refs/notes/attest"], cwd=root, check=False, capture=True)
    if lookup.returncode != 0:
        raise TrustError(f"cannot inspect remote provenance ledger: {(lookup.stderr or '').strip()}")
    if not lookup.stdout.strip():
        if mode == "soft":
            print("provenance degraded: remote ledger does not exist yet")
            return
        raise TrustError("provenance is enforced but remote ledger does not exist")
    run(["git", "fetch", "origin", "+refs/notes/attest:refs/notes/attest"], cwd=root)


def verify(arguments: argparse.Namespace) -> int:
    root = git_root(arguments.root)
    config = apply_overrides(load_config(root / arguments.config), arguments.profile, arguments.threshold)
    validate_layer_files(root, config)
    comparison = derive_range(root, arguments.range)
    print(f"trust range: {comparison}")
    print("== lifecycle ==")
    run(config.lifecycle_command, cwd=root)
    if config.contract_enabled:
        if not (root / ".specsync/config.toml").is_file():
            raise TrustError("contract is enabled but .specsync/config.toml is missing")
        command = ["specsync", "check"]
        if config.effective_contract_coverage:
            command += ["--require-coverage", str(config.effective_contract_coverage)]
        print("== contract ==")
        run(command, cwd=root)
    else:
        print(f"== contract: off ({config.contract_skip_reason}) ==")
    print("== risk ==")
    run(["augur", "gate", "--range", comparison, "--threshold", config.risk_threshold], cwd=root)
    mode = config.effective_provenance_mode
    if mode == "off":
        print(f"== provenance: off ({config.provenance_skip_reason}) ==")
    else:
        policy = root / config.provenance_policy
        if not policy.is_file():
            raise TrustError(f"provenance policy is missing: {config.provenance_policy}")
        fetch_notes(root, mode)
        print("== provenance ==")
        target, value = provenance_target(root, comparison, config.provenance_scope)
        result = run(
            ["attest", "verify", f"--{target}", value, "--policy", str(policy), "--json"],
            cwd=root,
            check=False,
            capture=True,
        )
        try:
            report = json.loads(result.stdout or "")
        except json.JSONDecodeError as error:
            detail = (result.stderr or result.stdout or "no verification report").strip()
            raise TrustError(f"Attest execution failed: {detail}") from error
        if not isinstance(report, dict) or not isinstance(report.get("passed"), bool):
            raise TrustError("Attest execution failed: malformed verification report")
        satisfied = result.returncode == 0 and report["passed"] is True
        unsatisfied = (
            result.returncode != 0
            and report["passed"] is False
            and isinstance(report.get("violations"), list)
        )
        if not satisfied and not unsatisfied:
            raise TrustError("Attest execution failed: report and exit status disagree")
        if unsatisfied:
            if mode == "soft":
                print("provenance degraded: policy is not satisfied")
            else:
                raise TrustError("provenance policy is not satisfied")
    if config.atlas_enabled:
        print("== atlas ==")
        result = run(["fledge-atlas", str(root), "--json"], cwd=root, capture=True)
        try:
            atlas = json.loads(result.stdout or "")
        except json.JSONDecodeError as error:
            raise TrustError("Atlas execution failed: malformed JSON report") from error
        verdict = atlas.get("verdict") if isinstance(atlas, dict) else None
        if not isinstance(verdict, str) or not verdict:
            raise TrustError("Atlas execution failed: report is missing verdict")
        print(f"atlas: {verdict}")
    else:
        print(f"== atlas: off ({config.atlas_skip_reason}) ==")
    print("trust gate passed" if mode != "soft" else "trust gate passed (progressive provenance)")
    return 0


def parser() -> argparse.ArgumentParser:
    root_parser = argparse.ArgumentParser(
        prog="fledge trust",
        description="One gate for contracts, verification, risk, and provenance",
    )
    root_parser.add_argument("--version", action="version", version=f"%(prog)s {trust_version()}")
    commands = root_parser.add_subparsers(dest="command", required=True)
    adopt_parser = commands.add_parser("adopt", help="Add Trust to a repository")
    adopt_parser.add_argument("--root")
    adopt_parser.add_argument("--profile", choices=("standard", "strict"), default="standard")
    adopt_parser.add_argument("--dry-run", action="store_true")
    adopt_parser.add_argument("--force", action="store_true")
    adopt_parser.add_argument("--no-specs", metavar="REASON")
    adopt_parser.add_argument("--no-attest", metavar="REASON")
    atlas_group = adopt_parser.add_mutually_exclusive_group()
    atlas_group.add_argument("--atlas", action="store_true", help="Enable Atlas publication")
    atlas_group.add_argument("--no-atlas", metavar="REASON", help="Record a custom reason for leaving Atlas disabled")
    adopt_parser.set_defaults(handler=adopt)
    for name in ("status", "doctor"):
        command_parser = commands.add_parser(name, help=f"{name.title()} Trust configuration")
        command_parser.add_argument("--root")
        command_parser.add_argument("--config", default=".trust.toml")
        command_parser.add_argument("--json", action="store_true")
        command_parser.set_defaults(handler=status if name == "status" else doctor)
    verify_parser = commands.add_parser("verify", help="Run the Trust gate")
    verify_parser.add_argument("--root")
    verify_parser.add_argument("--config", default=".trust.toml")
    verify_parser.add_argument("--range")
    verify_parser.add_argument("--profile", choices=("standard", "strict"))
    verify_parser.add_argument("--threshold", choices=("proceed", "review", "block"))
    verify_parser.set_defaults(handler=verify)
    action_parser = commands.add_parser("action-resolve", help=argparse.SUPPRESS)
    action_parser.add_argument("--working-directory", default=".")
    action_parser.add_argument("--config", default=".trust.toml")
    action_parser.add_argument("--range", default="")
    action_parser.add_argument("--profile", default="")
    action_parser.add_argument("--threshold", default="")
    action_parser.set_defaults(handler=action_resolve)
    lifecycle_parser = commands.add_parser("action-lifecycle", help=argparse.SUPPRESS)
    lifecycle_parser.add_argument("--working-directory", default=".")
    lifecycle_parser.add_argument("--config", default=".trust.toml")
    lifecycle_parser.set_defaults(handler=action_lifecycle)
    return root_parser


def main() -> int:
    try:
        arguments = parser().parse_args()
        return int(arguments.handler(arguments))
    except TrustError as error:
        print(f"fledge trust: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
