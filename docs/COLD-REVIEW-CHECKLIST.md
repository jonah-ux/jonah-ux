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

Use Python 3.11 or later. Keep `git rev-parse HEAD` with the command output and compare it with
the [review lock](AGENT-SYSTEMS-LAB-REVIEW-LOCK.json) before attributing a current-main run to the
frozen snapshot.

```bash
git clone https://github.com/jonah-ux/forgeyard.git
cd forgeyard
python3 -m venv .venv
. .venv/bin/activate
python3 -m pip install -e .
forgeyard demo
```

The demo should print a `forgeyard-demo/v1` document with a reviewable record and
packet. That proves the package's local evidence path; it does not prove a merge,
deployment, or production result.

## 3. Run the integrated local flow

The reference harness uses only checked-in synthetic reports and calls the public
Forgeyard CLI:

```bash
python3 scripts/run_reference_flow.py --scenario passing
python3 scripts/run_reference_flow.py --scenario blocked
python3 scripts/run_reference_flow.py --scenario tampered
```

Expected outcomes are `reviewable`, `blocked`, and `refused`, respectively. The
script returns zero when each expected outcome is observed, so the result field and
the nested compose/verification exits must be read together.

Then run the fixed-dataset lab benchmark:

```bash
python3 scripts/benchmark_lab.py --iterations 20 --warmup 3 --json
```

Check for `forgeyard-lab-benchmark/v1`, nine reports, six operation names
(`parse`, `validate`, `index`, `replay`, `compose`, `packet_verify`),
`packet_ok: true`, and `private_payloads_exported: false`. Timings are machine-local
observations, not cross-machine rankings.

With Forgeyard 0.5.1, run the native refusal evaluation separately:

```bash
forgeyard evaluate-refusals
```

