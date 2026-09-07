"""Remote / HTTP providers (OpenAI-compatible, Ollama, etc.).

Ollama belongs here. It is not native GGUF inference.
"""

from __future__ import annotations

from typing import Protocol

from Intelligence.Provider.language_model_provider import (
    InferenceBackend,
    LanguageModelProvider,
)


class RemoteLanguageModelProvider(LanguageModelProvider, Protocol):
    @property
    def backend(self) -> InferenceBackend:
        return InferenceBackend.REMOTE
