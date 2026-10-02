# Public integration walkthrough

This synthetic flow shows how three independent portfolio tools compose without
sharing private state:

1. **MCP Doctor** checks a server contract and emits a machine-readable report.
2. **Agent Proof** seals that report into an observed, tamper-evident evidence record.
3. **Forgeyard** records the review decision with explicit passing evidence.

The flow uses only the public synthetic fixture in MCP Doctor. It does not read
transcripts, credentials, customer data, provider state, or a real repository.

## Run it locally

Clone the three repositories beside one another, then set these paths:

```bash
export MCP_DOCTOR_ROOT="$PWD/mcp-doctor"
export AGENT_PROOF_ROOT="$PWD/agent-proof"
export FORGEYARD_ROOT="$PWD/forgeyard"
export CONTEXT_INTEGRITY_ROOT="$PWD/context-integrity-lab"
export PYTHON_BIN=python3
workdir="$(mktemp -d)"
```

Run the contract check and save its JSON report:

```bash
PYTHONPATH="$MCP_DOCTOR_ROOT/src" "$PYTHON_BIN" -m mcp_doctor.cli \
  check "$MCP_DOCTOR_ROOT/examples/valid-server.json" --json \
  > "$workdir/mcp.json"
```

Create the small evidence specification that binds the report to the run:

```bash
cat > "$workdir/spec.json" <<'JSON'
{
  "run_id": "portfolio-mcp-check",
  "actor": "portfolio-demo",
  "repository": {
    "url": "https://example.invalid/fixture",
    "branch": "main",
    "commit": "0123456789abcdef0123456789abcdef01234567"
  },
  "operation": {
    "argv": ["mcp-doctor", "check", "valid-server.json", "--json"],
    "cwd": ".",
    "environment": {"PORTFOLIO_DEMO": "true"}
  },
  "result": {
    "exit_code": 0,
    "duration_ms": 1,
    "stdout": "mcp contract passed",
    "stderr": "",
    "observed": true,
    "partial": false,
    "unknowns": []
  },
  "sources": ["mcp.json"],
  "artifacts": [{"path": "mcp.json", "label": "MCP Doctor contract report"}],
  "notes": ["Synthetic public portfolio integration fixture."]
}
JSON
```

Seal and independently verify the report:

```bash
PYTHONPATH="$AGENT_PROOF_ROOT/src" "$PYTHON_BIN" -m agent_proof.cli \
  record "$workdir/spec.json" --artifact-root "$workdir" --out "$workdir/proof.json"
PYTHONPATH="$AGENT_PROOF_ROOT/src" "$PYTHON_BIN" -m agent_proof.cli \
  verify "$workdir/proof.json" --artifact-root "$workdir" \
  --require-observed --require-artifacts
```

Finally, make the review decision explicit in Forgeyard:

```bash
PYTHONPATH="$FORGEYARD_ROOT/src" "$PYTHON_BIN" -m forgeyard.cli create \
  --task-id portfolio-mcp-check \
  --repository fixture \
  --request "review MCP contract" \
  --evidence 'contract=pass:report verified' \
  --evidence 'proof=pass:record verified' \
  --output "$workdir/forgeyard.json"
PYTHONPATH="$FORGEYARD_ROOT/src" "$PYTHON_BIN" -m forgeyard.cli verify \
  "$workdir/forgeyard.json"
```

The meaningful boundary is visible in the output: MCP Doctor proves the
contract shape, Agent Proof proves the integrity of the recorded observation,
and Forgeyard proves only that the supplied review evidence is ready for human
review. None of those records claim deployment, adoption, or a user-visible
outcome.

## Context Integrity Lab to Agent Proof to Forgeyard

The deeper admission path uses the same bounded handoff with a scoped context
fixture. The Context Integrity Lab CLI emits `context-integrity/v1`, Agent Proof
hashes the requested scope and keeps answer text outside the normalized
envelope, and Forgeyard accepts the reviewed `projection.status.ok` field:

```bash
PYTHONPATH="$CONTEXT_INTEGRITY_ROOT" "$PYTHON_BIN" \
  "$CONTEXT_INTEGRITY_ROOT/context_integrity.py" \
  "$CONTEXT_INTEGRITY_ROOT/fixtures/records.json" "Who owns the API?" \
  --person person-a --project project-a --now 2026-10-01T12:00:00Z \
  > "$workdir/context.json"

PYTHONPATH="$AGENT_PROOF_ROOT/src" "$PYTHON_BIN" -m agent_proof.cli \
  normalize "$workdir/context.json" --artifact-root "$workdir" \
  --out "$workdir/context.interop.json"
PYTHONPATH="$AGENT_PROOF_ROOT/src" "$PYTHON_BIN" -m agent_proof.cli \
  verify-interop "$workdir/context.interop.json" \
  --artifact-root "$workdir" --require-input

PYTHONPATH="$FORGEYARD_ROOT/src" "$PYTHON_BIN" -m forgeyard.cli compose \
  --task-id context-admission \
  --repository fixture \
  --request "review admitted context" \
  --input context="$workdir/context.interop.json" \
  --output "$workdir/context-review.json"
```

The final record contains only `schema=agent-proof/interop/v1; ok=true` for
the normalized report. A fresh answer, a refusal, a stale record, or a
source-binding mismatch remains visible in the source-bound readback and cannot
be promoted to a reviewable Forgeyard record by inference.

## Extended interoperability contracts

The same evidence boundary now has three additional synthetic paths on public
main:

- **Sandbox receipt to evaluation:** Agent Sandbox Run emits an
  `agent-sandbox/v2` receipt. Agent Eval Kit consumes the saved receipt through
  `agent-eval/receipt/v1`, checks the receipt digest, exit and timeout state,
  and selected output fragments, and fails closed when the receipt is changed.
  Evaluation does not rerun the command or claim that the sandbox is secure.
- **Recovery trace to bounded query:** Chatlens exports a redacted
  `chatlens-trace-envelope/v1` JSONL document. Agent Trace Lite imports and
  inspects that bounded stream after validating the source/session identity,
  event and envelope digests, row limits, and atomic output ownership. The
  import proves a portable trace shape, not that the original conversation is
  complete or that a user-visible result occurred.
- **Sibling evidence to portable review:** Agent Proof normalizes known policy,
  sandbox, evaluation, trace, context-pack, resume, Context Integrity, and proof
  envelopes into `agent-proof/interop/v1`. Forgeyard then seals verified records and receipts
  into `forgeyard-provenance-packet/v1`, binding the exact source bytes and
  rejecting drift, tampering, unsafe paths, or unknown live source roots.

These contracts are intentionally loss-aware and synthetic. Each downstream
consumer verifies the bytes it received, while the profile keeps package
release status and real-world adoption as separate claims.