The 0.5.1 release executes nineteen synthetic native contract cases and controls. Compare the
package version and returned corpus identity with the
[0.5.1 packet evidence](EXTERNAL-REVIEW-PACKET.md#forgeyard-release-after-the-snapshot).
This is a native contract exercise; it does not establish specialist policy/sandbox enforcement
or provider behavior.

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
These fifteen rows are stored catalogue labels. The native evaluation above is the executed
refusal evidence; neither boundary establishes production enforcement or outside adoption.

## 5. Follow the owner boundaries

To check declarations before connecting the tools, use the
[Agent Proof 0.5.0 installed review route](EXTERNAL-REVIEW-PACKET.md#agent-proof-050-offline-compatibility-foundation).
It checks all thirteen selected declarations and explicit version constraints while reporting
`execution=not_attempted`. Keep that result separate from the owner-native behavior below.

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
```

Before installation, verify the downloaded bytes against the release's `SHA256SUMS` using the
owner-native audit with `--dist-dir` and `--require-dist`, as described in the
[audit matrix](AGENT-SYSTEMS-LAB-AUDIT-MATRIX.md). Keep the wheel, sdist, and checksum manifest
together in that directory. An omitted or incomplete directory must not be treated as release
evidence.

After the artifact audit passes, install into the disposable environment:

```bash
python3 -m pip install --no-index --no-deps PACKAGE.whl
python3 -m pip check
```

Record the package version, tag, target commit, asset names, and checksum as one observation. A
successful local install does not prove that the package was built reproducibly or that a future
release will carry the same dependencies.

Check the source boundary directly:

```bash
test -f LICENSE
test -f SECURITY.md
python3 - <<'PY'
import pathlib, tomllib
data = tomllib.loads(pathlib.Path("pyproject.toml").read_text())
print(data.get("project", {}).get("dependencies", []))
PY
```

The current public Python owners use standard-library runtime dependencies in their reviewed
packages. This command records the actual project metadata; it is not a substitute for a complete
license audit or a platform-attested build provenance record.

Every current flagship owner exposes a bounded, owner-native public audit. Run it from each clean
checkout and keep the receipt with the source head:

```bash
python3 scripts/audit_public_surface.py --json
```

Use this command in Forgeyard, Agent Proof, Atlas Agent Runtime, ChatLens, Agent Policy, Agent Sandbox Run,
Sourcemark, Worktree Conservator, Agent Resume, Agent Trace Lite, MCP Doctor, and Context
Integrity Lab. Slipstream owns a Node command instead; run it from its checkout:

```bash
node scripts/audit_public_surface.js --json
```

A static `pass`
means the named dependency, license, release-marker, and high-signal privacy checks passed. An
artifact result of `unavailable` is expected when no `--dist-dir` was supplied. The audits do not
claim complete DLP, security certification, reproducible builds across machines, deployment,
adoption, or production readiness.

Use the [owner audit matrix](AGENT-SYSTEMS-LAB-AUDIT-MATRIX.md) to keep the schema names, commands,
and artifact boundary aligned as owner heads move.

### Secret, private-path, and synthetic-data scan

Run the scan from the repository root and inspect every match. The patterns are intentionally
conservative; a fixture that contains a documented synthetic marker must be classified rather than
silently ignored:

```bash
rg -n --hidden --glob '!.git/**' --glob '!.venv/**' -e \
  '-----BEGIN (RSA|OPENSSH|EC|PGP) PRIVATE KEY-----|sk-[A-Za-z0-9]{20,}|ghp_[A-Za-z0-9]{20,}|/Users/|/home/|jonahsnorthstar|customer|EIN|api[_-]?key' .
```

Ripgrep returns exit `0` for matches, `1` for no matches, and `2` for a command error. An error is
an incomplete scan and must be repaired before interpreting the output. The `-e` keeps the leading
hyphens in the private-key pattern from being parsed as command options.

The expected outcome for a public fixture tree is zero unclassified hits. A clean search is not a
secret-scanning service and does not prove that a provider-side history is clean. Keep transcript
text, credentials, customer records, private paths, and employer policy outside checked-in examples.

### Hostile-input and confused-deputy review

Use the existing owner tests and receipts rather than creating a second security harness:

- Forgeyard 0.5.1 `forgeyard evaluate-refusals` executes nineteen native cases with a passing
  control, including traversal, symlink escape, payload redaction, schema drift, duplicate
  evidence, stale provenance, bounded summaries, and false completion. The pinned corpus
  rejects empty or truncated success claims. The fifteen Workbench threat labels remain a
  separate static catalogue; they do not execute every specialist owner's enforcement path.
- Forgeyard `python3 scripts/evaluate_lab.py --dist-dir ./dist --install --json` makes supplied
  artifact or installation failures block its result. Omitted optional inputs remain unavailable.
  Latency, separate Python allocation peaks, artifact sizes, and installation timings are local
  observations with explicit environment and protocol metadata.
- Agent Proof `verify-graph --input` must refuse a changed edge and a resealed orphan edge.
- Agent Policy must preserve default-deny and its versioned `agent-policy/receipt/v1` boundary.
- Agent Sandbox Run must keep `agent-sandbox/v2` backend and enforcement disclosure explicit; a
  fallback receipt is evidence of fallback, not proof of isolation.
- Worktree Conservator must leave real worktrees untouched during disposable conformance runs.

Record the exact command, source head, receipt, and refusal result. A green fixture test proves the
fixture boundary; it does not prove production security, deployment, adoption, or resistance to
unseen inputs.

For a complete graph/packet reproducer, run the [failure-analysis walkthrough](FAILURE-WALKTHROUGH.md).
It uses the existing lock and native CLIs, keeps each refusal report, and distinguishes an intact
unbound graph from a source-bound verification. Hosted CI runs its runnable blocks and preserves
the native verification reports with generic runner paths redacted.

### Adoption and maintenance boundary

Read the public repository observations separately from functional proof:

```bash
gh api repos/OWNER/REPO --jq '{stars: .stargazers_count, forks: .forks_count, issues: .open_issues_count}'
gh api repos/OWNER/REPO/contributors --jq 'length'
```

Stars, forks, downloads, a local install, and a hosted demo remain observations. Outside adoption
requires a directly observed independent consumer or contributor; otherwise record `unknown`.
