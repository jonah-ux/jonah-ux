# Agent Systems Lab conformance matrix

This matrix is the public owner map for the current conformance wave. Each
repository keeps its native schema and test runner. The manifests point to the
existing Agent Proof interop owner where a normalized handoff is needed; no
repository imports another at runtime and no second registry is introduced.

| Owner | Native boundary | Public conformance artifact | Current proof |
| --- | --- | --- | --- |
| [Forgeyard](https://github.com/jonah-ux/forgeyard) | `ai-work-evidence/v1`, `forgeyard-compose/v1`, `forgeyard-provenance-packet/v1` | [Corpus and runner](https://github.com/jonah-ux/forgeyard/tree/main/conformance), [v0.5.0 release](https://github.com/jonah-ux/forgeyard/releases/tag/v0.5.0) | Seven-case owner corpus, hosted Workbench, 15-class adversarial matrix, tagged reference flow, and six-operation benchmark |
| [ChatLens](https://github.com/jonah-ux/chatlens) | `chatlens-trace-envelope/v1`, shared evidence projection | [Consumer conformance](https://github.com/jonah-ux/chatlens/blob/main/tests/test_conformance.py) | Independent fixture validates complete/partial trace status and owner corpus pin |
| [Atlas Agent Runtime](https://github.com/jonah-ux/atlas-agent-runtime) | `atlas-receipt/v1`, shared evidence projection | [Consumer conformance](https://github.com/jonah-ux/atlas-agent-runtime/blob/main/tests/test_conformance.py) | Independent fixture validates completed/queued/failed lifecycle status and owner corpus pin |
| [Agent Proof](https://github.com/jonah-ux/agent-proof) | `agent-proof/interop/v1`, `agent-proof-lab-conformance/v1` | [Interop registry](https://github.com/jonah-ux/agent-proof/blob/main/conformance/agent-systems-lab.json) | Native adapter tests cover policy, sandbox, evaluation, trace, context-pack, resume, and Context Integrity envelopes |
| [Context Integrity Lab](https://github.com/jonah-ux/context-integrity-lab) | `context-integrity/v1` | [Owner manifest](https://github.com/jonah-ux/context-integrity-lab/blob/main/conformance/agent-systems-lab.json) | Supported, wrong-scope, stale, uncertain, unavailable-source, citation, and unknown-state tests |
| [Agent Policy](https://github.com/jonah-ux/agent-policy) | `agent-policy/v1` | [Owner manifest](https://github.com/jonah-ux/agent-policy/blob/main/conformance/agent-systems-lab.json) | Explicit allow/deny/default-deny, digest, traversal, version, and privacy-boundary tests |
| [Agent Sandbox Run](https://github.com/jonah-ux/agent-sandbox-run) | `agent-sandbox/v2` | [Owner manifest](https://github.com/jonah-ux/agent-sandbox-run/blob/main/conformance/agent-systems-lab.json) | Backend/enforcement disclosure, command/receipt digest, bounded-output, and timeout tests |
| [Agent Resume](https://github.com/jonah-ux/agent-resume) | `agent-resume/v1` | [Owner manifest](https://github.com/jonah-ux/agent-resume/blob/main/conformance/agent-systems-lab.json) | Fingerprint, identity, tamper-refusal, and field/digest-only diff tests |
| [Agent Trace Lite](https://github.com/jonah-ux/agent-trace-lite) | `agent-trace/v1`, `agent-trace/inspect/v1` | [Owner manifest](https://github.com/jonah-ux/agent-trace-lite/blob/main/conformance/agent-systems-lab.json) | Redaction, raw/redacted digest, safe query, malformed JSONL, and non-object refusal tests |
| [MCP Doctor](https://github.com/jonah-ux/mcp-doctor) | `mcp-doctor/v1` | [Owner manifest](https://github.com/jonah-ux/mcp-doctor/blob/main/conformance/agent-systems-lab.json) | Clean, warning, strict, baseline drift, malformed input, and stable diagnostic-code tests |
| [Worktree Conservator](https://github.com/jonah-ux/worktree-conservator) | `worktree-conservator.result/v1` | [Owner manifest](https://github.com/jonah-ux/worktree-conservator/blob/main/conformance/agent-systems-lab.json) | Disposable scan/plan/apply/verify/audit/restore lifecycle; refusal codes remain owner tests |
| [Slipstream](https://github.com/jonah-ux/slipstream) | `slipstream/query/v1`, `inspect/v1`, `manifest/v1`, `verify/v1` | [Owner manifest](https://github.com/jonah-ux/slipstream/blob/main/conformance/agent-systems-lab.json) | Node self-test proves local query, inspect, deterministic manifest, and tamper-refusing verify |

The matrix proves source-level conformance surfaces and independent local
behavior. It does not claim that every repository is deployed together, that an
external user has adopted the suite, or that a valid receipt proves a
production outcome. For the reproducible install and review sequence, use the
[cold-review checklist](COLD-REVIEW-CHECKLIST.md).
