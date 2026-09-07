from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol, Sequence


@dataclass(frozen=True)
class ModelDescriptor:
    id: str
    filename: str
    sha256: str | None = None


class ModelCatalog(Protocol):
    def list_models(self) -> Sequence[ModelDescriptor]:
        ...

    def get(self, model_id: str) -> ModelDescriptor | None:
        ...
