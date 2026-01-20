from __future__ import annotations
from collections import defaultdict
from collections.abc import Callable, Iterable
from .models import Status, Task

class TaskCatalog:
    def __init__(self, tasks: Iterable[Task]=()) -> None:
        self._tasks: dict[str, Task] = {}
        for task in tasks: self.add(task)
    def add(self, task: Task) -> None:
        if task.id in self._tasks: raise KeyError(f"duplicate task: {task.id}")
        self._tasks[task.id]=task
    def get(self, task_id: str) -> Task: return self._tasks[task_id]
    def upsert(self, task: Task) -> None: self._tasks[task.id]=task
    def remove(self, task_id: str) -> Task: return self._tasks.pop(task_id)
    def list(self) -> list[Task]: return list(self._tasks.values())
    def filter(self, *, status: Status|None=None, tag: str|None=None, capability: str|None=None) -> list[Task]:
        return [t for t in self._tasks.values() if (status is None or t.status==status) and (tag is None or tag in t.tags) and (capability is None or t.required_capability==capability)]
    def sorted(self, key: str="priority") -> list[Task]:
        keys: dict[str,Callable[[Task],object]]={"priority":lambda t:(-t.priority,t.created_at,t.id),"name":lambda t:(t.name.lower(),t.id),"created":lambda t:(t.created_at,t.id)}
        if key not in keys: raise ValueError(f"unknown sort: {key}")
        return sorted(self._tasks.values(), key=keys[key])
    def grouped_by_status(self) -> dict[Status,list[Task]]:
        out: dict[Status,list[Task]]=defaultdict(list)
        for task in self._tasks.values(): out[task.status].append(task)
        return dict(out)
