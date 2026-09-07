"""Import-graph helpers for architecture tests. Not production runtime."""

from __future__ import annotations

import ast
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

TOP = (
    "Core",
    "Intelligence",
    "Model",
    "Execution",
    "Memory",
    "Infrastructure",
    "Integration",
)


def module_imports(path: Path) -> set[str]:
    tree = ast.parse(path.read_text(encoding="utf-8"))
    found: set[str] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                found.add(alias.name.split(".")[0])
        elif isinstance(node, ast.ImportFrom) and node.module:
            found.add(node.module.split(".")[0])
    return found


def files_under(*parts: str) -> list[Path]:
    base = ROOT.joinpath(*parts)
    return [p for p in base.rglob("*.py") if p.is_file()]


def imported_tops(*parts: str) -> set[str]:
    tops: set[str] = set()
    for path in files_under(*parts):
        tops |= {name for name in module_imports(path) if name in TOP}
    return tops
