#!/usr/bin/env python3
"""Read-only secret scanning of every reachable blob in public Git repositories.

Report finding locations and categories, never credential values.
"""
from __future__ import annotations

import argparse
from collections import Counter
from io import BytesIO
import json
import math
from pathlib import Path
import re
import subprocess
import sys
import tempfile
from urllib.parse import quote
from urllib.request import Request, urlopen

MAX_BLOB_BYTES = 1024 * 1024
BATCH_SIZE = 64
PROVIDER_PATTERNS = (
    ("private_key", re.compile(rb"-----BEGIN (?:RSA |EC |OPENSSH |DSA )?PRIVATE KEY-----")),
    ("github_token", re.compile(rb"\b(?:gh[pousr]_[A-Za-z0-9_]{20,}|github_pat_[A-Za-z0-9_]{20,})\b")),
    ("openai_key", re.compile(rb"\bsk-(?:proj-)?[A-Za-z0-9_-]{20,}\b")),
    ("aws_access_key", re.compile(rb"\b(?:AKIA|ASIA)[0-9A-Z]{16}\b")),
    ("google_api_key", re.compile(rb"\bAIza[0-9A-Za-z_-]{20,}\b")),
    ("google_oauth_secret", re.compile(rb"\bGOCSPX-[A-Za-z0-9_-]{20,}\b")),
    ("slack_token", re.compile(rb"\bxox[baprs]-[A-Za-z0-9-]{20,}\b")),
    ("stripe_secret", re.compile(rb"\b(?:sk_live|rk_live)_[A-Za-z0-9]{20,}\b")),
    ("sendgrid_key", re.compile(rb"\bSG\.[A-Za-z0-9_-]{20,}\.[A-Za-z0-9_-]{20,}\b")),
    ("twilio_api_key", re.compile(rb"\bSK[0-9a-fA-F]{32}\b")),
)
ASSIGNMENT = re.compile(
    rb"""(?ix)
    \b(?:client_secret|refresh_token|access_token|api_key|apikey|
         secret_access_key|oauth_token|service_role_key)
    \b\s*["']?\s*[:=]\s*["']?
    (?P<value>[A-Za-z0-9._~+/\-]{24,})
    """
)
REPOSITORY_NAME = re.compile(r"^[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+$")
PLACEHOLDER = re.compile(rb"(?i)(placeholder|replace[_-]?me|your[_-]|example|process\.env|changeme|dummy|fake[_-])")


def entropy(value: bytes) -> float:
    frequencies = Counter(value)
    return -sum((count / len(value)) * math.log2(count / len(value)) for count in frequencies.values())


def scan_blob(data: bytes, path: str, blob_sha: str) -> list[dict[str, object]]:
    if b"\0" in data[:4096]:
        return []
    findings = []
    for line_number, line in enumerate(data.splitlines(), start=1):
        kinds = {name for name, pattern in PROVIDER_PATTERNS if pattern.search(line)}
        for match in ASSIGNMENT.finditer(line):
            secret = match.group("value")
            if not PLACEHOLDER.search(secret) and len(set(secret)) >= 8 and entropy(secret) >= 3.2:
                kinds.add("assigned_secret")
        for kind in sorted(kinds):
            findings.append({"path": path, "line": line_number, "blob": blob_sha[:12], "kind": kind})
    return findings


def run_git(repo: Path, *args: str, input_data: bytes | None = None) -> bytes:
    result = subprocess.run(
        ["git", "-C", str(repo), *args],
        input=input_data, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
        check=True, timeout=180,
    )
    return result.stdout


