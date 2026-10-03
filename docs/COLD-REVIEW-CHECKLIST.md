# Agent Systems Lab cold-review checklist

This is the shortest reproducible review path for an engineer who starts with
Jonah's GitHub profile and has no access to private systems. It is deliberately
written as an evidence checklist: a green command proves only the boundary named
next to it.

## 1. Start at the profile

Read the [profile README](../README.md), then open the
[Agent Systems Lab architecture](AGENT-SYSTEMS-LAB-ARCHITECTURE.md). Confirm that
each capability has one public owner and that the profile distinguishes standalone
installation, current main, tagged releases, hosted fixtures, and production
outcomes.

## 2. Run one repository by itself

Forgeyard is the shortest entry point because it has both a local CLI and a hosted
Workbench:

```bash
git clone https://github.com/jonah-ux/forgeyard.git
cd forgeyard
python3 -m venv .venv
. .venv/bin/activate
python -m pip install -e .
forgeyard demo
```

The demo should print a `forgeyard-demo/v1` document with a reviewable record and
packet. That proves the package's local evidence path; it does not prove a merge,
deployment, or production result.

## 3. Run the integrated local flow

The reference harness uses only checked-in synthetic reports and calls the public
Forgeyard CLI:

```bash
python scripts/run_reference_flow.py --scenario passing
python scripts/run_reference_flow.py --scenario blocked
python scripts/run_reference_flow.py --scenario tampered
```

Expected outcomes are `reviewable`, `blocked`, and `refused`, respectively. The
script returns zero when each expected outcome is observed, so the result field and
the nested compose/verification exits must be read together.

Then run the fixed-dataset lab benchmark:

```bash
python scripts/benchmark_lab.py --iterations 20 --warmup 3 --json
```

Check for `forgeyard-lab-benchmark/v1`, nine reports, six operation names
(`parse`, `validate`, `index`, `replay`, `compose`, `packet_verify`),
`packet_ok: true`, and `private_payloads_exported: false`. Timings are machine-local
observations, not cross-machine rankings.

## 4. Inspect the hosted refusal surface

