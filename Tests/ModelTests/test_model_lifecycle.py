from Model.Catalog import ModelCatalog, ModelDescriptor
from Model.Download import ModelDownloader, ModelValidator
from Model.Storage import ModelStore
from Tests.architecture import imported_tops


def test_lifecycle_protocols_exist():
    assert ModelCatalog is not None
    assert ModelDownloader is not None
    assert ModelValidator is not None
    assert ModelStore is not None
    descriptor = ModelDescriptor(id="example", filename="example.gguf")
    assert descriptor.filename.endswith(".gguf")


def test_model_does_not_import_inference():
    tops = imported_tops("Model")
    assert "Intelligence" not in tops
    assert "Core" not in tops
    assert "Execution" not in tops
