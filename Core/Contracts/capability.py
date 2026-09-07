from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Capability:
    """Named ability the agent may invoke. Core does not implement it."""

    id: str
    name: str
    mutating: bool = False
