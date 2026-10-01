# Jonah Helland — selected work

This is the fastest route through my public engineering work. Each sample has public source, a runnable interface, tests, and an explicit evidence boundary.

## Start with these three

### [Chatlens](https://github.com/jonah-ux/chatlens)

**Problem:** an agent’s previous reasoning is often trapped in a local session store when the next person needs to continue the work.

**What it shows:** local-first data discovery, bounded search and rendering, multiple source adapters, privacy boundaries, stable JSON output, and a versioned CLI release.

**Proof:** [v0.1.0 release](https://github.com/jonah-ux/chatlens/releases/tag/v0.1.0) · [CI](https://github.com/jonah-ux/chatlens/actions) · [README](https://github.com/jonah-ux/chatlens#readme)

```bash
python -m pip install 'git+https://github.com/jonah-ux/chatlens.git@v0.1.0'
chatlens --help
```

### [Worktree Conservator](https://github.com/jonah-ux/worktree-conservator)

**Problem:** removing a Git worktree can destroy useful context when identity, merge state, or recovery evidence is unclear.

**What it shows:** defensive CLI design, deterministic plans, archive verification, explicit refusal states, recovery-oriented workflows, and an independent post-apply readback command.

**Proof:** [v0.2.0 prerelease](https://github.com/jonah-ux/worktree-conservator/releases/tag/v0.2.0) · [merged PR](https://github.com/jonah-ux/worktree-conservator/pull/1) · [CI](https://github.com/jonah-ux/worktree-conservator/actions) · [README](https://github.com/jonah-ux/worktree-conservator#readme)

### [MCP Doctor](https://github.com/jonah-ux/mcp-doctor)

**Problem:** an agent cannot make a reliable decision when an MCP tool contract is missing descriptions, schemas, or timeouts.

**What it shows:** contract validation, stable diagnostic codes, JSON and stdin interfaces, strict CI mode, deterministic contract fingerprints, baseline drift reports, and honest error boundaries.

**Proof:** [v0.2.4 prerelease](https://github.com/jonah-ux/mcp-doctor/releases/tag/v0.2.4) · [hardened main](https://github.com/jonah-ux/mcp-doctor/commit/2fa44b9a5bd15a3fcf8a6776ab133498d9a5990b) · [CI](https://github.com/jonah-ux/mcp-doctor/actions/runs/36908352525) · [README](https://github.com/jonah-ux/mcp-doctor#readme)

MCP Doctor has a public v0.2.4 prerelease with downloadable artifacts and
hosted consumer checks. Current main is a 0.3.0 source candidate with fresh
wheel and sdist consumer proof; the release remains labeled prerelease, so the
profile does not imply a stable package or PyPI publication.

### [Slipstream](https://github.com/jonah-ux/slipstream)

**Problem:** a local vector index can return plausible nearest results while its dimension, row parity, or caller-owned metadata state is no longer trustworthy.

**What it shows:** local SQLite + sqlite-vec indexing, atomic rebuilds, read-only integrity readback, stable identity digests, redacted metadata inspection, content-bound row and stored-vector digests, and a consumer-installable CLI contract.

**Proof:** [v0.1.0 public prerelease](https://github.com/jonah-ux/slipstream/releases/tag/v0.1.0) · [hardened manifest and verify main](https://github.com/jonah-ux/slipstream/commit/48009934c2cba2ea71ee1e730fc500f03e6ff2af) · [merged PR](https://github.com/jonah-ux/slipstream/pull/3) · [fresh consumer receipt](https://github.com/jonah-ux/slipstream/actions) · [CI](https://github.com/jonah-ux/slipstream/actions)

The public `v0.1.0` prerelease remains the released install surface. Current `main` adds `slipstream/inspect/v1`, `slipstream/manifest/v1`, and `slipstream/verify/v1` with fail-closed tamper and output-collision handling; its `0.2.0` release object has not been claimed.

### [Forgeyard](https://github.com/jonah-ux/forgeyard)

**Problem:** coding-agent work is difficult to review when the task, evidence, and readiness decision are scattered across prose and shell history.

**What it shows:** durable JSON task records, explicit pass/fail/unknown evidence, SHA-256 identity, fail-closed review readiness, and bounded worktree planning without hidden command execution.

**Proof:** [public repository](https://github.com/jonah-ux/forgeyard) · [CI](https://github.com/jonah-ux/forgeyard/actions) · [README](https://github.com/jonah-ux/forgeyard#readme)

Forgeyard is intentionally an early public foundation. Worktree execution, command capture, resume, and cleanup safety are planned slices and remain labeled as planned.

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

**Proof:** [v0.2.0 stable release](https://github.com/jonah-ux/agent-proof/releases/tag/v0.2.0) · [license metadata PR](https://github.com/jonah-ux/agent-proof/pull/4) · [current main](https://github.com/jonah-ux/agent-proof/commit/dad3fdc9d32ee4cf8c5f0b255b7a28e3d17e1038) · [CI](https://github.com/jonah-ux/agent-proof/actions) · [README](https://github.com/jonah-ux/agent-proof#readme)

Agent Proof now has a stable `v0.2.0` GitHub release with wheel and source assets, checksums, fresh consumer installs, and a demo that verifies tamper refusal and the provenance graph.
