from Intelligence.Provider import InferenceBackend, LanguageModelProvider, LocalGGUFProvider
from Intelligence.Inference import InferenceEngine, NativeInferenceRuntime


def test_native_and_remote_are_distinct():
    assert InferenceBackend.NATIVE_GGUF != InferenceBackend.REMOTE
    assert InferenceBackend.NATIVE_GGUF.value == "native_gguf"


def test_protocols_are_importable():
    assert LanguageModelProvider is not None
    assert LocalGGUFProvider is not None
    assert InferenceEngine is not None
    assert NativeInferenceRuntime is not None
