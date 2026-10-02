# Jonah Helland — selected work

This is the fastest route through my public engineering work. Each sample has public source, a runnable interface, tests, and an explicit evidence boundary.

## Start with these three

### [Chatlens](https://github.com/jonah-ux/chatlens)

**Problem:** an agent’s previous reasoning is often trapped in a local session store when the next person needs to continue the work.

**What it shows:** local-first data discovery, bounded search and rendering, multiple source adapters, privacy boundaries, stable JSON output, and a versioned CLI release.

**Proof:** [v0.3.0 stable release](https://github.com/jonah-ux/chatlens/releases/tag/v0.3.0) · [current main](https://github.com/jonah-ux/chatlens/commit/0b4ce8e99fe9cfae911c0c73b40e646bb49cce58) · [release candidate PR](https://github.com/jonah-ux/chatlens/pull/10) · [CI](https://github.com/jonah-ux/chatlens/actions) · [README](https://github.com/jonah-ux/chatlens#readme)

```bash
python -m pip install 'git+https://github.com/jonah-ux/chatlens.git@v0.3.0'
chatlens --help
```

### [Worktree Conservator](https://github.com/jonah-ux/worktree-conservator)

**Problem:** removing a Git worktree can destroy useful context when identity, merge state, or recovery evidence is unclear.

**What it shows:** defensive CLI design, deterministic plans, archive verification, explicit refusal states, recovery-oriented workflows, and an independent post-apply readback command.

**Proof:** [v0.2.0 stable release](https://github.com/jonah-ux/worktree-conservator/releases/tag/v0.2.0) · [current main](https://github.com/jonah-ux/worktree-conservator/commit/7fd35503b5b07739b81be0697477b63c6d6a0979) · [maintainer recovery PR](https://github.com/jonah-ux/worktree-conservator/pull/8) · [CI](https://github.com/jonah-ux/worktree-conservator/actions) · [README](https://github.com/jonah-ux/worktree-conservator#readme)

### [MCP Doctor](https://github.com/jonah-ux/mcp-doctor)

**Problem:** an agent cannot make a reliable decision when an MCP tool contract is missing descriptions, schemas, or timeouts.

**What it shows:** contract validation, stable diagnostic codes, JSON and stdin interfaces, strict CI mode, deterministic contract fingerprints, baseline drift reports, and honest error boundaries.

**Proof:** [v0.3.0 prerelease](https://github.com/jonah-ux/mcp-doctor/releases/tag/v0.3.0) · [hardened main](https://github.com/jonah-ux/mcp-doctor/commit/fa3b2f7938172d350d2b878876952fde5775c034) · [release workflow](https://github.com/jonah-ux/mcp-doctor/actions/runs/36920607505) · [README](https://github.com/jonah-ux/mcp-doctor#readme)

MCP Doctor has a public v0.3.0 prerelease with downloadable wheel, sdist, and checksum assets. Its hosted release workflow verifies annotated-tag identity and a fresh installed consumer; the release remains labeled prerelease and is not presented as a stable package or PyPI publication.

### [Slipstream](https://github.com/jonah-ux/slipstream)

**Problem:** a local vector index can return plausible nearest results while its dimension, row parity, or caller-owned metadata state is no longer trustworthy.

**What it shows:** local SQLite + sqlite-vec indexing, atomic rebuilds, read-only integrity readback, stable identity digests, redacted metadata inspection, content-bound row and stored-vector digests, and a consumer-installable CLI contract.

**Proof:** [v0.2.0 stable release](https://github.com/jonah-ux/slipstream/releases/tag/v0.2.0) · [current main](https://github.com/jonah-ux/slipstream/commit/5f455ef781ba7d51ae64fffad4ad4bdf29204f26) · [caller-owned workflow PR](https://github.com/jonah-ux/slipstream/pull/8) · [fresh consumer receipt](https://github.com/jonah-ux/slipstream/actions) · [CI](https://github.com/jonah-ux/slipstream/actions)

The public `v0.2.0` stable release includes `slipstream/inspect/v1`, `slipstream/manifest/v1`, and `slipstream/verify/v1` with fail-closed tamper and output-collision handling. The packed-consumer CI gate and release target point at the hardened main.

### [Forgeyard](https://github.com/jonah-ux/forgeyard)

**Problem:** coding-agent work is difficult to review when the task, evidence, and readiness decision are scattered across prose and shell history.

**What it shows:** durable JSON task records, explicit pass/fail/unknown evidence, SHA-256 identity, fail-closed review readiness, and bounded worktree planning without hidden command execution.

**Proof:** [v0.3.2 annotated prerelease](https://github.com/jonah-ux/forgeyard/releases/tag/v0.3.2) · [v0.3.0 stable line](https://github.com/jonah-ux/forgeyard/releases/tag/v0.3.0) · [current main](https://github.com/jonah-ux/forgeyard/commit/242a55b635b57a7ac350d5f3b32e22683b26c9ed) · [public Workbench](https://jonah-ux.github.io/forgeyard/) · [Pages deployment](https://github.com/jonah-ux/forgeyard/actions/runs/37072935676) · [interop PR #15](https://github.com/jonah-ux/forgeyard/pull/15) · [patch release PR #16](https://github.com/jonah-ux/forgeyard/pull/16) · [annotated release-path PR #18](https://github.com/jonah-ux/forgeyard/pull/18) · [release workflow](https://github.com/jonah-ux/forgeyard/actions/runs/37075121371) · [current-main CI](https://github.com/jonah-ux/forgeyard/actions/runs/37075121395) · passing, Context Integrity, MCP010 drift-blocked, export, tamper-refusal, bounded benchmark receipt, and runtime-loaded fixture flows; downloaded v0.3.2 wheel/source checksums and fresh consumers read back

Forgeyard remains an early public foundation. Worktree execution, command capture, resume, and cleanup safety are planned slices and remain labeled as planned.

### [Context Integrity Lab](https://github.com/jonah-ux/context-integrity-lab)

**Problem:** an assistant can produce a plausible answer from the wrong person, stale context, unavailable sources, or fresh but irrelevant evidence.

**What it shows:** deterministic person/project scope admission, freshness windows, structured citations, explicit refusal states, duplicate and ambiguous identity holds, and a local browser console over fictional records.

**Proof:** [v0.2.0 stable release](https://github.com/jonah-ux/context-integrity-lab/releases/tag/v0.2.0) · [current main](https://github.com/jonah-ux/context-integrity-lab/commit/537a42c37603a47db26b6dcdb41e02ee15799229) · [envelope PR #1](https://github.com/jonah-ux/context-integrity-lab/pull/1) · [CI](https://github.com/jonah-ux/context-integrity-lab/actions/runs/37073892096) · [README](https://github.com/jonah-ux/context-integrity-lab#readme) · wheel `0cc846bfe182bcc8ed95bb575135ba86da48b60ffeb01fca8b25603a7cdbeb1f` · sdist `9354dea7ecda5126d0b54b6c7905f8f608042a26b660f1d034d1b14488afcca1` · downloaded wheel/sdist consumers exercised the supported `context-integrity/v1` envelope, citation count, refusal fields, and downstream Agent Proof handoff

Context Integrity Lab is synthetic and local-first. It does not claim model accuracy, production deployment, employer-system integration, or external adoption.

### Supporting lab: deeper contracts on public main

- [Agent Eval Kit](https://github.com/jonah-ux/agent-eval-kit) now has a `v0.3.0` prerelease and scores saved Agent Sandbox Run receipts without rerunning commands through `agent-eval/receipt/v1` at [main `df736b3`](https://github.com/jonah-ux/agent-eval-kit/commit/df736b33581d9314b9a677ec41cda3083068324f).
- [Context Pack](https://github.com/jonah-ux/context-pack) now has a `v0.2.0` prerelease with deterministic bounded-source manifests and diff safety at [main `e436a70`](https://github.com/jonah-ux/context-pack/commit/e436a70f4de5aee8a8c0846dc7f882e83b81ebc4).
- [Agent Policy](https://github.com/jonah-ux/agent-policy) now has a `v0.2.0` prerelease with ordered policy layers and digest-bound explanations at [main `cc5ee7d`](https://github.com/jonah-ux/agent-policy/commit/cc5ee7df8984fb539dfa45089329057388cff192).
- [Agent Trace Lite](https://github.com/jonah-ux/agent-trace-lite) now has a `v0.2.0` prerelease and remains the bounded downstream consumer for Chatlens `trace-import` at [main `5660935`](https://github.com/jonah-ux/agent-trace-lite/commit/5660935a86e12173009621cc70c15fe7adead30a).
- [Agent Resume](https://github.com/jonah-ux/agent-resume) now has a `v0.2.0` prerelease with integrity-bound continuation records and redacted diffs at [main `1f0edf7`](https://github.com/jonah-ux/agent-resume/commit/1f0edf71c64a8b30a9ceb711073529d6f7d6a123).
- [Agent Sandbox Run](https://github.com/jonah-ux/agent-sandbox-run) now has a `v0.2.0` prerelease and remains the receipt producer consumed by Agent Eval Kit at [main `ff1c9b2`](https://github.com/jonah-ux/agent-sandbox-run/commit/ff1c9b2f460ddd2f50a07825cc06406e2217da8b).

Agent Proof's public v0.2.0 release remains stable while the annotated v0.3.1
prerelease carries the Context Integrity adapter. Agent Eval Kit, Context Pack,
Agent Policy, Agent Trace Lite, Agent Resume, and Agent Sandbox Run have
annotated prereleases with independent downloaded-asset readback. Forgeyard
v0.3.0 remains the stable line while annotated v0.3.2 carries the Workbench
interop slice; Chatlens v0.3.0 and Context Integrity Lab v0.2.0 are stable
public releases.
External adoption remains unknown until a consumer outside these repository
workflows is observed.

## The engineering pattern

Across the projects, I focus on the full path from a small interface to a result someone else can inspect:

- **APIs and integrations:** adapters and explicit input contracts keep system boundaries visible.
- **Data and state:** local indexes, bounded records, hashes, and coverage fields make state inspectable.
- **Automation:** noninteractive commands, stable JSON, meaningful exit codes, and CI-friendly behavior.
- **Reliability:** refusal states and unknowns stay visible instead of being turned into false success.
- **Release discipline:** public source, versioned tags or release heads, CI, demos, security guidance, and reproducible checks. I label prereleases and release candidates separately instead of implying that every tool is already a published package.

The smaller [agent tooling lab](https://github.com/jonah-ux#the-agent-tooling-lab) extends the same pattern into evaluation, evidence, policy, tracing, continuation, and command limits.

## Good conversations to have with me

- Designing an API or automation workflow that has to remain observable after it leaves the happy path.
- Turning a local or internal workflow into a small, installable developer tool.
- Making AI-agent behavior inspectable through structured output, evidence records, and safe boundaries.
- Connecting product needs, databases, integrations, and operational reality without hiding uncertainty.


### [Agent Proof](https://github.com/jonah-ux/agent-proof)

**Problem:** a command receipt can be intact while the artifact, source envelope, or claimed outcome has changed or was never observed.

**What it shows:** canonical evidence records, append-only hash chains, repository identity, redacted output digests, schema-aware collection, portable gzip/tar bundle verification, and explicit unknown or partial states.

**Proof:** [v0.3.1 annotated prerelease](https://github.com/jonah-ux/agent-proof/releases/tag/v0.3.1) · [v0.2.0 stable baseline](https://github.com/jonah-ux/agent-proof/releases/tag/v0.2.0) · [current main](https://github.com/jonah-ux/agent-proof/commit/1287b880e02bd979026af96c7466714d224a2080) · [interop PR #10](https://github.com/jonah-ux/agent-proof/pull/10) · [CLI version PR #11](https://github.com/jonah-ux/agent-proof/pull/11) · [annotated release-path PR #12](https://github.com/jonah-ux/agent-proof/pull/12) · [release workflow](https://github.com/jonah-ux/agent-proof/actions/runs/37075015117) · [README](https://github.com/jonah-ux/agent-proof#readme)

Agent Proof has a stable `v0.2.0` GitHub release and an annotated `v0.3.1` prerelease with wheel/source assets, checksums, fresh consumer installs, and the reviewed `context-integrity/v1` adapter. The release workflow and downloaded readback prove the package and CLI identity; external adoption remains unknown.
