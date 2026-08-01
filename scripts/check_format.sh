#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"
command -v clang-format >/dev/null && find assignment solutions -type f \( -name '*.cpp' -o -name '*.hpp' \) -print0 | xargs -0 clang-format --dry-run --Werror
command -v dotnet >/dev/null && dotnet format solutions/csharp/PolyglotScheduler.sln --verify-no-changes --no-restore
command -v ruff >/dev/null && ruff format --check assignment/python solutions/python && ruff check assignment/python solutions/python
