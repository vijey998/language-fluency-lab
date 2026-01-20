#pragma once
#include "catalog.hpp"
#include <vector>
namespace scheduler { class DependencyGraph { TaskCatalog const& catalog_; public: explicit DependencyGraph(TaskCatalog const& c):catalog_(c){} [[nodiscard]] std::vector<std::string> topological_order() const; [[nodiscard]] std::vector<std::string> ready_ids() const; }; }
