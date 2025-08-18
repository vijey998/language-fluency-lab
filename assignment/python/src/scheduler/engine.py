from collections.abc import Callable
from .catalog import TaskCatalog
from .events import Event,EventBus
from .graph import DependencyGraph
from .models import Status,Task,Worker
from .structures import StablePriorityQueue
class SchedulerEngine:
    def __init__(self,catalog:TaskCatalog,bus:EventBus|None=None): self.catalog=catalog; self.bus=bus or EventBus()
    def run(self,workers:list[Worker],handler:Callable[[Task],None]|None=None)->list[str]:
        completed=[]; handler=handler or (lambda _:None)
        while True:
            graph=DependencyGraph(self.catalog.list()); ready=StablePriorityQueue[Task]()
            for tid in graph.ready_ids():
                task=self.catalog.get(tid)
                if task.status==Status.PENDING: self.catalog.upsert(task.transition(Status.READY)); task=self.catalog.get(tid)
                ready.push(task,task.priority)
            if not ready: break
            progressed=False
            while ready:
                task=ready.pop(); worker=next((w for w in workers if w.can_run(task)),None)
                if worker is None: continue
                progressed=True; self.catalog.upsert(task.transition(Status.RUNNING)); self.bus.publish(Event("task.started",{"id":task.id,"worker":worker.id}))
                try: handler(task); done=self.catalog.get(task.id).transition(Status.SUCCEEDED)
                except Exception: done=self.catalog.get(task.id).transition(Status.FAILED)
                self.catalog.upsert(done); self.bus.publish(Event("task.finished",{"id":task.id,"status":done.status})); completed.append(task.id)
            if not progressed: break
        return completed
