# Completion checklist

## Every language
- [ ] Package/module/library builds from a clean checkout
- [ ] Imports/includes/project references are understood, not cargo-culted
- [ ] Models validate and support equality/hashing appropriately
- [ ] list/vector, map/dictionary, set/hash set, deque/queue, stack, heap/priority queue used
- [ ] sorting with built-in and custom ordering
- [ ] graph traversal and cycle detection
- [ ] generic/template collection implemented
- [ ] iterator/generator/lazy query implemented
- [ ] errors/exceptions handled deliberately
- [ ] JSON and file paths round-trip
- [ ] thread/task/async path supports cancellation and shutdown
- [ ] unit tests cover happy path, boundary, and failure
- [ ] CLI and API composition roots wire dependencies

## C++
- [ ] header/source split, namespaces, CMake targets, linking
- [ ] const correctness, references, optional/variant, ranges
- [ ] unique_ptr/shared_ptr decision explained
- [ ] RAII, move semantics, jthread/stop_token

## C#
- [ ] solution/projects, namespace/usings, NuGet/project references
- [ ] records, interfaces, generics, LINQ/yield
- [ ] Task/async/await, cancellation, IDisposable/IAsyncDisposable
- [ ] dependency injection and configuration

## Python
- [ ] pyproject package, editable install, absolute/relative imports
- [ ] dataclass, Enum, Protocol/ABC, typing/generics
- [ ] generators/decorators/context managers
- [ ] asyncio versus threads understood
