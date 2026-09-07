"""HTTP client protocol. Native GGUF inference must not depend on this."""

from __future__ import annotations

from typing import Protocol


class HttpClient(Protocol):
    async def get(self, url: str) -> bytes:
        ...

    async def post(self, url: str, body: bytes) -> bytes:
        ...
