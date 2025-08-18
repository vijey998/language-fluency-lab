#pragma once
#include "model.hpp"
#include <functional>
#include <map>
#include <optional>
#include <vector>
namespace scheduler {
class TaskCatalog {
 std::unordered_map<std::string,Task> tasks_;
public:
 void add(Task task); Task const& get(std::string const& id) const; Task& get_mut(std::string const& id); bool remove(std::string const& id);
 [[nodiscard]] std::vector<std::reference_wrapper<Task const>> list() const;
 [[nodiscard]] std::vector<std::reference_wrapper<Task const>> by_status(Status s) const;
 [[nodiscard]] std::vector<std::reference_wrapper<Task const>> sorted_by_priority() const;
 [[nodiscard]] std::map<Status,std::vector<std::string>> grouped_ids() const;
};
}
