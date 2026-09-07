"""Provider abstraction. Runtime talks to this protocol, never to GGUF/HTTP."""

from __future__ import annotations

from enum import Enum
from typing import Protocol

from Intelligence.Inference.engine import InferenceRequest, InferenceResponse


class InferenceBackend(str, Enum):
    """NATIVE_GGUF is in-process. REMOTE is any network provider, including Ollama."""

    NATIVE_GGUF = "native_gguf"
    REMOTE = "remote"


class LanguageModelProvider(Protocol):
    @property
    def provider_id(self) -> str:
        ...

    @property
    def backend(self) -> InferenceBackend:
        ...

    async def complete(self, request: InferenceRequest) -> InferenceResponse:
        ...
