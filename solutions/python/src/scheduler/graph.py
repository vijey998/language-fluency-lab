from collections import defaultdict, deque
from .models import Status, Task

class DependencyGraph:
    def __init__(self, tasks: list[Task]) -> None:
        self.tasks={t.id:t for t in tasks}
        for t in tasks:
            missing=t.dependencies-self.tasks.keys()
            if missing: raise KeyError(f"unknown dependencies for {t.id}: {sorted(missing)}")
        self.topological_order()
    def topological_order(self) -> list[str]:
        indegree={tid:0 for tid in self.tasks}; children:dict[str,list[str]]=defaultdict(list)
        for t in self.tasks.values():
            indegree[t.id]=len(t.dependencies)
            for dep in t.dependencies: children[dep].append(t.id)
        queue=deque(sorted(k for k,v in indegree.items() if v==0)); order=[]
        while queue:
            node=queue.popleft(); order.append(node)
            for child in sorted(children[node]):
                indegree[child]-=1
                if indegree[child]==0: queue.append(child)
        if len(order)!=len(self.tasks): raise ValueError("dependency cycle")
        return order
    def ready_ids(self) -> list[str]:
        return [t.id for t in self.tasks.values() if t.status in {Status.PENDING,Status.READY} and all(self.tasks[d].status==Status.SUCCEEDED for d in t.dependencies)]
