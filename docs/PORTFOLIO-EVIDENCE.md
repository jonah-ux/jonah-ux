# Wave 2 public-main install matrix

Verification date: 2026-09-30

Each repository was installed from its public `main` branch into a fresh Python 3.14 virtual environment, its top-level CLI help was checked, and its documented `demos/demo.py` was run. The final current-head command ran through `worker-lifecycle` operation `wave2-current-head-final-matrix-20260930` and completed with exit code 0 and clean descendant cleanup.

| Repository | Installed CLI | Demo result |
| --- | --- | --- |
| [mcp-doctor](https://github.com/jonah-ux/mcp-doctor) | `mcp-doctor 0.2.0` | clean contract passes; broken fixture emits MCP002/MCP004 findings; tag identity and installed-consumer gates green at `7e73d0d` |
| [agent-eval-kit](https://github.com/jonah-ux/agent-eval-kit) | `agent-eval` | `agent-eval/v1`, `ok: true`, exit code 0; top-level `--help` succeeds; release identity gates and CI green at `175dc19` |
| [agent-proof](https://github.com/jonah-ux/agent-proof) | `agent-proof` | `agent-proof/v1` envelope with explicit `observed: false`; release identity gates and CI green at `3b2743c` |
| [context-pack](https://github.com/jonah-ux/context-pack) | `context-pack` | bounded file list, byte count, and SHA-256 digest; release identity gates and CI green at `26efe75` |
| [agent-policy](https://github.com/jonah-ux/agent-policy) | `agent-policy` | `agent-policy/v1` allow decision with reason; release identity gates and CI green at `869b009` |
| [agent-trace-lite](https://github.com/jonah-ux/agent-trace-lite) | `agent-trace` | `agent-trace/v1` HTML artifact with two events; release identity gates and CI green at `fdeca9a` |
| [agent-resume](https://github.com/jonah-ux/agent-resume) | `agent-resume` | valid `agent-resume/validation/v1` continuation record; release identity gates and CI green at `85a34d1` |
| [agent-sandbox-run](https://github.com/jonah-ux/agent-sandbox-run) | `agent-sandbox` | `agent-sandbox/v1` receipt with `enforced: false` honestly reported; release identity gates and CI green at `ce87a33` |

MCP Doctor and seven supporting repositories now carry the strengthened `.github/workflows/release.yml`: a semantic-version tag must match the package version and annotated HEAD, build wheel/source assets, verify both consumers, write `SHA256SUMS`, and only then create a GitHub prerelease. All eight workflow files pass `actionlint`; no tag was pushed as part of this evidence pass.

This proves public installability and runnable demos from `main`; it does not claim that these tools have published GitHub release objects yet.

The release payloads have also been built and consumed independently from the
current public heads: each repository produced a wheel, source archive, and
`SHA256SUMS`, then installed both artifacts into fresh environments. The
receipt is worker operation `wave2-artifact-build-install-clean-20261001`,
which completed successfully with clean cleanup and no license-deprecation
warnings.

Hosted CI is also green for all eight of those exact heads after the SPDX
metadata cleanup.

Seven supporting repositories now also verify annotated tag identity, package version matching, wheel/source consumer help, and `gh release create --verify-tag` before publication. A separate local bounded-source branch remains preserved for later review; it was not mixed into this release-gate change.
