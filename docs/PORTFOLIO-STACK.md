# End-to-end agent reliability stack

This is the larger cross-project example behind the portfolio: a disposable workflow that recovers context, indexes the recovered facts, binds the outputs to an observed proof, preserves the Git worktree, and hands the combined evidence to Forgeyard for review.

The stack is intentionally synthetic. It never reads a real transcript store, changes a user's repository, sends a provider request, or claims deployment or adoption.

## Run it

Check out the released tags beside one another:

```console
git clone --branch v0.3.0 https://github.com/jonah-ux/chatlens.git
 git clone --branch v0.2.0 https://github.com/jonah-ux/slipstream.git
 git clone --branch v0.2.0 https://github.com/jonah-ux/agent-proof.git
 git clone --branch v0.2.0 https://github.com/jonah-ux/worktree-conservator.git
 git clone --branch v0.3.0 https://github.com/jonah-ux/forgeyard.git
```

Install the Python packages in a virtual environment and build Slipstream's native dependencies according to its README. Then run:

```console
export CHATLENS_ROOT="$PWD/chatlens"
export SLIPSTREAM_ROOT="$PWD/slipstream"
export AGENT_PROOF_ROOT="$PWD/agent-proof"
export WORKTREE_ROOT="$PWD/worktree-conservator"
export FORGEYARD_ROOT="$PWD/forgeyard"
./jonah-ux/docs/integration/portfolio-stack-demo.sh
```

The final JSON reports the meaningful boundaries:

- Chatlens recovery envelope valid and identity-matched.
- Slipstream nearest-neighbor result plus manifest verification.
- Agent Proof observed record verified with artifact hashes.
- Worktree Conservator archive verification and restore.
- Forgeyard review record ready for a human reviewer.

The components remain independently installable and independently owned; this script is a reference consumer, not a new runtime or shared registry.
