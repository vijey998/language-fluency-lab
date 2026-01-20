from collections import defaultdict
from collections.abc import Callable
from dataclasses import dataclass, field
from datetime import datetime, timezone
from threading import Lock
from typing import Any
@dataclass(frozen=True,slots=True)
class Event: name:str; payload:dict[str,Any]; occurred_at:datetime=field(default_factory=lambda: datetime.now(timezone.utc))
class EventBus:
    def __init__(self): self._handlers:dict[str,list[Callable[[Event],None]]]=defaultdict(list); self._lock=Lock()
    def subscribe(self,name:str,handler:Callable[[Event],None])->Callable[[],None]:
        with self._lock:self._handlers[name].append(handler)
        def unsubscribe():
            with self._lock:self._handlers[name].remove(handler)
        return unsubscribe
    def publish(self,event:Event)->None:
        with self._lock: handlers=tuple(self._handlers[event.name])
        for handler in handlers: handler(event)
