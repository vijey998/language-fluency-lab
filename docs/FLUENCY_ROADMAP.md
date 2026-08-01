# Language fluency roadmap

This lab targets rapid, idiomatic implementation—not learning programming from scratch.

## Expected progression

| Outcome | Focused effort for an experienced engineer |
|---|---:|
| Comfortable syntax recall | 2–3 days |
| Standard-library fluency | 5–7 days |
| Reliable interview-speed coding | 2–3 weeks |
| Thinking naturally in each language | 1–2 months of continued use |

Completing the repository once is the first pass. Interview fluency comes from timed reconstruction,
translation, and spaced repetition.

## Seven-day intensive pass

### Day 1 — C++ core

Implement models, catalog, collection operations, equality, hashing, custom sorting, and module wiring.
End with a 20-minute cold rewrite of `Task`, `Worker`, and `TaskCatalog`.

### Day 2 — C++ systems surface

Implement graph traversal, priority queues, ownership, RAII, templates, concurrency, and tests. Repeat
three components without references.

### Day 3 — C# translation

Translate the completed mental model into C#. Focus on projects, references, records, interfaces,
generics, LINQ, `Task`, cancellation, disposal, and dependency composition.

### Day 4 — Python translation

Implement the same architecture idiomatically using packages, dataclasses, typing, protocols,
generators, context managers, `asyncio`, and standard-library collections. Do not write C# with
Python punctuation.

### Day 5 — Persistence and boundaries

Implement JSON, SQLite, CLI, API boundaries, validation, exceptions, logging, and metrics in all three
languages. Practice adding and importing a new module from scratch.

### Day 6 — Translation sprints

Complete the drills in `drills/TRANSLATION_DRILLS.md`. Record lookup count and syntax failures, not
just elapsed time.

### Day 7 — Interview simulation

Perform one 45-minute implementation per language in a blank directory. Include tests, one refactor,
and one follow-up requirement. Review only after the timer ends.

## Weeks 2–3: convert familiarity into speed

Use three 45–60 minute sessions per week:

1. **Cold build:** reconstruct one component without opening the repository.
2. **Translation:** immediately implement it in the other two languages.
3. **Extension:** add a requirement such as cancellation, caching, persistence, or a new strategy.

Rotate through LRU cache, trie, rate limiter, bounded queue, dependency graph, event bus, worker pool,
JSON repository, and a small API endpoint.

## Fluency metrics

Track these in `docs/PRACTICE_LOG.csv`:

- elapsed minutes;
- compiler or test failures;
- documentation lookups;
- autocomplete uses;
- incorrect library/API recalls;
- design rewrites;
- whether the final code is idiomatic;
- whether you can explain ownership, lifetime, cancellation, and complexity.

A fast incorrect implementation is not fluency. The target is clean code with very few repairs.

## Exit criteria

You are interview-ready in a language when you can repeatedly:

- create the project/module structure and imports in under 5 minutes;
- implement value objects with validation, equality, hashing, and serialization in under 10 minutes;
- use core collections, heaps, queues, maps, and sets without lookup;
- implement a graph or scheduler component in under 25 minutes;
- add a strategy/plugin and wire it through the composition root in under 15 minutes;
- write three focused tests in under 10 minutes;
- complete a follow-up refactor without destabilizing the first solution.
