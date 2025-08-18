PRAGMA foreign_keys = ON;
CREATE TABLE IF NOT EXISTS tasks (
  id TEXT PRIMARY KEY,
  name TEXT NOT NULL,
  priority INTEGER NOT NULL CHECK(priority BETWEEN 0 AND 100),
  required_capability TEXT NOT NULL,
  estimated_ms INTEGER NOT NULL CHECK(estimated_ms > 0),
  payload_json TEXT NOT NULL,
  created_at TEXT NOT NULL,
  status TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS task_dependencies (
  task_id TEXT NOT NULL REFERENCES tasks(id) ON DELETE CASCADE,
  dependency_id TEXT NOT NULL REFERENCES tasks(id) ON DELETE CASCADE,
  PRIMARY KEY(task_id, dependency_id),
  CHECK(task_id <> dependency_id)
);
-- Exercises:
-- 1. Return ready tasks whose dependencies all succeeded, ordered by priority.
-- 2. Return task counts grouped by status.
-- 3. Return the critical path by accumulated estimated_ms (recursive CTE).
-- 4. Atomically claim one ready task for a worker capability.
