"""Agent protocol — identity + run. No providers, no I/O."""

from __future__ import annotations

from typing import Protocol

from Core.Contracts.execution_result import ExecutionResult


class Agent(Protocol):
    """Top-level agent. Implementations are wired in Integration."""

    @property
    def agent_id(self) -> str:
        ...

    async def run(self, goal: str) -> ExecutionResult:
        ...
