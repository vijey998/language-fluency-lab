#pragma once
#include "graph.hpp"
#include "structures.hpp"
#include <functional>
namespace scheduler { class SchedulerEngine { TaskCatalog& catalog_; public: explicit SchedulerEngine(TaskCatalog& c):catalog_(c){} std::vector<std::string> run(std::vector<Worker> const&,std::function<void(Task const&)> handler={}); }; }
