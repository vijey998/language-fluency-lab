#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

missing=()
if command -v clang-format >/dev/null 2>&1; then
  find assignment solutions -type f \( -name '*.cpp' -o -name '*.hpp' -o -name '*.h' \) -print0 | xargs -0 clang-format -i
else
  missing+=("clang-format")
fi

if command -v dotnet >/dev/null 2>&1; then
  dotnet format assignment/csharp/PolyglotScheduler.sln --no-restore || dotnet format assignment/csharp/PolyglotScheduler.sln
  dotnet format solutions/csharp/PolyglotScheduler.sln --no-restore || dotnet format solutions/csharp/PolyglotScheduler.sln
else
  missing+=("dotnet SDK 8+")
fi

if command -v ruff >/dev/null 2>&1; then
  ruff check --fix assignment/python solutions/python
  ruff format assignment/python solutions/python
else
  missing+=("ruff")
fi

if ((${#missing[@]})); then
  printf '\nSkipped unavailable formatter(s): %s\n' "${missing[*]}"
  printf 'Install them using docs/FORMATTING.md, then rerun this script.\n'
fi
