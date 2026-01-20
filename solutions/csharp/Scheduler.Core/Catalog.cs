namespace Scheduler.Core;
public sealed class TaskCatalog(IEnumerable<WorkTask>? seed=null)
{
 private readonly Dictionary<string,WorkTask> _tasks=new(StringComparer.Ordinal);
 public TaskCatalog():this(null){} public TaskCatalog(IEnumerable<WorkTask>? seed):this(){if(seed is not null)foreach(var t in seed)Add(t);}
 public void Add(WorkTask task){task.Validate();if(!_tasks.TryAdd(task.Id,task))throw new ArgumentException("duplicate");}
 public WorkTask this[string id]{get=>_tasks[id];set=>_tasks[id]=value.Validate();}
 public IReadOnlyCollection<WorkTask> All=>_tasks.Values;
 public IEnumerable<WorkTask> Filter(Status? status=null,string? tag=null,string? capability=null)=>_tasks.Values.Where(t=>(status is null||t.Status==status)&&(tag is null||t.Tags.Contains(tag))&&(capability is null||t.RequiredCapability==capability));
 public IEnumerable<WorkTask> SortedByPriority()=>_tasks.Values.OrderByDescending(t=>t.Priority).ThenBy(t=>t.Id,StringComparer.Ordinal);
 public IReadOnlyDictionary<Status,int> CountsByStatus()=>_tasks.Values.GroupBy(t=>t.Status).ToDictionary(g=>g.Key,g=>g.Count());
}
