#include "scheduler/engine.hpp"
#include <cassert>
#include <iostream>
using namespace scheduler;
int main(){TaskCatalog c;Task a{"a","A",10};Task b{"b","B",99};b.dependencies.insert("a");c.add(a);c.add(b);auto order=DependencyGraph(c).topological_order();assert((order==std::vector<std::string>{"a","b"}));SchedulerEngine e(c);auto done=e.run({Worker{"w",{"cpu"}}});assert((done==std::vector<std::string>{"a","b"}));StablePriorityQueue<std::string> q;q.push("low",1);q.push("high",9);assert(q.pop()=="high");LruCache<std::string,int> cache(2);cache.put("a",1);cache.put("b",2);cache.get("a");cache.put("c",3);assert(!cache.get("b"));std::cout<<"ok\n";}
