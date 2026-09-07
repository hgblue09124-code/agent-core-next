"""Local GGUF provider boundary.

A future LocalGGUFProvider implementation MUST:

- report backend == InferenceBackend.NATIVE_GGUF
- call NativeInferenceRuntime (in-process)
- never use a network client

This module defines the protocol only. No native runtime is shipped here.
"""

from __future__ import annotations

from typing import Protocol

from Intelligence.Inference.native import NativeInferenceRuntime
from Intelligence.Provider.language_model_provider import (
    InferenceBackend,
    LanguageModelProvider,
)


class LocalGGUFProvider(LanguageModelProvider, Protocol):
    """On-device GGUF provider. Not a network wrapper."""

    @property
    def backend(self) -> InferenceBackend:
        return InferenceBackend.NATIVE_GGUF

    @property
    def inference(self) -> NativeInferenceRuntime:
        ...
