from __future__ import annotations

from dataclasses import dataclass, field
from typing import Mapping


@dataclass(frozen=True)
class Action:
    """A planned unit of work. Planner produces these; Executor runs them."""

    name: str
    capability_id: str
    input: Mapping[str, object] = field(default_factory=dict)
