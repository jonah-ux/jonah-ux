#!/usr/bin/env python3
"""Validate the public review lock and packet without third-party dependencies."""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
LOCK_PATH = ROOT / "docs" / "AGENT-SYSTEMS-LAB-REVIEW-LOCK.json"
PACKET_PATH = ROOT / "docs" / "EXTERNAL-REVIEW-PACKET.md"
SCHEMA = "agent-systems-lab/review-validation/v1"
SHA = re.compile(r"^[0-9a-f]{40}$")
SHA256 = re.compile(r"^[0-9a-f]{64}$")
OWNER = re.compile(r"^[a-z0-9][a-z0-9-]{0,99}$")
REPOSITORY = re.compile(r"^jonah-ux/[a-z0-9][a-z0-9-]{0,99}$")
VERSION = re.compile(r"^[0-9]+\.[0-9]+\.[0-9]+$")
ARTIFACT_NAME = re.compile(r"^[A-Za-z0-9][A-Za-z0-9_.+-]*$")
PACKET_OWNER = re.compile(
    r"^\|\s*\[[^\]\r\n]+\]\(https://github\.com/"
    r"(jonah-ux/[a-z0-9-]+)\)\s*\|\s*`([0-9a-f]{40})`\s*\|",
    re.MULTILINE,
)
MAX_INPUT_BYTES = 1024 * 1024
LIMITS = [
    "this validator checks profile source and packet consistency only",
    "recorded artifact metadata is checked; "
    "artifact bytes and installs are not replayed",
    "it does not fetch owner repositories or establish deployment, adoption, "
    "or production outcomes",
]


def _matches(pattern: re.Pattern[str], value: Any) -> bool:
    return isinstance(value, str) and pattern.fullmatch(value) is not None


def _git_head() -> str:
    result = subprocess.run(
        ["git", "rev-parse", "HEAD"],
        cwd=ROOT,
        check=False,
        capture_output=True,
        text=True,
        timeout=5,
    )
    value = result.stdout.strip()
    if result.returncode or not SHA.fullmatch(value):
        raise ValueError("current_git_head_unavailable")
    return value


def _read_text(path: Path) -> str:
    if path.is_symlink() or path.parent.is_symlink():
        raise ValueError("symlink_input")
    if not path.is_file():
        raise ValueError("invalid_input")
    with path.open("rb") as source:
        raw = source.read(MAX_INPUT_BYTES + 1)
    if len(raw) > MAX_INPUT_BYTES:
        raise ValueError("input_too_large")
    return raw.decode("utf-8")


