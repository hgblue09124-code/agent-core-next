from __future__ import annotations

from typing import Protocol

from Core.Contracts.action import Action
from Core.Contracts.execution_result import ExecutionResult


class OutcomeVerifier(Protocol):
    """Verifies. Does not plan or execute."""

    def verify(self, action: Action, result: ExecutionResult) -> bool:
        ...
