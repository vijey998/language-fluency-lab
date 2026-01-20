from __future__ import annotations
from collections import OrderedDict, deque
from dataclasses import dataclass, field
from heapq import heappop, heappush
from threading import Condition
from typing import Generic, TypeVar
T=TypeVar("T"); K=TypeVar("K"); V=TypeVar("V")

class StablePriorityQueue(Generic[T]):
    def __init__(self)->None: self._heap:list[tuple[int,int,T]]=[]; self._seq=0
    def push(self,item:T,priority:int)->None: heappush(self._heap,(-priority,self._seq,item)); self._seq+=1
    def pop(self)->T: return heappop(self._heap)[2]
    def __bool__(self)->bool: return bool(self._heap)

class LruCache(Generic[K,V]):
    def __init__(self,capacity:int):
        if capacity<=0: raise ValueError("capacity")
        self.capacity=capacity; self._data:OrderedDict[K,V]=OrderedDict()
    def get(self,key:K)->V|None:
        if key not in self._data:return None
        self._data.move_to_end(key); return self._data[key]
    def put(self,key:K,value:V)->None:
        self._data[key]=value; self._data.move_to_end(key)
        if len(self._data)>self.capacity:self._data.popitem(last=False)

@dataclass
class _TrieNode:
    children:dict[str,"_TrieNode"]=field(default_factory=dict); values:set[str]=field(default_factory=set)
class Trie:
    def __init__(self): self.root=_TrieNode()
    def insert(self,text:str,value:str)->None:
        node=self.root
        for ch in text.lower(): node=node.children.setdefault(ch,_TrieNode()); node.values.add(value)
    def prefix(self,prefix:str)->list[str]:
        node=self.root
        for ch in prefix.lower():
            if ch not in node.children:return []
            node=node.children[ch]
        return sorted(node.values)

class BoundedQueue(Generic[T]):
    def __init__(self,capacity:int): self.capacity=capacity; self._q:deque[T]=deque(); self._closed=False; self._cv=Condition()
    def put(self,item:T)->None:
        with self._cv:
            self._cv.wait_for(lambda:len(self._q)<self.capacity or self._closed)
            if self._closed: raise RuntimeError("closed")
            self._q.append(item); self._cv.notify_all()
    def get(self)->T:
        with self._cv:
            self._cv.wait_for(lambda:self._q or self._closed)
            if not self._q: raise RuntimeError("closed")
            item=self._q.popleft(); self._cv.notify_all(); return item
    def close(self)->None:
        with self._cv:self._closed=True; self._cv.notify_all()