def _unique_keys(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("duplicate_json_key")
        result[key] = value
    return result


def _load() -> tuple[Any, str]:
    lock = json.loads(_read_text(LOCK_PATH), object_pairs_hook=_unique_keys)
    packet = _read_text(PACKET_PATH)
    return lock, packet


def _artifact_errors(artifact: Any, owner: str, packet: str) -> list[str]:
    if not isinstance(artifact, dict) or artifact.get("state") != "verified":
        return ["artifact_not_verified"]

    errors: list[str] = []
    digests = [artifact.get("checksum_manifest_sha256")]
    if owner == "slipstream":
        digests.append(artifact.get("artifact_sha256"))
        if not _matches(VERSION, str(artifact.get("release", "")).removeprefix("v")):
            errors.append("artifact_version_invalid")
        runtime = artifact.get("consumer_node")
        if (
            not isinstance(runtime, str)
            or not _matches(VERSION, runtime.removeprefix("v"))
            or artifact.get("consumer_self_test") != "pass"
        ):
            errors.append("artifact_consumer_not_verified")
    else:
        assets = artifact.get("artifacts")
        assets = assets if isinstance(assets, list) else []
        names = [item.get("name") for item in assets if isinstance(item, dict)]
        valid_names = all(_matches(ARTIFACT_NAME, name) for name in names)
        if (
            len(assets) != 2
            or len(names) != 2
            or not valid_names
            or len(set(names)) != 2
            or sum(name.endswith(".whl") for name in names) != 1
            or sum(name.endswith(".tar.gz") for name in names) != 1
        ):
            errors.append("artifact_set_invalid")
        digests.extend(
            item.get("sha256") if isinstance(item, dict) else None for item in assets
        )
        if not _matches(VERSION, artifact.get("package_version")):
            errors.append("artifact_version_invalid")
        if artifact.get("local_build") != "pass":
            errors.append("artifact_build_not_verified")
        if not _matches(VERSION, artifact.get("consumer_python")):
            errors.append("artifact_consumer_not_verified")

    if not all(_matches(SHA256, digest) for digest in digests):
        errors.append("artifact_digest_invalid")
    elif any(digest not in packet for digest in digests):
        errors.append("artifact_digest_missing_from_packet")
    if artifact.get("local_packed_audit") != "pass":
        errors.append("artifact_audit_not_verified")
    if artifact.get("consumer_install") != "pass":
        errors.append("artifact_consumer_not_verified")
    for field in (
        "consumer_cli_help",
        "consumer_check_help",
        "consumer_demo_help",
        "consumer_demo",
    ):
        if field in artifact and artifact[field] != "pass":
            errors.append("artifact_consumer_not_verified")
    if "consumer_demo" in artifact and (
        artifact.get("consumer_demo_reviewable") is not True
        or not _matches(SHA256, artifact.get("consumer_demo_record_sha256"))
        or artifact["consumer_demo_record_sha256"] not in packet
    ):
        errors.append("artifact_demo_not_verified")
    return list(dict.fromkeys(errors))


def validate(expected_published_head: str | None = None) -> dict[str, Any]:
    errors: list[str] = []
    try:
        lock, packet = _load()
    except UnicodeDecodeError:
        return {
            "schema": SCHEMA,
            "result": "blocked",
            "errors": ["load_failed:invalid_utf8"],
        }
    except (OSError, json.JSONDecodeError, ValueError, RecursionError) as exc:
        code = str(exc) if type(exc) is ValueError else "invalid_input"
        if code not in {"duplicate_json_key", "input_too_large", "symlink_input"}:
            code = "invalid_input"
        return {
            "schema": SCHEMA,
            "result": "blocked",
            "errors": [f"load_failed:{code}"],
        }
    if not isinstance(lock, dict):
        return {
            "schema": SCHEMA,
            "result": "blocked",
            "errors": ["lock_not_object"],
        }

    if lock.get("schema") != "agent-systems-lab-review-lock/v1":
        errors.append("lock_schema_invalid")
    owners = lock.get("owners")
    if not isinstance(owners, list) or len(owners) != 13:
        errors.append("owner_count_must_equal_13")
        owners = owners if isinstance(owners, list) else []

    repositories = [
        owner["repository"]
        for owner in owners
        if isinstance(owner, dict) and _matches(REPOSITORY, owner.get("repository"))
    ]
    heads = [
        owner["source_head"]
        for owner in owners
        if isinstance(owner, dict) and _matches(SHA, owner.get("source_head"))
    ]
    if len(set(repositories)) != len(repositories):
        errors.append("owner_repositories_not_unique")
    if len(set(heads)) != len(heads):
        errors.append("owner_source_heads_not_unique")

    packet_heads: dict[str, str] = {}
    for repository, head in PACKET_OWNER.findall(packet):
        if repository in packet_heads:
            errors.append("packet_owner_rows_not_unique")
        packet_heads[repository] = head
    if set(packet_heads) != set(repositories):
        errors.append("packet_owner_set_does_not_match_lock")

    verified_artifacts = 0
    for index, owner in enumerate(owners):
        if not isinstance(owner, dict):
            errors.append("owner_entry_not_object")
            continue
        repository = owner.get("repository")
        label = repository if _matches(REPOSITORY, repository) else f"owner_{index}"
        if not _matches(REPOSITORY, repository):
            errors.append(f"owner_repository_invalid:{label}")
        owner_id = owner.get("owner")
        if not _matches(OWNER, owner_id):
            errors.append(f"owner_id_invalid:{label}")
        elif repository != f"jonah-ux/{owner_id}":
            errors.append(f"owner_repository_mismatch:{label}")
        if owner.get("audit_state") != "verified-at-head":
            errors.append(f"audit_not_verified:{label}")
        source_head = owner.get("source_head")
        if not _matches(SHA, source_head):
            errors.append(f"source_head_invalid:{label}")
        if isinstance(source_head, str) and source_head not in packet:
            errors.append(f"source_head_missing_from_packet:{label}")
        if (
            _matches(REPOSITORY, repository)
            and packet_heads.get(repository) != source_head
        ):
            errors.append(f"source_head_does_not_match_packet:{label}")
        artifact_errors = _artifact_errors(owner.get("artifact"), owner_id, packet)
        if artifact_errors:
            errors.extend(f"{code}:{label}" for code in artifact_errors)
        else:
            verified_artifacts += 1

    profile = lock.get("profile")
    if not isinstance(profile, dict):
        errors.append("profile_block_missing")
        profile = {}
    for field in ("snapshot_base_head", "lock_published_head"):
        if not _matches(SHA, profile.get(field)):
            errors.append(f"profile_{field}_invalid")
    if profile.get("repository") != "jonah-ux/jonah-ux":
        errors.append("profile_repository_invalid")
    packet_bases = re.findall(r"profile base head\s+`([0-9a-f]{40})`", packet)
    if packet_bases != [profile.get("snapshot_base_head")]:
        errors.append("profile_snapshot_base_missing_from_packet")
    if expected_published_head is not None:
        if not _matches(SHA, expected_published_head):
            errors.append("expected_published_head_invalid")
        elif profile.get("lock_published_head") != expected_published_head:
            errors.append("lock_published_head_does_not_match_expected_parent")

    review_route = lock.get("review_route")
    if not isinstance(review_route, dict):
        errors.append("review_route_missing")
    else:
        if review_route.get("outside_review") != "not_requested":
            errors.append("outside_review_state_changed")
        if review_route.get("adoption") != "unknown":
            errors.append("adoption_state_changed")
    if "synthetic fixtures" not in packet.lower():
        errors.append("packet_synthetic_boundary_missing")
    if "outside adoption" not in packet.lower():
        errors.append("packet_adoption_limit_missing")

    revision = None
    try:
        revision = _git_head()
    except (OSError, ValueError, subprocess.TimeoutExpired):
        errors.append("current_git_head_unavailable")

    public_profile = {}
    if profile.get("repository") == "jonah-ux/jonah-ux":
        public_profile["repository"] = profile["repository"]
    for field in ("snapshot_base_head", "lock_published_head"):
        if _matches(SHA, profile.get(field)):
            public_profile[field] = profile[field]

    return {
        "schema": SCHEMA,
        "result": "pass" if not errors else "blocked",
        "source": {"revision": revision},
        "owners": len(owners),
        "verified_artifacts": verified_artifacts,
        "profile": public_profile,
        "errors": errors,
        "limits": LIMITS,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--published-head",
        help="expected containing profile parent commit; on a PR this is the base head",
    )
    parser.add_argument("--json", action="store_true", help="emit formatted JSON")
    args = parser.parse_args(argv)
    report = validate(args.published_head)
    print(json.dumps(report, indent=2 if args.json else None, sort_keys=True))
    return 0 if report["result"] == "pass" else 2


if __name__ == "__main__":
    sys.exit(main())
