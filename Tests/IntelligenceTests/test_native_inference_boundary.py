from pathlib import Path

from Tests.architecture import ROOT, files_under, imported_tops

FORBIDDEN_NATIVE = ("ollama", "llama_cpp", "http.client", "urllib", "requests")


def test_native_inference_has_no_http_or_ollama():
    for path in files_under("Intelligence", "Inference"):
        text = path.read_text(encoding="utf-8").lower()
        for token in ("ollama", "llama_cpp", "urllib", "http.client"):
            assert token not in text, f"{path} must not mention {token}"
    tops = imported_tops("Intelligence", "Inference")
    assert "Infrastructure" not in tops
    assert "Model" not in tops


def test_no_fake_gguf_implementation():
    inf = ROOT / "Intelligence" / "Inference"
    assert not list(inf.rglob("*gguf*"))
    assert not list(inf.rglob("*llama*"))


def test_local_gguf_provider_is_protocol_only():
    source = (ROOT / "Intelligence" / "Provider" / "local_gguf.py").read_text(encoding="utf-8")
    assert "class LocalGGUFProvider" in source
    assert "Protocol" in source
    assert "ollama" not in source.lower()
