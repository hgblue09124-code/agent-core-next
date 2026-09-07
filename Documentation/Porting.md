# Porting from legacy agent-core

Legacy: `hgblue09124-code/agent-core` (reference only). Do not copy its tree.

Worth considering later, rewritten into these modules:

- contracts (Action, Capability, ExecutionResult)
- model metadata / catalog
- download validation
- storage logic
- capability definitions
- execution logic split into Planner / Executor / Verification
- memory abstractions
- tests that represent real behavior

Do not port:

- dual Python + Swift runtimes as competing sources of truth
- multiple overlapping orchestrators
- GGUFChatProvider / LocalPlannerProvider that route "local" through HTTP/Ollama
- console HTTP server inside Core
- SwiftUI, IPA packaging, constitution JSON, experience/learning pipelines
- mock-default planner disguised as inference

When a component is ported, rewrite it to the new boundary. Do not preserve
coupling for compatibility.