Open the [Forgeyard Workbench](https://jonah-ux.github.io/forgeyard/), choose
**Load adversarial matrix**, and compose the record. The current matrix has fifteen
classified refusal reports covering stale source, capability denial, unenforced
execution, partial and malformed input, unknown lifecycle, tampered bytes, path
traversal, symlink escape, prompt/secret leakage, schema drift, duplicate delivery,
stale source identity, unbounded output, and false completion.

The expected visible state is `15` specialists, `BLOCKED` decision, and `SEALED`
integrity. The checked-in artifact is [adversarial.json](https://github.com/jonah-ux/forgeyard/blob/main/docs/workbench/fixtures/adversarial.json);
the CLI and provenance contracts remain authoritative for real records.

## 5. Follow the owner boundaries

| Question | Owner to inspect | Boundary to preserve |
| --- | --- | --- |
| Is context fresh and in scope? | [Context Integrity Lab](https://github.com/jonah-ux/context-integrity-lab) | Refusal and unknown states stay explicit. |
| Is a trace portable and redacted? | [ChatLens](https://github.com/jonah-ux/chatlens) and [Agent Trace Lite](https://github.com/jonah-ux/agent-trace-lite) | Raw transcript stores do not become public evidence. |
| Is a capability allowed? | [Agent Policy](https://github.com/jonah-ux/agent-policy) and [MCP Doctor](https://github.com/jonah-ux/mcp-doctor) | Unknown contracts and default-deny decisions fail closed. |
| Was execution bounded? | [Agent Sandbox Run](https://github.com/jonah-ux/agent-sandbox-run) and [Atlas](https://github.com/jonah-ux/atlas-agent-runtime) | A receipt reports enforcement and lifecycle state rather than implying security. |
| Can the result be continued and proved? | [Agent Resume](https://github.com/jonah-ux/agent-resume) and [Agent Proof](https://github.com/jonah-ux/agent-proof) | Digests, source identity, and unknowns remain loss-aware. |
| Is delivery reviewable? | [Forgeyard](https://github.com/jonah-ux/forgeyard) and [Worktree Conservator](https://github.com/jonah-ux/worktree-conservator) | Review readiness is separate from merge, deployment, and recovery. |

## 6. Keep the claims straight

- A current-main source readback proves what the repository contains now; it is not
  a tagged release.
- A tagged wheel or source archive plus checksum and fresh consumer proves artifact
  usability for that release; it is not proof of outside adoption.
- A Pages readback proves the synthetic browser fixture is reachable and behaving;
  it is not proof of a hosted production service.
- A benchmark receipt proves the named local operations ran on the named dataset;
  it is not a model-quality, provider-latency, security, or deployment benchmark.
- Stars, forks, downloads, and a local run are observations. External adoption stays
  unknown until an independent consumer or contributor is directly observed.

The public lab intentionally contains no Auto Shop Media source, customer data,
credentials, private paths, transcripts, production logs, or proprietary operating
policy.

## 7. Run the supply-chain and privacy checks

These checks are deliberately separate from the functional demos. A passing command proves only
the named boundary; a missing tool or provider-side control stays `unavailable`.

### Release and dependency provenance

For each released package under review, read the tag, target commit, assets, and checksums from the
repository release page, then verify the downloaded files before installation:

```bash
gh release view TAG --repo OWNER/REPO --json tagName,targetCommitish,assets
sha256sum PACKAGE.whl PACKAGE.tar.gz
python -m pip install --no-index --no-deps PACKAGE.whl
python -m pip check
```

Record the package version, tag, target commit, asset names, and checksum as one observation. A
successful local install does not prove that the package was built reproducibly or that a future
release will carry the same dependencies.

Check the source boundary directly:

```bash
test -f LICENSE
test -f SECURITY.md
python - <<'PY'
import pathlib, tomllib
data = tomllib.loads(pathlib.Path("pyproject.toml").read_text())
print(data.get("project", {}).get("dependencies", []))
PY
```

The current public Python owners use standard-library runtime dependencies in their reviewed
packages. This command records the actual project metadata; it is not a substitute for a complete
license audit or a platform-attested build provenance record.

The four flagship owners also expose a bounded, owner-native public audit. Run it from each clean
checkout and keep the receipt with the source head:

```bash
python scripts/audit_public_surface.py --json
```

Use this command in Forgeyard, Agent Proof, Atlas Agent Runtime, and ChatLens. A static `pass`
means the named dependency, license, release-marker, and high-signal privacy checks passed. An
artifact result of `unavailable` is expected when no `--dist-dir` was supplied. The audits do not
claim complete DLP, security certification, reproducible builds across machines, deployment,
adoption, or production readiness.

### Secret, private-path, and synthetic-data scan

Run the scan from the repository root and inspect every match. The patterns are intentionally
conservative; a fixture that contains a documented synthetic marker must be classified rather than
silently ignored:

```bash
rg -n --hidden --glob '!.git/**' \
  '-----BEGIN (RSA|OPENSSH|EC|PGP) PRIVATE KEY-----|sk-[A-Za-z0-9]{20,}|ghp_[A-Za-z0-9]{20,}|/Users/|/home/|jonahsnorthstar|customer|EIN|api[_-]?key' .
```

The expected outcome for a public fixture tree is zero unclassified hits. A clean search is not a
secret-scanning service and does not prove that a provider-side history is clean. Keep transcript
text, credentials, customer records, private paths, and employer policy outside checked-in examples.

### Hostile-input and confused-deputy review

Use the existing owner tests and receipts rather than creating a second security harness:

- Forgeyard `forgeyard-evaluation/v1` covers fifteen refusal mutations, including traversal,
  symlink escape, prompt/secret leakage, schema drift, duplicate delivery, stale identity,
  unbounded output, and false completion.
- Agent Proof `verify-graph --input` must refuse a changed edge and a resealed orphan edge.
- Agent Policy must preserve default-deny and its versioned `agent-policy/receipt/v1` boundary.
- Agent Sandbox Run must keep `agent-sandbox/v2` backend and enforcement disclosure explicit; a
  fallback receipt is evidence of fallback, not proof of isolation.
- Worktree Conservator must leave real worktrees untouched during disposable conformance runs.

Record the exact command, source head, receipt, and refusal result. A green fixture test proves the
fixture boundary; it does not prove production security, deployment, adoption, or resistance to
unseen inputs.

### Adoption and maintenance boundary

Read the public repository observations separately from functional proof:

```bash
gh api repos/OWNER/REPO --jq '{stars: .stargazers_count, forks: .forks_count, issues: .open_issues_count}'
gh api repos/OWNER/REPO/contributors --jq 'length'
```

Stars, forks, downloads, a local install, and a hosted demo remain observations. Outside adoption
requires a directly observed independent consumer or contributor; otherwise record `unknown`.
