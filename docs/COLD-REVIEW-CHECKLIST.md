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
