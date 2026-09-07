from Tests.architecture import imported_tops


def test_core_does_not_import_model_or_infrastructure():
    tops = imported_tops("Core")
    assert "Model" not in tops
    assert "Infrastructure" not in tops
    assert "Integration" not in tops


def test_core_does_not_import_execution_or_memory_or_intelligence():
    """Core owns contracts only; collaborators are injected later."""
    tops = imported_tops("Core")
    assert "Execution" not in tops
    assert "Memory" not in tops
    assert "Intelligence" not in tops
