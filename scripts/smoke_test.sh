#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cmake -S "$ROOT/solutions/cpp" -B "$ROOT/build/cpp"
cmake --build "$ROOT/build/cpp" -j
ctest --test-dir "$ROOT/build/cpp" --output-on-failure
PYTHONPATH="$ROOT/solutions/python/src" python3 -m pytest "$ROOT/solutions/python/tests"
if command -v dotnet >/dev/null; then dotnet run --project "$ROOT/solutions/csharp/Scheduler.Tests"; else echo "dotnet not installed; skipped C# runtime check"; fi
