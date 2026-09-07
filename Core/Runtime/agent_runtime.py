"""AgentRuntime protocol.

Runtime orchestrates. It does not own inference, downloads, memory
persistence, or platform I/O. Collaborators are injected by Integration.

Future call path (runtime, not import of implementations):

    AgentRuntime → LanguageModelProvider → LocalGGUFProvider
                 → InferenceEngine → NativeInferenceRuntime → GGUF
"""

from __future__ import annotations

from typing import Protocol

from Core.Contracts.execution_result import ExecutionResult


class AgentRuntime(Protocol):
    async def run(self, goal: str) -> ExecutionResult:
        ...

    async def resume(self, run_id: str) -> ExecutionResult:
        ...
