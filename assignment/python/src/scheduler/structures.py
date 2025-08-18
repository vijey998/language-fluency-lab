from collections import OrderedDict
from heapq import heappop, heappush
from typing import Generic,TypeVar
T=TypeVar("T"); K=TypeVar("K"); V=TypeVar("V")

class StablePriorityQueue(Generic[T]):
    """Complete this. Higher priority first; equal priority preserves insertion order."""
    def __init__(self): self._heap=[]; self._seq=0
    def push(self,item:T,priority:int)->None:
        # TODO: store a tuple that avoids comparing item values
        raise NotImplementedError
    def pop(self)->T: raise NotImplementedError
    def __bool__(self)->bool: return bool(self._heap)

class LruCache(Generic[K,V]):
    """Fully implemented example of a generic mutable collection wrapper."""
    def __init__(self,capacity:int):
        if capacity<=0: raise ValueError("capacity")
        self.capacity=capacity; self._data:OrderedDict[K,V]=OrderedDict()
    def get(self,key:K)->V|None:
        if key not in self._data:return None
        self._data.move_to_end(key); return self._data[key]
    def put(self,key:K,value:V)->None:
        self._data[key]=value; self._data.move_to_end(key)
        if len(self._data)>self.capacity:self._data.popitem(last=False)

# TODO: implement Trie and BoundedQueue using the contracts in shared-spec.
