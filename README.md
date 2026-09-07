# Agent Core Next

Agent Core is a modular agent runtime designed around strict responsibility
boundaries. Model inference, execution, memory, model lifecycle, and
infrastructure are independently replaceable components.

This repository is the next-generation foundation. It is **not** a copy of
`hgblue09124-code/agent-core`. Legacy master is reference-only; components are
ported later, rewritten to fit these boundaries.

Native GGUF inference is a **future** implementation under the
`Intelligence/Inference` boundary. It is not present in this initial commit,
and it will never be implemented as HTTP-to-Ollama.

## Architecture

```
Core            Agent, Runtime, Contracts
Intelligence    Model abstraction, Provider, Inference, Prompt
Model           Catalog → Download → Validation → Storage
Execution       Planner → Executor → Verification
Memory          Store, Retrieval
Infrastructure  Networking, Persistence, Logging, Platform
Integration     Dependency injection / wiring
```

Dependency direction is one-way:

```
Core → domain abstractions → concrete implementations → Infrastructure
```

Never reverse it.

## Boundaries (enforced)

| Rule | Meaning |
| --- | --- |
| Download ≠ Inference | Model lifecycle does not run models |
| Inference ≠ Runtime | Runtime orchestrates; it does not own GGUF |
| Planner ≠ Executor | Planner decides; Executor executes |
| Executor ≠ Verification | Verifier is a separate step |
| Memory ≠ Runtime | Memory is not inside AgentRuntime |
| Provider ≠ Agent | Providers are Intelligence, not Core |
| Infrastructure ≠ Core | Platform I/O stays out of Core |
| Native ≠ HTTP | Local GGUF is in-process, never Ollama-over-HTTP |

See [Documentation/Architecture.md](Documentation/Architecture.md).

## Status

Initial architecture only: compile-safe protocols, no fake native inference,
no hidden Ollama/HTTP local path.

```bash
pip install -e ".[dev]"
pytest
```
