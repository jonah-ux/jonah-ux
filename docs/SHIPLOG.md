# Jonah Helland — public ship log

This is a short record of public engineering work that another developer can
verify. Each entry links to source, a release, CI, or a reproducible receipt.

## Verified public history

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
