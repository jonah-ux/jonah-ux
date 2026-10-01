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
