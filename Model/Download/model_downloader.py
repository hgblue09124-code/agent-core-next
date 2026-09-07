"""Download is not inference. Implementations use Infrastructure Networking."""

from __future__ import annotations

from typing import Protocol

from Model.Catalog.model_catalog import ModelDescriptor


class ModelDownloader(Protocol):
    async def download(self, descriptor: ModelDescriptor, destination: str) -> str:
        ...
