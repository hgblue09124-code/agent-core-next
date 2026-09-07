from __future__ import annotations

from typing import Protocol


class Persistence(Protocol):
    def write(self, key: str, data: bytes) -> None:
        ...

    def read(self, key: str) -> bytes | None:
        ...
