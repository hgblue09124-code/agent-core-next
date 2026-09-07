from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class LanguageModel:
    """Logical model identity used at inference time. Not a file on disk."""

    id: str
    display_name: str
