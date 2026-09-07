from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Mapping


class ExecutionStatus(str, Enum):
    SUCCESS = "SUCCESS"
    FAILED = "FAILED"
    DENIED = "DENIED"
    NOT_EXECUTED = "NOT_EXECUTED"


@dataclass(frozen=True)
class ExecutionResult:
    status: ExecutionStatus
    output: str = ""
    details: Mapping[str, object] = field(default_factory=dict)
