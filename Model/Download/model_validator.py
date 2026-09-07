from __future__ import annotations

from typing import Protocol

from Model.Catalog.model_catalog import ModelDescriptor


class ModelValidator(Protocol):
    def validate(self, path: str, descriptor: ModelDescriptor) -> bool:
        ...
