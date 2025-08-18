#include "scheduler/catalog.hpp"
#include <algorithm>
namespace scheduler {
Task Task::transitioned(Status target) const { bool ok=(status==Status::pending&&(target==Status::ready||target==Status::cancelled))||(status==Status::ready&&(target==Status::running||target==Status::cancelled))||(status==Status::running&&(target==Status::succeeded||target==Status::failed||target==Status::cancelled))||(status==Status::failed&&(target==Status::ready||target==Status::cancelled)); if(!ok)throw std::logic_error("invalid transition");auto c=*this;c.status=target;return c; }
void TaskCatalog::add(Task t){if(tasks_.contains(t.id))throw std::invalid_argument("duplicate");tasks_.emplace(t.id,std::move(t));}
Task const& TaskCatalog::get(std::string const&id)const{return tasks_.at(id);} Task& TaskCatalog::get_mut(std::string const&id){return tasks_.at(id);} bool TaskCatalog::remove(std::string const&id){return tasks_.erase(id)>0;}
std::vector<std::reference_wrapper<Task const>> TaskCatalog::list()const{std::vector<std::reference_wrapper<Task const>> out;for(auto const&[_,t]:tasks_)out.push_back(std::cref(t));return out;}
std::vector<std::reference_wrapper<Task const>> TaskCatalog::by_status(Status s)const{auto all=list();std::erase_if(all,[&](auto r){return r.get().status!=s;});return all;}
std::vector<std::reference_wrapper<Task const>> TaskCatalog::sorted_by_priority()const{auto out=list();std::ranges::sort(out,{},[](auto r){return std::pair{-r.get().priority,r.get().id};});return out;}
std::map<Status,std::vector<std::string>> TaskCatalog::grouped_ids()const{std::map<Status,std::vector<std::string>> out;for(auto const&[id,t]:tasks_)out[t.status].push_back(id);return out;}
}
