# Formatting and VS Code setup

V2 is configured so formatting is repository policy, not personal taste.

## Fastest VS Code setup

1. Open the **repository root** in VS Code, not an individual language folder.
2. Accept **Install Recommended Extensions** when VS Code prompts you.
3. Install the command-line tools below.
4. Run **Terminal → Run Task → Format: entire repository** once.
5. Thereafter, saving a file formats it automatically.

The workspace already includes:

- `.vscode/settings.json` — format-on-save and language-specific defaults;
- `.vscode/extensions.json` — recommended extensions;
- `.vscode/tasks.json` — formatting, checking, and testing commands;
- `.clang-format` — Google-derived C++20 style;
- `.editorconfig` — shared whitespace and C# conventions;
- Ruff configuration in both Python `pyproject.toml` files.

## Install formatter command-line tools

### Windows with Winget

```powershell
winget install LLVM.LLVM
winget install Microsoft.DotNet.SDK.8
py -m pip install ruff
```

Close and reopen VS Code after installing LLVM so `clang-format` is on `PATH`.

### macOS with Homebrew

```bash
brew install llvm dotnet@8 ruff
```

If Homebrew does not link LLVM, add its `bin` directory to `PATH`.

### Ubuntu / Debian

```bash
sudo apt update
sudo apt install clang-format dotnet-sdk-8.0
python3 -m pip install --user ruff
```

## Format everything from a terminal

```bash
bash scripts/format_all.sh
```

Equivalent native commands:

```bash
# C++
find assignment solutions -type f \( -name '*.cpp' -o -name '*.hpp' \) -print0 \
  | xargs -0 clang-format -i

# C#
dotnet format assignment/csharp/PolyglotScheduler.sln
dotnet format solutions/csharp/PolyglotScheduler.sln

# Python
ruff check --fix assignment/python solutions/python
ruff format assignment/python solutions/python
```

## Check without modifying files

```bash
bash scripts/check_format.sh
```

## Useful VS Code commands

- **Format Document:** `Shift+Alt+F` on Windows/Linux, `Shift+Option+F` on macOS.
- **Format Selection:** use the Command Palette.
- **Organize Imports:** run from the Command Palette when not triggered on save.
- **Run Task:** `Ctrl+Shift+P` → `Tasks: Run Task`.

## When a file still looks wrong

1. Check the language mode in the lower-right corner of VS Code.
2. Run **Format Document With…** and select the configured formatter.
3. Choose **Configure Default Formatter** if VS Code asks.
4. Confirm the repository root is open so workspace settings are active.
5. Confirm the relevant executable is on `PATH`.

C++ and C# formatters can expand the intentionally compact starter examples. Ruff handles
Python formatting and import ordering. Markdown is word-wrapped but not aggressively rewritten,
so instructional lists remain readable.
