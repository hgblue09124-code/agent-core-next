from __future__ import annotations

from dataclasses import dataclass, field
from typing import Mapping, Protocol, Sequence


@dataclass(frozen=True)
class InferenceRequest:
    prompt: str
    messages: Sequence[Mapping[str, str]] = field(default_factory=tuple)
    max_tokens: int | None = None


@dataclass(frozen=True)
class InferenceResponse:
    text: str
    finish_reason: str | None = None


class InferenceEngine(Protocol):
    """Runs a completion. Native and remote engines both satisfy this."""

    async def infer(self, request: InferenceRequest) -> InferenceResponse:
        ...
