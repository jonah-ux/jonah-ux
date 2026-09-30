# Wave 2 public-main install matrix

Verification date: 2026-09-30

Each repository was installed from its public `main` branch into a fresh Python 3.14 virtual environment, then its documented `demos/demo.py` was run. The command ran through `worker-lifecycle` operation `wave2-public-main-demo-matrix-20260930-r2` and completed with exit code 0 and clean descendant cleanup.

| Repository | Installed CLI | Demo result |
| --- | --- | --- |
| [mcp-doctor](https://github.com/jonah-ux/mcp-doctor) | `mcp-doctor 0.2.0` | clean contract passes; broken fixture emits MCP002/MCP004 findings |
| [agent-eval-kit](https://github.com/jonah-ux/agent-eval-kit) | `agent-eval` | `agent-eval/v1`, `ok: true`, exit code 0 |
| [agent-proof](https://github.com/jonah-ux/agent-proof) | `agent-proof` | `agent-proof/v1` envelope with explicit `observed: false` |
| [context-pack](https://github.com/jonah-ux/context-pack) | `context-pack` | bounded file list, byte count, and SHA-256 digest |
| [agent-policy](https://github.com/jonah-ux/agent-policy) | `agent-policy` | `agent-policy/v1` allow decision with reason |
| [agent-trace-lite](https://github.com/jonah-ux/agent-trace-lite) | `agent-trace` | `agent-trace/v1` HTML artifact with two events |
| [agent-resume](https://github.com/jonah-ux/agent-resume) | `agent-resume` | valid `agent-resume/validation/v1` continuation record |
| [agent-sandbox-run](https://github.com/jonah-ux/agent-sandbox-run) | `agent-sandbox` | `agent-sandbox/v1` receipt with `enforced: false` honestly reported |

This proves public installability and runnable demos from `main`; it does not claim that these tools have published GitHub release objects yet.
