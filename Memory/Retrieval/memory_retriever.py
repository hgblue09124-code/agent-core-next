from __future__ import annotations

from typing import Protocol, Sequence

from Memory.Store.memory_store import MemoryRecord


class MemoryRetriever(Protocol):
    def retrieve(self, query: str, limit: int = 5) -> Sequence[MemoryRecord]:
        ...
