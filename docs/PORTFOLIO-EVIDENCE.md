# Wave 2 public-main install matrix

Verification date: 2026-09-30

Each repository was installed from its public `main` branch into a fresh Python 3.14 virtual environment, its top-level CLI help was checked, and its documented `demos/demo.py` was run. The final current-head command ran through `worker-lifecycle` operation `wave2-current-head-final-matrix-20260930` and completed with exit code 0 and clean descendant cleanup.

| Repository | Installed CLI | Demo result |
| --- | --- | --- |
| [mcp-doctor](https://github.com/jonah-ux/mcp-doctor) | `mcp-doctor 0.2.0` | clean contract passes; broken fixture emits MCP002/MCP004 findings; tag identity and installed-consumer gates green at `7e73d0d` |
| [agent-eval-kit](https://github.com/jonah-ux/agent-eval-kit) | `agent-eval` | `agent-eval/v1`, `ok: true`, exit code 0; top-level `--help` succeeds; artifact matrix clean at `6d4a953` |
| [agent-proof](https://github.com/jonah-ux/agent-proof) | `agent-proof` | `agent-proof/v1` envelope with explicit `observed: false`; artifact matrix clean at `24b5835` |
| [context-pack](https://github.com/jonah-ux/context-pack) | `context-pack` | bounded file list, byte count, and SHA-256 digest; artifact matrix clean at `ea1c7f9` |
| [agent-policy](https://github.com/jonah-ux/agent-policy) | `agent-policy` | `agent-policy/v1` allow decision with reason; artifact matrix clean at `23576bc` |
| [agent-trace-lite](https://github.com/jonah-ux/agent-trace-lite) | `agent-trace` | `agent-trace/v1` HTML artifact with two events; artifact matrix clean at `84f9918` |
| [agent-resume](https://github.com/jonah-ux/agent-resume) | `agent-resume` | valid `agent-resume/validation/v1` continuation record; artifact matrix clean at `7f2c3e1` |
| [agent-sandbox-run](https://github.com/jonah-ux/agent-sandbox-run) | `agent-sandbox` | `agent-sandbox/v1` receipt with `enforced: false` honestly reported; artifact matrix clean at `2ffad63` |

All eight repositories now also carry the same reviewed `.github/workflows/release.yml`: a semantic-version tag builds a wheel and source archive, writes `SHA256SUMS`, and creates a GitHub prerelease. The eight workflow files pass `actionlint`; no tag was pushed as part of this evidence pass.

This proves public installability and runnable demos from `main`; it does not claim that these tools have published GitHub release objects yet.

The release payloads have also been built and consumed independently from the
current public heads: each repository produced a wheel, source archive, and
`SHA256SUMS`, then installed both artifacts into fresh environments. The
receipt is worker operation `wave2-artifact-build-install-clean-20261001`,
which completed successfully with clean cleanup and no license-deprecation
warnings.

Hosted CI is also green for all eight of those exact heads after the SPDX
metadata cleanup.
