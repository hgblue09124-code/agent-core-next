from __future__ import annotations

from typing import Protocol, Sequence

from Core.Contracts.action import Action


class Planner(Protocol):
    """Decides. Does not execute."""

    async def plan(self, goal: str) -> Sequence[Action]:
        ...
