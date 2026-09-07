import inspect

from Integration.DependencyContainer import DependencyContainer


def test_container_is_explicit_dataclass():
    fields = {f for f in DependencyContainer.__dataclass_fields__}
    assert "runtime" in fields
    assert "provider" in fields
    assert "inference" in fields
    assert "planner" in fields
    assert "executor" in fields
    assert "verifier" in fields
    assert "memory_store" in fields
    assert "memory_retriever" in fields
    assert "model_catalog" in fields
    assert "model_store" in fields


def test_container_is_not_a_singleton_module():
    source = inspect.getsource(DependencyContainer)
    assert "singleton" not in source.lower()
