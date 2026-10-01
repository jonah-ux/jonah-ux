# Jonah Helland — public ship log

This is a short record of public engineering work that another developer can
verify. Each entry links to source, a release, CI, or a reproducible receipt.

## Verified public history

| 2026-10-01 | Forgeyard 0.3.0 stable flagship release shipped with specialist-report composition and portable provenance packets | [release](https://github.com/jonah-ux/forgeyard/releases/tag/v0.3.0) · [workflow](https://github.com/jonah-ux/forgeyard/actions/runs/36932568488) · [merged PR](https://github.com/jonah-ux/forgeyard/pull/8) |

| 2026-10-01 | Chatlens 0.2.2 stable release shipped with checksum portability and snapshot identity-drift refusal | [release](https://github.com/jonah-ux/chatlens/releases/tag/v0.2.2) · [CI](https://github.com/jonah-ux/chatlens/actions) · [evidence matrix](PORTFOLIO-EVIDENCE.md) |

| 2026-10-01 | Forgeyard 0.2.6 stable release shipped with the one-command evidence-to-review demo | [release](https://github.com/jonah-ux/forgeyard/releases/tag/v0.2.6) · [workflow](https://github.com/jonah-ux/forgeyard/actions/runs/36928134865) · [merged PR](https://github.com/jonah-ux/forgeyard/pull/6) |

| 2026-10-01 | Forgeyard 0.2.0 promoted to stable after digest-pinned verifier, hosted release gates, and fresh wheel/source consumer proof | [release](https://github.com/jonah-ux/forgeyard/releases/tag/v0.2.0) · [workflow](https://github.com/jonah-ux/forgeyard/actions/runs/36919769410) · [evidence matrix](PORTFOLIO-EVIDENCE.md) |

| 2026-10-01 | Chatlens 0.2.0 promoted to stable after cross-platform CI and fresh wheel/source consumer proof | [release](https://github.com/jonah-ux/chatlens/releases/tag/v0.2.0) · [CI](https://github.com/jonah-ux/chatlens/actions) · [evidence matrix](PORTFOLIO-EVIDENCE.md) |

| 2026-10-01 | Slipstream 0.2.0 stable release published with inspect/manifest/verify contracts and packed-consumer CI proof | [release](https://github.com/jonah-ux/slipstream/releases/tag/v0.2.0) · [main commit](https://github.com/jonah-ux/slipstream/commit/d8a08b51a9105e341328341f06cac89d1725c812) · [CI](https://github.com/jonah-ux/slipstream/actions) |

| 2026-10-01 | MCP Doctor 0.3.0 prerelease published with deterministic fingerprints, baseline drift gates, wheel/sdist assets, checksums, and installed-consumer verification | [release](https://github.com/jonah-ux/mcp-doctor/releases/tag/v0.3.0) · [workflow](https://github.com/jonah-ux/mcp-doctor/actions/runs/36920607505) |

The public portfolio began on **2026-09-29**. These are the actual dates and
public commits; the history is intentionally not backfilled or re-dated.

| Date | Milestone | Public proof |
| --- | --- | --- |
| 2026-09-29 | Chatlens and Worktree Conservator source extraction began | [Chatlens history](https://github.com/jonah-ux/chatlens/commits/main) · [Worktree Conservator history](https://github.com/jonah-ux/worktree-conservator/commits/main) |
| 2026-09-30 | MCP Doctor and the seven supporting tools gained public packaging, demos, CI, and release workflows | [MCP Doctor history](https://github.com/jonah-ux/mcp-doctor/commits/main) · [portfolio evidence](PORTFOLIO-EVIDENCE.md) |
| 2026-09-30 | Profile README, hiring samples, evidence map, roadmap, and ship log were published | [profile history](https://github.com/jonah-ux/jonah-ux/commits/main) |
| 2026-10-01 | Release identity and built-consumer gates were propagated across the support tools | [latest profile evidence](PORTFOLIO-EVIDENCE.md) |
| 2026-10-01 | Worktree Conservator 0.2.0 stable release shipped with independent archive readback | [release](https://github.com/jonah-ux/worktree-conservator/releases/tag/v0.2.0) · [merged PR](https://github.com/jonah-ux/worktree-conservator/pull/1) · [main commit](https://github.com/jonah-ux/worktree-conservator/commit/dc6acf64a3698e4d709b82b3653d4e92031b3021) |
| 2026-10-01 | Forgeyard 0.2.0 prerelease published with digest-pinned record verification, wheel/source assets, checksums, and GitHub consumer gates | [release](https://github.com/jonah-ux/forgeyard/releases/tag/v0.2.0) · [merged PR](https://github.com/jonah-ux/forgeyard/pull/5) · [workflow](https://github.com/jonah-ux/forgeyard/actions/runs/36919769410) |

## 2026-10-01 — Forgeyard verified-release path

Forgeyard main now carries the verified 0.2.0 release path: annotated-tag
identity gates, wheel/source consumer checks, checksum assets, and explicit
separation between current source and the still-unpublished release object.
Worktree execution, command capture, resume, and cleanup remain planned
slices rather than shipped claims.

Evidence: [merged PR](https://github.com/jonah-ux/forgeyard/pull/5) · [public main](https://github.com/jonah-ux/forgeyard/commit/89cb5747ff9faa524d623ba650f34be7751173d3) · [hosted CI](https://github.com/jonah-ux/forgeyard/actions/runs/36919297244) · fresh consumer operations `forgeyard-verify-cli-tests-20261001d` and `forgeyard-020-consumer-check-20261001b`

GitHub contribution history should reflect this actual public work. Earlier
private or internal development is not presented as public open-source history.

## 2026-09-30 — release paths ready for the reliability toolkit

Added and linted the same semantic-tag release workflow across the eight
supporting tools:

- [MCP Doctor](https://github.com/jonah-ux/mcp-doctor)
- [Agent Eval Kit](https://github.com/jonah-ux/agent-eval-kit)
- [Agent Proof](https://github.com/jonah-ux/agent-proof)
- [Context Pack](https://github.com/jonah-ux/context-pack)
- [Agent Policy](https://github.com/jonah-ux/agent-policy)
- [Agent Trace Lite](https://github.com/jonah-ux/agent-trace-lite)
- [Agent Resume](https://github.com/jonah-ux/agent-resume)
- [Agent Sandbox Run](https://github.com/jonah-ux/agent-sandbox-run)

The workflow builds a wheel and source archive, writes `SHA256SUMS`, and
creates a GitHub prerelease only after an annotated semantic-version tag is
deliberately pushed. The workflow files pass `actionlint`; this historical
entry describes the release-path setup before the later public prerelease
objects were published.

Evidence: [portfolio evidence matrix](PORTFOLIO-EVIDENCE.md)

## 2026-10-01 — Worktree Conservator 0.2.0 stable release

Added receipt-bound, read-only archive verification to the flagship worktree
tool. The release includes wheel and source artifacts, checksums, a disposable
demo that proves `verify` before restore, and fresh wheel/sdist consumer runs.

Evidence: [v0.2.0 stable release](https://github.com/jonah-ux/worktree-conservator/releases/tag/v0.2.0) · [CI](https://github.com/jonah-ux/worktree-conservator/actions) · [release proof](PORTFOLIO-EVIDENCE.md)

## 2026-09-30 — public-main install matrix

Installed all eight supporting tools into fresh Python 3.14 environments and
ran each repository's documented disposable demo. The receipts cover stable
JSON schemas, bounded digests, explicit policy decisions, redacted traces,
identity validation, and honest sandbox enforcement state.

Evidence: [wave 2 install matrix](PORTFOLIO-EVIDENCE.md)

## 2026-09-30 — Agent Eval Kit help contract

The top-level `agent-eval --help` path now succeeds without requiring a
fixture or command. The CLI uses an explicit `run` subcommand, has a focused
test for the help contract, and still emits the same `agent-eval/v1` scorecard
from its disposable demo.

Evidence: [fix commit](https://github.com/jonah-ux/agent-eval-kit/commit/5b1ce5f) · [green CI run](https://github.com/jonah-ux/agent-eval-kit/actions/runs/36793852849)

## 2026-10-01 — release payload matrix

Built the wheel and source archive for every supporting tool from its current
public head, wrote a checksum manifest, and installed both artifacts into
fresh environments. Every artifact install passed its CLI help check. The
SPDX license metadata cleanup removed the shared setuptools deprecation warning
from the build output.

Evidence: `wave2-artifact-build-install-clean-20261001` completed with exit
code 0 and clean worker cleanup.

## 2026-10-01 — MCP Doctor release gates

MCP Doctor now refuses malformed, mismatched, lightweight, or moved tags. Its
release workflow verifies the package version, annotated tag identity, built
wheel/source payloads, and an installed consumer before publication. The
installed consumer checks the version, help contract, clean fixture, stable
MCP002/MCP004 diagnostics, and unreadable-input exit behavior.

Evidence: [release-gate commit](https://github.com/jonah-ux/mcp-doctor/commit/7e73d0d) · [green CI](https://github.com/jonah-ux/mcp-doctor/actions/runs/36795843101)

## 2026-10-01 — MCP Doctor contract drift baselines

MCP Doctor main now emits a deterministic SHA-256 fingerprint for the tools,
resources, and prompts it checks. A `--baseline=PATH` comparison reports only
stable entry names and digests for added, removed, and changed contracts;
`--fail-on-drift` turns that warning into an exit-1 CI gate. The report keeps
manifest descriptions and schema contents out of the drift payload, and a
malformed baseline returns an explicit input error.

Evidence: [merged PR](https://github.com/jonah-ux/mcp-doctor/pull/3) · [public main](https://github.com/jonah-ux/mcp-doctor/commit/2fa44b9a5bd15a3fcf8a6776ab133498d9a5990b) · [hosted CI](https://github.com/jonah-ux/mcp-doctor/actions/runs/36908352525) · fresh consumer operation `mcp-doctor-baseline-consumer-20261001-v1` · wheel SHA-256 `5cabfe8e90b72d5ea792086d3502889f2452294af61c62c07fb96e79646e3796` · sdist SHA-256 `24dbcd3d70f5d79a23aa24f5c16aa89182addeb2bf8ea2b704f7ae621af07865`

The public install surface is now v0.3.0 prerelease with wheel, sdist, checksums, and hosted consumer proof.

## 2026-10-01 — release gates propagated

The same tag identity and built-consumer checks now protect Agent Eval Kit,
Agent Proof, Agent Policy, Agent Trace Lite, Agent Resume, Agent Sandbox Run,
and Context Pack. Their latest CI runs are green. A separate bounded-source
branch remains preserved for later review and was not mixed into the public
release-gate change.

Evidence: [portfolio evidence matrix](PORTFOLIO-EVIDENCE.md)

## 2026-09-30 — Chatlens 0.1.0 prerelease

Chatlens now has a public GitHub prerelease with a wheel, source archive, and
`SHA256SUMS`. A clean Python 3.14 environment installed directly from the
public `v0.1.0` tag and returned `chatlens 0.1.0` with the expected CLI
commands.

Evidence: [release](https://github.com/jonah-ux/chatlens/releases/tag/v0.1.0) · [README demo](https://github.com/jonah-ux/chatlens#see-it-work)

## 2026-09-29 — agent reliability toolkit becomes composable

The profile now maps a single workflow across context recovery, bounded input,
policy decisions, sandbox receipts, proof bundles, and continuation records.
Each tool stays small, local-first, noninteractive, and explicit about what
it did not verify.

Evidence: [profile README](https://github.com/jonah-ux) · [one-minute work samples](WORK-SAMPLES.md)

## 2026-09-30 — profile visual system

Published the selected cool-tone workflow map as the profile hero and added
three small, accessible graphics that explain the portfolio at a glance:
the inspect/evaluate/prove/recover loop, the connected toolkit stack, and the
agent-friendly CLI contract. The images are stored in the repository so the
profile renders without a third-party design host.

Evidence: [profile README](https://github.com/jonah-ux) · `docs/profile-hero.png` · `docs/agent-loop.svg` · `docs/toolkit-stack.svg` · `docs/cli-contract.svg`

## 2026-09-30 — next open-source candidates

Screened existing work for a public-safe extraction path. The first greenlight
candidate is the reusable Slipstream local index engine; BreakTrace Lite is the
next candidate after synthetic-fixture and privacy work. Meeting Assistant and
the generic Agent Protocols edition remain qualified yellow candidates, while
customer integrations and operational experiment corpora stay private.

Evidence: [open-source pipeline](OPEN-SOURCE-PIPELINE.md)

## 2026-09-30 — Slipstream Core v0.1.0 prerelease

Extracted the provider-neutral local SQLite + `sqlite-vec` index core from the
larger private Slipstream work into a standalone public repository. The public
repo has an agent-friendly CLI, synthetic fixture, atomic build path, offline
self-test, Node 20/22/24 CI, an uploaded package tarball, and `SHA256SUMS`.
The uploaded tarball was downloaded by an independent consumer environment,
installed with its native dependency, and passed `slipstream self-test`.
Private registries, corpora, hooks, telemetry, credentials, customer data, and
internal adapters are excluded.

Evidence: [repository](https://github.com/jonah-ux/slipstream) · [v0.1.0 prerelease](https://github.com/jonah-ux/slipstream/releases/tag/v0.1.0) · [CI run](https://github.com/jonah-ux/slipstream/actions/runs/36815123917) · consumer proof `slipstream-consumer-selftest-20260930`

## 2026-10-01 — developer presence plan

Added a staged signup plan for the public surfaces that fit the portfolio:
LinkedIn, npm, PyPI, one technical writing home, Hugging Face, Product Hunt,
Docker Hub, and optional GitHub Sponsors. Each surface has a concrete trigger;
the plan explicitly avoids empty accounts, duplicate blogs, and package
publication before a stable release and consumer proof exist.

Evidence: [developer presence plan](DEVELOPER-PRESENCE.md)

## How to read this log

The log records public source and observed behavior. It does not count a commit
as a release, a demo as production adoption, or a historical claim as current
truth.


## 2026-10-01 — Agent Proof 0.2.0 stable release

Agent Proof 0.2.0 is the first stable public release in the toolkit. The reviewed release workflow built wheel and source assets, wrote SHA256SUMS, installed both distributions as fresh consumers, and ran the synthetic tamper-refusal and provenance-graph demo. Independent download readback verified both checksums and both consumer installs.

Evidence: [stable release](https://github.com/jonah-ux/agent-proof/releases/tag/v0.2.0) · [release commit](https://github.com/jonah-ux/agent-proof/commit/dad3fdc9d32ee4cf8c5f0b255b7a28e3d17e1038) · [license metadata PR](https://github.com/jonah-ux/agent-proof/pull/4) · [CI](https://github.com/jonah-ux/agent-proof/actions) · [evidence matrix](PORTFOLIO-EVIDENCE.md)

## 2026-10-01 — Chatlens 0.2.0 recovery prerelease

Chatlens 0.2.0 promotes the content-addressed recovery snapshot and source-matching verifier from main into a public prerelease. The wheel and source archive were checksum-verified, installed in fresh consumers, and the synthetic demo confirmed its transcript boundary.

Evidence: [v0.2.0 prerelease](https://github.com/jonah-ux/chatlens/releases/tag/v0.2.0) · [CI](https://github.com/jonah-ux/chatlens/actions) · [README](https://github.com/jonah-ux/chatlens#readme) · [evidence matrix](PORTFOLIO-EVIDENCE.md)

## 2026-10-01 — Agent Proof portable evidence readback

Agent Proof now reads its own exported gzip/tar bundles after the original artifact root is gone. The verifier rejects unsafe archive members, checks the manifest and document digests, reconstructs only declared source/artifact bytes, and reuses the v2 record/ledger/run verifier. The same mainline change adds a deterministic collector for recognized sibling envelopes.

Evidence: [merged PR](https://github.com/jonah-ux/agent-proof/pull/2) · [main commit](https://github.com/jonah-ux/agent-proof/commit/b3bb7b6fbcfa5464ad4bb366540bd5043974a275) · [CI](https://github.com/jonah-ux/agent-proof/actions) · [evidence matrix](PORTFOLIO-EVIDENCE.md)

The stable v0.2.0 release now carries the public install surface; its release assets and fresh-consumer readback are recorded above.

## 2026-10-01 — Slipstream inspectable index readback

Slipstream main now exposes a read-only `inspect` command with the
`slipstream/inspect/v1` contract. It checks the vec0 dimension, item/vector
parity, missing and orphan rows, stable item identity digest, kind counts, and
redacted metadata digests. The offline self-test requires a successful inspect
readback, and a fresh npm `0.2.0` tarball consumer built the public fixture and
returned four indexed items with four matching vector rows.

Evidence: [merged PR](https://github.com/jonah-ux/slipstream/pull/1) · [main commit](https://github.com/jonah-ux/slipstream/commit/8a862991f8829f6e0115d2d79b15043ced03262a) · [CI](https://github.com/jonah-ux/slipstream/actions) · [v0.1.0 public prerelease](https://github.com/jonah-ux/slipstream/releases/tag/v0.1.0)

The public install surface remains v0.1.0 until the next annotated release tag and asset readback exist.

## 2026-10-01 — Slipstream redacted content manifest

Slipstream main now adds `slipstream/manifest/v1` and `slipstream/verify/v1`.
The manifest records redacted per-row identity and stored float32 vector-byte
digests, metadata type and digest summaries, dimension and parity, package
version, SQLite version, and sqlite-vec runtime identity. Verification
rebuilds the same summary from a read-only copy and rejects changed rows,
vectors, metadata, dimensions, or runtime identity. The inspect and manifest
paths copy the database family into a temporary directory before reading, so
source `-wal` and `-shm` files are not created by inspection.

Evidence: [merged PR](https://github.com/jonah-ux/slipstream/pull/2) · [main commit at that stage](https://github.com/jonah-ux/slipstream/commit/b714d2377542c7ae4a7b457c5100c70edebe86ac) · [hosted CI](https://github.com/jonah-ux/slipstream/actions/runs/36892132065) · fresh consumer operation `slipstream-manifest-consumer-20261001-v2` · package SHA-256 `aec2c666ab6310ac62e0e6b0f2a817f22279dc007309779d95b36659c3fec4aa`

The public install surface remains v0.1.0. The source package is 0.2.0, but no 0.2.0 release object or tag is claimed here.

## 2026-10-01 — advanced interoperability pass

The next pass connected the public reliability tools at their existing evidence
boundaries. Each lane landed through a reviewed pull request and kept its
source, release, installed-consumer, and outcome claims separate.

### Agent Eval Kit receipt scoring

Agent Eval Kit main `df736b3` now scores a saved `agent-sandbox/v2` receipt
without rerunning the command. `agent-eval/receipt/v1` verifies receipt
integrity, expected exit and timeout state, and selected stdout fragments. The
source candidate is 0.3.0; the public release remains v0.1.1.

Evidence: [merged PR](https://github.com/jonah-ux/agent-eval-kit/pull/2) · [main](https://github.com/jonah-ux/agent-eval-kit/commit/df736b33581d9314b9a677ec41cda3083068324f) · 9-test operation `agent-eval-receipt-interop-final-20261001-v2` · fresh wheel/sdist consumers · wheel SHA-256 `743805e63ffd6c2a5dd543fdbf0cc720a807e59e5989fd57d7bb8c83d3f9ddf8` · sdist SHA-256 `2094b73ea67ef0a197562dfe32dc1d212a3c4749344a5983e73fb9e4d9c273f4`

### Agent Proof loss-aware sibling envelopes

Agent Proof main `f6dfa05` includes the reviewed `fe8c89b` interop change.
`agent-proof/interop/v1` normalizes known sibling envelopes without importing
raw values, while `interop-verify/v1` binds source bytes and fails closed on
tampering or unsafe paths. The stable v0.2.0 release boundary is unchanged.

Evidence: [merged PR](https://github.com/jonah-ux/agent-proof/pull/8) · [current main](https://github.com/jonah-ux/agent-proof/commit/f6dfa0506eb536cd9590b31a03452e06f2e8ff8b) · 33-test operation `agent-proof-interop-tests-20261001-v8` · demo operation `agent-proof-interop-regression-20261001-v7` · fresh wheel/sdist consumer operation `agent-proof-interop-consumer-20261001-v3` · hosted CI run `36929650619`

### Chatlens trace export

Chatlens main `a94ac1b` now exports a bounded, redacted
`chatlens-trace-envelope/v1` JSONL stream and validates it through
`trace-import`. The envelope binds source/session identity, row limits, event
digests, and the envelope digest; the importer refuses partial, tampered, or
unsafe output. The v0.2.2 stable release remains the public install surface.

Evidence: [merged PR](https://github.com/jonah-ux/chatlens/pull/7) · [main](https://github.com/jonah-ux/chatlens/commit/a94ac1b47b29219cf90867e7e3dea73f353ab1c6) · 23 synthetic tests · compileall proof · fresh Chatlens 0.2.2 wheel SHA-256 `347f80fc72fd901e156886fef86db16c13147e94549d9c039d394196b58c5865` · fresh Agent Trace Lite consumer with `trace-import ok:true` and `inspect` exit 0 · hosted macOS/Linux Python 3.11/3.12 CI

### Chatlens recovery trace handoff

Chatlens main now includes a synthetic recovery-trace roundtrip that writes a
bounded JSONL envelope, validates its digests, imports it through the public
reader, and proves redaction of email, home-path, and query-token fields. The
public v0.2.2 stable release remains the install surface.

Evidence: [merged PR](https://github.com/jonah-ux/chatlens/pull/8) · [current main](https://github.com/jonah-ux/chatlens/commit/442d9f47087630c9c88aaf472af97ea183f86ed1) · synthetic output `valid: true`, `trace_state: matched`, `redaction_proof: true` · 23-test CI matrix

### Forgeyard portable provenance packets

Forgeyard main `0ad158b` now seals verified records and evidence receipts into
`forgeyard-provenance-packet/v1`. The packet embeds exact record and receipt
bytes, binds source freshness, and rejects drift, tampering, unsafe paths, or
unknown live source roots. The later v0.3.0 release now carries this contract
as a stable public install surface.

Evidence: [merged PR](https://github.com/jonah-ux/forgeyard/pull/7) · [main](https://github.com/jonah-ux/forgeyard/commit/0ad158bb7c6b9655a0855971cf0df1270e37cd12) · 19-test operation `forgeyard-provenance-tests-20261001-v11` · compileall operation `forgeyard-provenance-compileall-20261001-v2` · fresh wheel/sdist consumer operation `forgeyard-provenance-consumer-20261001-v3` · adversarial refusal operation `forgeyard-provenance-adversarial-20261001-v4` · wheel SHA-256 `76f956fe5b1f0f507c46d5d6787c533c52e1ae8f783d24791b12d4ad97f600bf` · sdist SHA-256 `c566465c93467533b3107b2f0fdaea76157a3d669a424f78e79c8f7470f0d698`

### Forgeyard specialist-report composition

Forgeyard main now also includes `compose`, an offline read-only boundary that
accepts specialist reports only when they expose a boolean `ok` result. It
copies bounded schema/result metadata into review evidence, rejects malformed
reports, and keeps raw specialist payloads out of the review record. The
public v0.3.0 stable release carries this composition path.

Evidence: [merged PR](https://github.com/jonah-ux/forgeyard/pull/8) · [current main](https://github.com/jonah-ux/forgeyard/commit/d3fbd317032e903d2c4260e9f21973a90be26b68) · 22-test operation `forgeyard-compose-tests-20261001d` · clean `compose` consumer readback with `status: ready_for_review` and `verify` `reviewable: true`

The remaining unreleased projects retain the current boundaries in the
[advanced-pass roadmap](ROADMAP.md): another feature is held until it has a
named downstream consumer, a sanitized fixture, adversarial refusal coverage,
and fresh package readback. Forgeyard's 0.3.0 stable promotion is recorded
above; the other release boundaries remain unchanged.

## 2026-10-01 — Slipstream packed-consumer release gate

Slipstream main now runs a clean packed-consumer path in CI, rebuilding the
native dependency before invoking the CLI and keeping source, tag, asset, and
published-consumer proof separate. The release remains unpublished at 0.2.0.

Evidence: [merged PR](https://github.com/jonah-ux/slipstream/pull/6) · [public main](https://github.com/jonah-ux/slipstream/commit/80691b99337a949a0618393d1444ed38817f9a50) · [hosted CI](https://github.com/jonah-ux/slipstream/actions/runs/36919556239)

## 2026-10-01 — public toolkit iteration pass

The supporting lab received one deeper public-main pass per project. Agent Eval
Kit now compares repeated candidate trials with stable matrix fingerprints,
rankings, stability, latency, and structured timeout results. Context Pack now
has deterministic provenance manifests, verification, diff safety, atomic output,
and symlink/hardlink protections. Agent Policy now composes ordered layers and
binds decisions to normalized policy/request digests. Agent Trace Lite now has
strict redacted trace integrity inspection and bounded queries. Agent Resume now
has canonical handoff fingerprints and redacted diffs. Agent Sandbox Run now
emits bounded v2 receipts with command/output/receipt digests and explicit
timeout/enforcement state.

Evidence: [Agent Eval main](https://github.com/jonah-ux/agent-eval-kit/commit/83a443bf1f347f45359575cd79098e92daf7c892) · [Context Pack main](https://github.com/jonah-ux/context-pack/commit/e436a70f4de5aee8a8c0846dc7f882e83b81ebc4) · [Agent Policy main](https://github.com/jonah-ux/agent-policy/commit/cc5ee7df8984fb539dfa45089329057388cff192) · [Trace main](https://github.com/jonah-ux/agent-trace-lite/commit/5660935a86e12173009621cc70c15fe7adead30a) · [Resume main](https://github.com/jonah-ux/agent-resume/commit/1f0edf71c64a8b30a9ceb711073529d6f7d6a123) · [Sandbox main](https://github.com/jonah-ux/agent-sandbox-run/commit/ff1c9b2f460ddd2f50a07825cc06406e2217da8b)

The new source candidates remain separate from release adoption. Their current
public prerelease surfaces are unchanged until each project completes its own
tag, artifact, checksum, and fresh-download readback.

## 2026-10-01 — Slipstream manifest hardening

Slipstream main now carries the follow-up hardening for the manifest contract.
Manifest rows are canonically ordered by stable identity and item metadata is
hashed from canonical JSON. Stored vectors are encoded and labeled as
little-endian float32 bytes; malformed stored lengths and non-finite values are
rejected. `verify` returns exit 1 on mismatch, `manifest --out` refuses the
index and SQLite sidecars and writes atomically, missing paths do not create
parents, symlinked index paths resolve their sidecars, and the package exposes
the engine entrypoint for library consumers.

Evidence: [merged PR](https://github.com/jonah-ux/slipstream/pull/3) · [public main](https://github.com/jonah-ux/slipstream/commit/48009934c2cba2ea71ee1e730fc500f03e6ff2af) · [Node 20/22/24 hosted CI](https://github.com/jonah-ux/slipstream/actions/runs/36898248473) · fresh consumer operation `slipstream-manifest-public-main-consumer-20261001-v1` · package SHA-256 `eb597a9f29ca16ef25e77eccf4d9c6fdf1f13b463e893bec04dce9887d59d6a1`

The public install surface remains v0.1.0. The source package is 0.2.0, but no 0.2.0 release object or tag is claimed here.

## 2026-10-01 — Slipstream caller-owned vector workflow

Slipstream main now includes a disposable caller-owned vector example that
builds, queries, inspects, manifests, and verifies a local index through the
package export. The workflow keeps the vector store and metadata local, then
reports the inspect and manifest results without claiming a hosted index or
embedding-provider behavior. The public v0.2.0 stable release remains the
install surface.

Evidence: [merged PR](https://github.com/jonah-ux/slipstream/pull/8) · [current main](https://github.com/jonah-ux/slipstream/commit/5f455ef781ba7d51ae64fffad4ad4bdf29204f26) · [merge commit](https://github.com/jonah-ux/slipstream/commit/44b56e22c91da7e8db43871db4e3ded2d6f801b0) · hosted Node 20/22/24 checks
