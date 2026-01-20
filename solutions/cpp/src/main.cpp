#include "scheduler/engine.hpp"
#include <iostream>
using namespace scheduler;
int main(int argc,char**argv){if(argc<2||std::string_view(argv[1])!="demo"){std::cerr<<"usage: scheduler_cli demo\n";return 2;}TaskCatalog c;Task a{"fetch","Fetch",80};Task b{"clean","Clean",70};b.dependencies.insert("fetch");Task d{"train","Train",90,"gpu"};d.dependencies.insert("clean");c.add(std::move(a));c.add(std::move(b));c.add(std::move(d));SchedulerEngine e(c);auto done=e.run({Worker{"local",{"cpu","gpu"}}},[](Task const&t){std::cout<<"running "<<t.id<<'\n';});std::cout<<done.size()<<" completed\n";}
