# Polyglot Scheduler Lab v2

A compact, interview-focused language-fluency curriculum implemented in **C++20, C#/.NET 8, and Python 3.12**.

The domain is a local distributed-task scheduler: tasks form a dependency graph, wait in priority queues, run on workers, emit events and metrics, persist to JSON/SQLite, and are exposed through a CLI and lightweight API boundary. A few deliberately extra components—LRU cache, trie, rate limiter, bounded queue, event bus—exist because interview fluency matters more than architectural purity.


## What v2 adds

- Repository-wide VS Code format-on-save for C++, C#, Python, JSON, and shared whitespace rules.
- Recommended extension installation through `.vscode/extensions.json`.
- One-command formatting and format verification through `scripts/format_all.sh` and `scripts/check_format.sh`.
- A realistic 2–3 day, 5–7 day, 2–3 week, and 1–2 month fluency progression.
- Seven-day intensive curriculum plus weeks 2–3 spaced-repetition plan.
- Cross-language translation drills and a practice metrics log.
- Timed cold-build simulations designed to convert syntax familiarity into interview speed.

Open the repository **root** in VS Code and accept the recommended extensions. Then read
`docs/FORMATTING.md` and run **Terminal → Run Task → Format: entire repository**.

## Repository layout

- `assignment/`: mixed starter code. Some files are complete examples, some contain focused TODOs, and some contain only a design contract.
- `solutions/`: complete reference implementations.
- `shared-spec/`: behavioral contracts and API/data model.
- `drills/`: timed interview-speed modifications.
- `scripts/`: smoke tests plus repository-wide formatting checks.
- `docs/FLUENCY_ROADMAP.md`: intensive week, weeks 2–3, metrics, and exit criteria.
- `docs/FORMATTING.md`: exact VS Code and command-line formatter setup.
- `docs/PRACTICE_LOG.csv`: timing and syntax-recall tracking.
- `drills/TRANSLATION_DRILLS.md`: repeat the same implementation across all three languages.

## Make every file look clean

The workspace is already configured for format-on-save. Install the recommended VS Code extensions
and the formatter executables, then run:

```bash
bash scripts/format_all.sh
```

Windows, macOS, Linux, troubleshooting, and native commands are documented in
[`docs/FORMATTING.md`](docs/FORMATTING.md). VS Code tasks are included for formatting, checking, and
testing the repository.

## Required tools

### C++
- CMake 3.20+
- A C++20 compiler (GCC 11+, Clang 14+, or MSVC 2022)

```bash
cmake -S solutions/cpp -B build/cpp
cmake --build build/cpp -j
ctest --test-dir build/cpp --output-on-failure
./build/cpp/scheduler_cli demo
```

For the assignment, replace `solutions/cpp` with `assignment/cpp`. Some later checkpoint tests are expected to fail until you implement the TODOs.

### C#
- .NET SDK 8+

```bash
dotnet build solutions/csharp/PolyglotScheduler.sln
dotnet test solutions/csharp/PolyglotScheduler.sln
dotnet run --project solutions/csharp/Scheduler.Cli -- demo
```

### Python
- Python 3.11+ (3.12 recommended)

```bash
cd solutions/python
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\\Scripts\\activate
python -m pip install -e '.[dev]'
pytest
python -m scheduler.cli demo
```

## How to use the lab

1. Read `shared-spec/REQUIREMENTS.md` and the checkpoint README for one language.
2. Work only in `assignment/<language>`.
3. Run tests after every small change.
4. Use the completed files as local examples before looking at the solution.
5. Compare against `solutions/` only after a checkpoint passes or after 30 minutes blocked.
6. Reimplement the same checkpoint in the other two languages without copying line-by-line.

## Learning timeline

For an experienced engineer, expect roughly:

| Milestone | Focused effort |
|---|---:|
| Comfortable syntax recall | 2–3 days |
| Standard-library fluency | 5–7 days |
| Reliable interview-speed coding | 2–3 weeks |
| Natural language-specific thinking | 1–2 months of continued use |

The full seven-day plan, weeks 2–3 repetition schedule, measurement system, and exit criteria are in
[`docs/FLUENCY_ROADMAP.md`](docs/FLUENCY_ROADMAP.md). Translation sprints are in
[`drills/TRANSLATION_DRILLS.md`](drills/TRANSLATION_DRILLS.md).

## Fluency benchmarks

You are ready when, without references, you can in each language:

- create a package/library and wire imports/references in under 5 minutes;
- model a value object with equality, hashing, validation, and serialization in under 10 minutes;
- use map/set/list/deque/heap/stack and custom sorting without syntax lookup;
- implement dependency traversal and a worker queue in under 25 minutes;
- add a new strategy implementation and inject it through the composition root in under 15 minutes;
- write three focused unit tests in under 10 minutes;
- explain ownership/lifetime in C++, disposal/cancellation in C#, and sync-vs-async behavior in Python.

## SQL extension

`shared-spec/schema.sql` contains an optional SQLite schema and query set. Each solution includes a repository boundary; the SQL exercise asks you to implement equivalent persistence in all three languages.

## Scope note

This is not production Kubernetes wearing a fake moustache. It is intentionally small enough to rebuild repeatedly while still covering the language surface area that causes interview hesitation.

## Practice methodology

The [AI-assisted practice methodology](docs/AI_WORKFLOW.md) defines how independent attempts, AI hints, tests, and practice metrics fit together.

## License

This project is available under the [MIT License](LICENSE).
