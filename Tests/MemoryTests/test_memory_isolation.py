from Memory.Store import MemoryStore
from Memory.Retrieval import MemoryRetriever
from Tests.architecture import imported_tops


def test_memory_protocols_exist():
    assert MemoryStore is not None
    assert MemoryRetriever is not None


def test_memory_does_not_import_runtime():
    tops = imported_tops("Memory")
    assert "Infrastructure" not in tops
    assert "Intelligence" not in tops
    assert "Model" not in tops
    # Memory may use Core.Contracts only
    assert imported_tops("Memory") <= {"Memory", "Core"}
