using System.Collections.Immutable;
namespace Scheduler.Core;
public enum Status { Pending, Ready, Running, Succeeded, Failed, Cancelled }
public sealed record WorkTask(string Id,string Name,int Priority=50,string RequiredCapability="cpu",int EstimatedMs=1,ImmutableHashSet<string>? Dependencies=null,ImmutableHashSet<string>? Tags=null,Status Status=Status.Pending)
{
 public ImmutableHashSet<string> Dependencies { get; init; }=Dependencies??[]; public ImmutableHashSet<string> Tags { get; init; }=Tags??[];
 public WorkTask Validate(){if(string.IsNullOrWhiteSpace(Id)||string.IsNullOrWhiteSpace(Name))throw new ArgumentException("id/name");if(Priority is <0 or >100)throw new ArgumentOutOfRangeException(nameof(Priority));if(EstimatedMs<=0)throw new ArgumentOutOfRangeException(nameof(EstimatedMs));if(Dependencies.Contains(Id))throw new ArgumentException("self dependency");return this;}
 public WorkTask Transition(Status target){var ok=(Status,target) switch{(Status.Pending,Status.Ready or Status.Cancelled)=>true,(Status.Ready,Status.Running or Status.Cancelled)=>true,(Status.Running,Status.Succeeded or Status.Failed or Status.Cancelled)=>true,(Status.Failed,Status.Ready or Status.Cancelled)=>true,_=>false};return ok?this with{Status=target}:throw new InvalidOperationException($"{Status}->{target}");}
}
public sealed record Worker(string Id,ImmutableHashSet<string> Capabilities){public bool CanRun(WorkTask task)=>Capabilities.Contains(task.RequiredCapability);}
