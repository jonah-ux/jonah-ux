# Open-source pipeline

The public portfolio grows from real systems Jonah has already built. Each
candidate below has a separate extraction, privacy, install, and release gate.
The labels describe the current boundary; they are not claims that a private
source tree is already public.

## Shipped first: Slipstream Core

**What it is:** a local semantic index engine for coding-agent tools and
documents. Build once into SQLite + `sqlite-vec`, then query locally without a
remote pooler round trip.

**Why it belongs in the portfolio:** it shows performance work, native Node
dependencies, vector search, deterministic fixtures, and a concrete reason an
agent tool should be local-first.

**Public shape:** extract the generic index engine, a small JSON fixture adapter,
an installable CLI, a benchmark command, and an offline self-test. Keep Fleet
registries, memory corpora, credentials, hooks, telemetry, and internal
adapters out of the public repository.

**Current proof:** public `v0.1.0` prerelease, uploaded package tarball,
`SHA256SUMS`, green Node 20/22/24 CI, a clean local `npm test` receipt, and a
fresh `0.2.0` consumer that builds an index, writes a redacted
`slipstream/manifest/v1`, and verifies the unchanged index with matching
manifest/current hashes. The release is a prerelease while the independent
consumer cycle continues.

## Greenlight after sanitization: BreakTrace Lite

**What it is:** an offline root-cause analysis engine that normalizes failure
signals, records competing hypotheses, and requires a skeptic check before a
case is called resolved.

**Why it belongs in the portfolio:** it demonstrates reliability engineering,
failure fingerprinting, explainable evidence, and explicit unknown states.

**Public shape:** publish the pure fingerprint, similarity, hypothesis, and
reporting modules with synthetic fixtures. Keep Supabase migrations, fleet
schemas, operational packets, live queries, and customer/system identifiers
private.

**Release bar:** synthetic failure corpus, redaction tests, deterministic JSON
schema, CLI demo, security review, and a fresh install from the tagged release.

## Yellow: Cited Meeting Assistant

**What it is:** a local-first meeting companion with on-device captions,
searchable context, and cited notes.

**Why it belongs in the portfolio:** it is a compelling product surface that
connects native application work, privacy, local inference, and evidence-backed
summaries.

**Boundary still needed:** package only the downloadable application and
synthetic demo data. Remove private runtime context, recordings, uploads,
queues, credentials, internal Fleet tooling, and personal history. The release
manifest already gives this project a useful starting point.

## Yellow: Agent Protocols

**What it is:** short trigger-based checklists for agent decisions such as
preflight, stale-context checks, blast-radius review, and honest handoff.

**Why it belongs in the portfolio:** it is approachable, immediately useful,
and shows how Jonah turns operational lessons into reusable agent interfaces.

**Boundary still needed:** the original protocol collection has been
consolidated into the Fleet monorepo and contains internal injection and
infrastructure references. A public edition should be a new generic protocol
library with examples, license, contribution guide, and no Fleet endpoints or
private rollout mechanics.

## Hold: experiment and customer-integrations work

The tool-value experiments, MCP integrations, recruiting systems, lead bots,
and Portal/Fleet operational repositories contain private fixtures, customer
data boundaries, credentials, or live-system assumptions. They remain valuable
source material, but the right public move is to extract a generic fixture or
SDK only after a separate privacy and ownership review.

## The extraction rule

Every new public repo must have:

1. one clear user problem and a short install path;
2. a synthetic fixture that works without Jonah's environment;
3. stable CLI or library contracts with machine-readable output;
4. tests that prove both the happy path and the honest failure path;
5. `LICENSE`, `SECURITY.md`, contribution guidance, and release notes;
6. a fresh-consumer receipt tied to the exact public tag.

This keeps the profile interesting without turning private operations into
public source or inflating the activity story.
