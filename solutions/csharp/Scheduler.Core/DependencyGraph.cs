namespace Scheduler.Core;
public sealed class DependencyGraph(TaskCatalog catalog)
{
 public IReadOnlyList<string> TopologicalOrder(){var degree=catalog.All.ToDictionary(t=>t.Id,_=>0);var children=new Dictionary<string,List<string>>();foreach(var t in catalog.All)foreach(var d in t.Dependencies){if(!degree.ContainsKey(d))throw new ArgumentException($"unknown {d}");degree[t.Id]++;if(!children.TryGetValue(d,out var list))children[d]=list=[];list.Add(t.Id);}var q=new PriorityQueue<string,string>(StringComparer.Ordinal);foreach(var (id,n) in degree)if(n==0)q.Enqueue(id,id);var result=new List<string>();while(q.TryDequeue(out var id,out _)){result.Add(id);if(!children.TryGetValue(id,out var cs))continue;foreach(var c in cs.Order(StringComparer.Ordinal))if(--degree[c]==0)q.Enqueue(c,c);}return result.Count==degree.Count?result:throw new InvalidOperationException("cycle");}
 public IEnumerable<string> ReadyIds()=>catalog.All.Where(t=>t.Status is Status.Pending or Status.Ready&&t.Dependencies.All(d=>catalog[d].Status==Status.Succeeded)).Select(t=>t.Id);
}
