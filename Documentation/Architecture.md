# Architecture

Concise map of module responsibilities and the future native GGUF path.

## Module responsibilities

**Core** owns Agent, Runtime, and contracts. It orchestrates. It does not own
HTTP, GGUF, Ollama, filesystem implementations, downloads, memory persistence,
or execution implementations.

**Intelligence** owns language-model, provider, inference, and prompt
abstractions.

```
LanguageModelProvider → InferenceEngine → Native | Remote implementation
```

**Model** owns lifecycle only:

```
Catalog → Download → Validation → Storage
```

Model management must not perform inference.

**Execution** is three modules, not one manager:

```
Planner decides → Executor executes → Verifier verifies
```

**Memory** is Store and Retrieval. It is not part of AgentRuntime.

**Infrastructure** holds platform-specific networking, persistence, logging,
and platform APIs. These must not leak into Core.

**Integration** wires concrete implementations through dependency injection.
No hidden globals. No unnecessary singletons.

**Tests** are split by the same boundaries. **Benchmarks** stay outside
production runtime and must never become part of AgentRuntime or Core.

## Dependency direction

```
Core
  ↓
Domain abstractions
  ↓
Concrete implementations
  ↓
Infrastructure
```

Allowed at the protocol level:

- Core contracts are imported by every domain.
- Core Runtime may accept Intelligence / Execution / Memory **protocols** via
  injection. It must not import their implementations.
- Intelligence Provider may depend on Intelligence Inference protocols.
- Model Download may depend on Infrastructure Networking protocols.
- Integration may depend on everything, because it is the composition root.

Forbidden:

- Core → Infrastructure implementations
- Core → Model lifecycle
- Intelligence → Model.Download / Model.Storage implementations
- Model → Intelligence.Inference
- Native inference → HTTP / Ollama
- Benchmarks → Core runtime

## Provider boundary

`LanguageModelProvider` is the only type Runtime talks to for language models.

Two backend kinds exist and must not be confused:

- `NATIVE_GGUF` — in-process native inference. No HTTP.
- `REMOTE` — network providers (OpenAI-compatible, Ollama, etc.).

Ollama is a remote provider. It is not native inference. A local GGUF provider
must use `NativeInferenceRuntime`, never an HTTP client.

## Model lifecycle

Catalog lists available models. Download fetches bytes. Validation checks
integrity. Storage persists the artifact. None of these steps run a model.

## Execution lifecycle

Planner produces an ordered list of actions. Executor runs one action.
OutcomeVerifier judges the result. These remain three replaceable modules.

## Memory boundary

`MemoryStore` writes. `MemoryRetriever` reads/searches. Runtime may call both
through injected protocols. Memory implementations live outside Core.

## Future native GGUF path

```
Core/Runtime
      ↓
Intelligence/Provider
      ↓
LocalGGUFProvider          (not implemented yet)
      ↓
Intelligence/Inference
      ↓
NativeInferenceRuntime     (protocol only)
      ↓
GGUF
```

Not this:

```
.onDevice → HTTP → Ollama
```

No native GGUF implementation ships in this commit. The boundary exists so a
later agent can add it without reversing dependencies.
