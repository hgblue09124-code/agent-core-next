from __future__ import annotations

from typing import Protocol, Sequence


class PromptBuilder(Protocol):
    def build(self, goal: str, context: Sequence[str] = ()) -> str:
        ...
