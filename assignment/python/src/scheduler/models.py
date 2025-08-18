from __future__ import annotations
from dataclasses import dataclass, field, replace
from datetime import datetime, timezone
from enum import StrEnum
from types import MappingProxyType
from typing import Any, Mapping

class Status(StrEnum):
    PENDING="pending"; READY="ready"; RUNNING="running"; SUCCEEDED="succeeded"; FAILED="failed"; CANCELLED="cancelled"

_ALLOWED = {
    Status.PENDING:{Status.READY,Status.CANCELLED}, Status.READY:{Status.RUNNING,Status.CANCELLED},
    Status.RUNNING:{Status.SUCCEEDED,Status.FAILED,Status.CANCELLED}, Status.FAILED:{Status.READY,Status.CANCELLED},
    Status.SUCCEEDED:set(), Status.CANCELLED:set(),
}

@dataclass(frozen=True, slots=True)
class Task:
    id: str
    name: str
    priority: int = 50
    required_capability: str = "cpu"
    estimated_ms: int = 1
    dependencies: frozenset[str] = field(default_factory=frozenset)
    tags: frozenset[str] = field(default_factory=frozenset)
    payload: Mapping[str, Any] = field(default_factory=dict, compare=False, hash=False)
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    status: Status = Status.PENDING

    def __post_init__(self) -> None:
        if not self.id.strip() or not self.name.strip(): raise ValueError("id and name are required")
        if not 0 <= self.priority <= 100: raise ValueError("priority must be 0..100")
        if self.estimated_ms <= 0: raise ValueError("estimated_ms must be positive")
        if self.id in self.dependencies: raise ValueError("self dependency")
        object.__setattr__(self, "payload", MappingProxyType(dict(self.payload)))

    def transition(self, target: Status) -> Task:
        if target not in _ALLOWED[self.status]: raise ValueError(f"invalid transition {self.status}->{target}")
        return replace(self, status=target)

@dataclass(frozen=True, slots=True)
class Worker:
    id: str
    capabilities: frozenset[str]
    def can_run(self, task: Task) -> bool: return task.required_capability in self.capabilities
