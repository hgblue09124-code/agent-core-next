from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol


@dataclass(frozen=True)
class MemoryRecord:
    id: str
    content: str


class MemoryStore(Protocol):
    def put(self, record: MemoryRecord) -> None:
        ...

    def get(self, memory_id: str) -> MemoryRecord | None:
        ...
