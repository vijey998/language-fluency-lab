from scheduler import *
from scheduler.structures import LruCache,StablePriorityQueue,Trie

def test_task_validation_and_transition():
    t=Task("a","A"); assert t.transition(Status.READY).status==Status.READY

def test_graph_and_engine():
    c=TaskCatalog([Task("a","A",10),Task("b","B",99,dependencies=frozenset({"a"}))]); e=SchedulerEngine(c)
    assert e.run([Worker("w",frozenset({"cpu"}))])==["a","b"]

def test_structures():
    q=StablePriorityQueue[str](); q.push("low",1); q.push("high",9); assert [q.pop(),q.pop()]==["high","low"]
    c=LruCache[str,int](2); c.put("a",1); c.put("b",2); c.get("a"); c.put("c",3); assert c.get("b") is None
    t=Trie(); t.insert("alpha","1"); t.insert("alpine","2"); assert t.prefix("alp")==["1","2"]
