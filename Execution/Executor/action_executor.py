from __future__ import annotations

from typing import Protocol

from Core.Contracts.action import Action
from Core.Contracts.execution_result import ExecutionResult


class ActionExecutor(Protocol):
    """Executes. Does not plan or verify."""

    async def execute(self, action: Action) -> ExecutionResult:
        ...
