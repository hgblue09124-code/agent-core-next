from __future__ import annotations

from typing import Protocol


class Platform(Protocol):
    """OS/app sandbox paths and clocks. Core does not import concrete APIs."""

    def data_dir(self) -> str:
        ...
