# Translation drills

The algorithm stays fixed; only language expression changes. Finish one implementation, close it,
and immediately reproduce it in the other two languages.

## Rules

1. Use no solution code during the first attempt.
2. Autocomplete may complete identifiers but must not generate blocks.
3. Wait three minutes before consulting syntax documentation.
4. Record every lookup in `docs/PRACTICE_LOG.csv`.
5. Compare idioms—not line-by-line similarity—after all three versions pass.

## Drill set

### 1. Collection transform — 12 minutes per language

Given tasks, group by owner, remove terminal tasks, sort each group by descending priority and then
ID, and return the top two tasks per owner.

Practice: vectors/lists, maps/dictionaries, grouping, lambdas, custom comparison, ranges/LINQ,
comprehensions, and stable ordering.

### 2. LRU cache — 20 minutes per language

Implement generic `get`, `put`, overwrite, recency update, and eviction behavior with O(1) average
operations.

Practice: templates/generics/type variables, hash maps, linked lists, iterators/references, equality,
and tests.

### 3. Dependency graph — 25 minutes per language

Add dependencies, reject unknown nodes and cycles, produce topological order, and identify nodes ready
to run from a supplied completed set.

Practice: sets, maps, queues/stacks, traversal, exceptions, and module boundaries.

### 4. Bounded worker queue — 30 minutes per language

Implement blocking producer/consumer behavior, clean shutdown, cancellation, and a capacity invariant.

Practice: mutexes/locks, condition variables/semaphores, threads/tasks, RAII/disposal/context managers,
and race-resistant testing.

### 5. JSON repository — 20 minutes per language

Persist and reload task objects while maintaining enum, timestamp, and optional-field compatibility.

Practice: files, serialization, errors, resource cleanup, package imports, and dependency inversion.

### 6. Strategy plugin — 15 minutes per language

Add a retry strategy and inject it into the engine without modifying task handlers.

Practice: abstract base classes/interfaces/protocols, composition, factories, constructors, and tests.

### 7. API follow-up — 20 minutes per language

Create one endpoint or callable boundary to submit a task, validate it, return an error model, and
retrieve it by ID. A network server is optional; the boundary and wiring are mandatory.

Practice: DTOs, validation, asynchronous calls, imports/references, and error translation.

## Final three-language sprint

In a blank directory, create a package/library containing:

- a task model;
- an in-memory repository;
- priority scheduling;
- dependency validation;
- one strategy interface;
- three tests;
- a CLI entry point.

Budget: 45 minutes per language. The target is not feature volume; it is low-friction, correctly wired,
idiomatic code.
