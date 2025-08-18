# Behavioral specification

## Task model
A task has: `id`, `name`, `priority`, `required_capability`, `estimated_ms`, `dependencies`, `tags`, `payload`, `created_at`, and `status`.

Rules:
1. IDs and names are non-empty.
2. Priority is 0–100; larger values run first.
3. Estimated duration is positive.
4. A task cannot depend on itself.
5. Status transitions: Pending -> Ready -> Running -> Succeeded/Failed/Cancelled. Failed may be retried to Ready.

## Catalog
Provides add/get/remove/update/list; rejects duplicate IDs; supports filtering by status/tag/capability; sorting by priority, name, or creation time; grouping by status; and text prefix lookup via a trie.

## Dependency graph
Reject cycles and unknown dependencies. Return a deterministic topological order. A task becomes ready only after all dependencies succeed.

## Scheduling
Use a stable priority queue: greater priority first, then earlier insertion sequence. A scheduling strategy chooses among ready tasks. Include FIFO and highest-priority strategies.

## Workers
Workers advertise capabilities. A worker may execute only compatible tasks. The worker pool uses a bounded blocking queue and supports graceful cancellation/shutdown.

## Cross-cutting components
- Event bus with subscribe/unsubscribe/publish.
- Metrics counters and duration samples.
- Token-bucket rate limiter.
- Generic LRU cache.
- JSON repository.
- Optional SQLite repository.

## CLI
Commands: `demo`, `list`, `add`, `run`, `graph`, `metrics`. The demo must build a small DAG and execute it.

## API boundary
Implement framework-neutral request/response handlers first. Optional adapters may expose HTTP using ASP.NET Minimal APIs, Python FastAPI, or a C++ HTTP library.
