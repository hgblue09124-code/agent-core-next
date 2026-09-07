from __future__ import annotations

from typing import Protocol

from Model.Catalog.model_catalog import ModelDescriptor


class ModelStore(Protocol):
    def put(self, descriptor: ModelDescriptor, path: str) -> None:
        ...

    def locate(self, model_id: str) -> str | None:
        ...
