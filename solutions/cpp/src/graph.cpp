#include "scheduler/graph.hpp"
#include <algorithm>
#include <deque>
#include <unordered_map>
namespace scheduler {
std::vector<std::string> DependencyGraph::topological_order()const{auto tasks=catalog_.list();std::unordered_map<std::string,int> degree;std::unordered_map<std::string,std::vector<std::string>> children;for(auto r:tasks)degree[r.get().id]=0;for(auto r:tasks){for(auto const&d:r.get().dependencies){if(!degree.contains(d))throw std::invalid_argument("unknown dependency");++degree[r.get().id];children[d].push_back(r.get().id);}}std::vector<std::string> zeros;for(auto const&[id,n]:degree)if(n==0)zeros.push_back(id);std::ranges::sort(zeros);std::deque<std::string> q(zeros.begin(),zeros.end());std::vector<std::string> out;while(!q.empty()){auto id=q.front();q.pop_front();out.push_back(id);auto& cs=children[id];std::ranges::sort(cs);for(auto const&c:cs)if(--degree[c]==0)q.push_back(c);}if(out.size()!=tasks.size())throw std::logic_error("cycle");return out;}
std::vector<std::string> DependencyGraph::ready_ids()const{std::vector<std::string> out;for(auto r:catalog_.list()){auto const&t=r.get();if(t.status!=Status::pending&&t.status!=Status::ready)continue;bool ready=std::ranges::all_of(t.dependencies,[&](auto const&d){return catalog_.get(d).status==Status::succeeded;});if(ready)out.push_back(t.id);}return out;}
}
