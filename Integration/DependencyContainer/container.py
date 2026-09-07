"""Explicit wiring. No process-global singleton."""

from __future__ import annotations

from dataclasses import dataclass

from Core.Runtime.agent_runtime import AgentRuntime
from Execution.Executor.action_executor import ActionExecutor
from Execution.Planner.planner import Planner
from Execution.Verification.outcome_verifier import OutcomeVerifier
from Intelligence.Inference.engine import InferenceEngine
from Intelligence.Provider.language_model_provider import LanguageModelProvider
from Memory.Retrieval.memory_retriever import MemoryRetriever
from Memory.Store.memory_store import MemoryStore
from Model.Catalog.model_catalog import ModelCatalog
from Model.Storage.model_store import ModelStore


@dataclass(frozen=True)
class DependencyContainer:
    runtime: AgentRuntime
    provider: LanguageModelProvider
    inference: InferenceEngine
    planner: Planner
    executor: ActionExecutor
    verifier: OutcomeVerifier
    memory_store: MemoryStore
    memory_retriever: MemoryRetriever
    model_catalog: ModelCatalog
    model_store: ModelStore