def scan_repository(name: str, repo: Path) -> dict[str, object]:
    """Scan unique blob objects reachable from all available Git refs."""
    objects = run_git(repo, "rev-list", "--objects", "--all").decode("utf-8", "replace").splitlines()
    paths = {}
    for row in objects:
        oid, _, path = row.partition(" ")
        if path and re.fullmatch(r"[0-9a-f]{40,64}", oid):
            paths.setdefault(oid, path)
    if not paths:
        raise RuntimeError("no named reachable Git objects")
    sizes = run_git(
        repo, "cat-file", "--batch-check=%(objectname) %(objecttype) %(objectsize)",
        input_data=("".join(oid + "\n" for oid in paths)).encode(),
    ).decode().splitlines()
    blobs = []
    skipped_large = 0
    for row in sizes:
        oid, kind, size_str = row.split()
        if kind != "blob":
            continue
        if int(size_str) > MAX_BLOB_BYTES:
            skipped_large += 1
        else:
            blobs.append((oid, paths[oid]))
    findings = []
    for offset in range(0, len(blobs), BATCH_SIZE):
        chunk = blobs[offset:offset + BATCH_SIZE]
        payload = run_git(repo, "cat-file", "--batch",
                          input_data=("".join(oid + "\n" for oid, _ in chunk)).encode())
        stream = BytesIO(payload)
        for oid, path in chunk:
            header = stream.readline().decode("ascii").strip().split()
            if len(header) != 3 or header[0] != oid or header[1] != "blob":
                raise RuntimeError("invalid Git object stream (scan incomplete)")
            size = int(header[2])
            content = stream.read(size)
            if len(content) != size or stream.read(1) != b"\n":
                raise RuntimeError("truncated Git blob stream (scan incomplete)")
            findings.extend({"repository": name, **finding}
                            for finding in scan_blob(content, path, oid))
    return {"repository": name, "blobs_scanned": len(blobs),
            "skipped_large_blobs": skipped_large, "findings": findings}


def select_repositories(entries: list[dict[str, object]]) -> list[str]:
    return sorted(
        entry["full_name"] for entry in entries
        if not entry.get("private") and not entry.get("fork") and not entry.get("archived")
        and isinstance(entry.get("full_name"), str)
        and REPOSITORY_NAME.fullmatch(entry["full_name"])
    )


def public_repositories(owner: str) -> list[str]:
    entries = []
    for page in range(1, 12):
        url = f"https://api.github.com/users/{quote(owner)}/repos?type=public&per_page=100&page={page}"
        request = Request(url, headers={"Accept": "application/vnd.github+json",
                                        "User-Agent": "public-repo-secret-history-audit"})
        with urlopen(request, timeout=30) as response:
            batch = json.load(response)
        if not isinstance(batch, list):
            raise RuntimeError("GitHub API did not return a repository list")
        entries.extend(batch)
        if len(batch) < 100:
            break
    else:
        raise RuntimeError("repository discovery exceeded page bound")
    repos = select_repositories(entries)
    if not repos:
        raise RuntimeError("No public original repositories discovered; refuse empty audit")
    return [name for name in repos if name.split("/")[0].lower() == owner.lower()]


def mirror_repository(name: str, destination: Path) -> None:
    if not REPOSITORY_NAME.fullmatch(name):
        raise ValueError("invalid repository name")
    url = f"https://github.com/{name}.git"
    subprocess.run(["git", "clone", "--mirror", "--quiet", "--", url, str(destination)],
                   stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True, timeout=240)
    # Unmerged public pull-request heads can contain credentials too.
    pull_heads = run_git(destination, "ls-remote", "origin", "refs/pull/*/head")
    if pull_heads.strip():
        run_git(destination, "fetch", "--quiet", "--no-tags", "origin",
                "+refs/pull/*/head:refs/audit/pull/*")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--owner", default="jonah-ux")
    args = parser.parse_args()
    if not re.fullmatch(r"[A-Za-z0-9-]+", args.owner):
        parser.error("invalid owner")
    report = {"owner": args.owner, "repositories_scanned": 0,
              "blobs_scanned": 0, "skipped_large_blobs": 0, "findings": [], "errors": []}
    try:
        repos = public_repositories(args.owner)
        for name in repos:
            print(f"Scanning historical Git objects: {name}", file=sys.stderr)
            try:
                with tempfile.TemporaryDirectory(prefix="public-secret-audit-") as workdir:
                    mirror = Path(workdir) / "repo.git"
                    mirror_repository(name, mirror)
                    result = scan_repository(name, mirror)
                    report["repositories_scanned"] += 1
                    report["blobs_scanned"] += result["blobs_scanned"]
                    report["skipped_large_blobs"] += result["skipped_large_blobs"]
                    report["findings"].extend(result["findings"])
            except (OSError, RuntimeError, subprocess.SubprocessError, ValueError) as exc:
                # External command stderr may contain untrusted content; never echo it.
                report["errors"].append({"repository": name, "failure_class": type(exc).__name__})
    except (OSError, RuntimeError, ValueError) as exc:
        report["errors"].append({"repository": "discovery", "failure_class": type(exc).__name__})
    report["findings"].sort(key=lambda x: (x["repository"], x["path"], x["line"], x["kind"]))
    print(json.dumps(report, indent=2))
    if report["errors"] or report["findings"]:
        return 1
    if report["skipped_large_blobs"]:
        print("Large blobs were skipped; results are partial. Review the JSON counters.", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
