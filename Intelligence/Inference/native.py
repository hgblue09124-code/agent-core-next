"""Native in-process inference runtime.

Future GGUF bindings implement this protocol.
This file must stay free of network clients and third-party shims.
No fake native implementation lives here.
"""

from __future__ import annotations

from typing import Protocol

from Intelligence.Inference.engine import InferenceEngine


class NativeInferenceRuntime(InferenceEngine, Protocol):
    """In-process GGUF runtime. Implementations must not open sockets."""

    @property
    def is_native(self) -> bool:
        return True
