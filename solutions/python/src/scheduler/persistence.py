from dataclasses import asdict
from datetime import datetime
import json
from pathlib import Path
from .models import Status,Task
class JsonTaskRepository:
    def __init__(self,path:Path): self.path=path
    def save(self,tasks:list[Task])->None:
        rows=[]
        for t in tasks:
            d=asdict(t); d["dependencies"]=sorted(t.dependencies); d["tags"]=sorted(t.tags); d["payload"]=dict(t.payload); d["created_at"]=t.created_at.isoformat(); d["status"]=t.status.value; rows.append(d)
        self.path.write_text(json.dumps(rows,indent=2))
    def load(self)->list[Task]:
        if not self.path.exists(): return []
        return [Task(**{**d,"dependencies":frozenset(d["dependencies"]),"tags":frozenset(d["tags"]),"created_at":datetime.fromisoformat(d["created_at"]),"status":Status(d["status"])}) for d in json.loads(self.path.read_text())]
