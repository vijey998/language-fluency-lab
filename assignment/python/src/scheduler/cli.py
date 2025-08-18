import argparse
from .catalog import TaskCatalog
from .engine import SchedulerEngine
from .models import Task,Worker

def demo()->int:
    tasks=[Task("fetch","Fetch data",80,tags=frozenset({"io"})),Task("clean","Clean data",70,dependencies=frozenset({"fetch"})),Task("train","Train model",90,"gpu",dependencies=frozenset({"clean"})),Task("report","Build report",50,dependencies=frozenset({"train"}))]
    catalog=TaskCatalog(tasks); engine=SchedulerEngine(catalog)
    order=engine.run([Worker("local",frozenset({"cpu","gpu"}))],lambda t:print(f"running {t.id}"))
    print("completed:",", ".join(order)); return 0

def main()->int:
    parser=argparse.ArgumentParser(); parser.add_argument("command",choices=["demo"]); args=parser.parse_args(); return demo() if args.command=="demo" else 1
if __name__=="__main__": raise SystemExit(main())
