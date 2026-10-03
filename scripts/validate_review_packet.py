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


def _git_head() -> str:
    result = subprocess.run(
        ["git", "rev-parse", "HEAD"], cwd=ROOT, check=False, capture_output=True, text=True
    )
    value = result.stdout.strip()
    if result.returncode or not SHA.fullmatch(value):
        raise ValueError("current_git_head_unavailable")
    return value


def _load() -> tuple[dict[str, Any], str]:
    lock = json.loads(LOCK_PATH.read_text(encoding="utf-8"))
    packet = PACKET_PATH.read_text(encoding="utf-8")
    return lock, packet


def validate(expected_published_head: str | None = None) -> dict[str, Any]:
    errors: list[str] = []
    try:
        lock, packet = _load()
    except (OSError, json.JSONDecodeError) as exc:
        return {"schema": SCHEMA, "result": "blocked", "errors": [f"load_failed:{exc}"]}

    if lock.get("schema") != "agent-systems-lab-review-lock/v1":
        errors.append("lock_schema_invalid")
    owners = lock.get("owners")
    if not isinstance(owners, list) or len(owners) != 13:
        errors.append("owner_count_must_equal_13")
        owners = owners if isinstance(owners, list) else []

    repositories = [owner.get("repository") for owner in owners if isinstance(owner, dict)]
    heads = [owner.get("source_head") for owner in owners if isinstance(owner, dict)]
    if len(set(repositories)) != len(repositories):
        errors.append("owner_repositories_not_unique")
    if len(set(heads)) != len(heads):
        errors.append("owner_source_heads_not_unique")

    verified_artifacts = 0
    for owner in owners:
        if not isinstance(owner, dict):
            errors.append("owner_entry_not_object")
            continue
        if owner.get("audit_state") != "verified-at-head":
            errors.append(f"audit_not_verified:{owner.get('repository')}")
        source_head = owner.get("source_head")
        if not isinstance(source_head, str) or not SHA.fullmatch(source_head):
            errors.append(f"source_head_invalid:{owner.get('repository')}")
        if isinstance(source_head, str) and source_head not in packet:
            errors.append(f"source_head_missing_from_packet:{owner.get('repository')}")
        artifact = owner.get("artifact")
        if not isinstance(artifact, dict) or artifact.get("state") != "verified":
            errors.append(f"artifact_not_verified:{owner.get('repository')}")
        else:
            verified_artifacts += 1

    profile = lock.get("profile")
    if not isinstance(profile, dict):
        errors.append("profile_block_missing")
        profile = {}
    for field in ("snapshot_base_head", "lock_published_head"):
        if not isinstance(profile.get(field), str) or not SHA.fullmatch(profile[field]):
            errors.append(f"profile_{field}_invalid")
    if expected_published_head is not None:
        if not SHA.fullmatch(expected_published_head):
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

    return {
        "schema": SCHEMA,
        "result": "pass" if not errors else "blocked",
        "source": {"revision": _git_head()},
        "owners": len(owners),
        "verified_artifacts": verified_artifacts,
        "profile": profile,
        "errors": errors,
        "limits": [
            "this validator checks profile source and packet consistency only",
            "it does not fetch owner repositories or establish deployment, adoption, or production outcomes",
        ],
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
