#pragma once
#include <chrono>
#include <compare>
#include <stdexcept>
#include <string>
#include <unordered_map>
#include <unordered_set>
namespace scheduler {
enum class Status { pending, ready, running, succeeded, failed, cancelled };
struct Task {
 std::string id,name; int priority{50}; std::string capability{"cpu"}; int estimated_ms{1};
 std::unordered_set<std::string> dependencies,tags; std::unordered_map<std::string,std::string> payload; Status status{Status::pending};
 Task(std::string id_,std::string name_,int p=50,std::string cap="cpu",int ms=1):id(std::move(id_)),name(std::move(name_)),priority(p),capability(std::move(cap)),estimated_ms(ms){
  if(id.empty()||name.empty()) throw std::invalid_argument("id/name"); if(priority<0||priority>100) throw std::invalid_argument("priority"); if(ms<=0) throw std::invalid_argument("estimated_ms"); }
 bool operator==(Task const& other) const noexcept { return id==other.id; }
 Task transitioned(Status target) const;
};
struct TaskHash { std::size_t operator()(Task const& t) const noexcept { return std::hash<std::string>{}(t.id); } };
struct Worker { std::string id; std::unordered_set<std::string> capabilities; [[nodiscard]] bool can_run(Task const& t) const { return capabilities.contains(t.capability); } };
}
