# Copilot instructions for this repository

Purpose
- Help AI coding agents become productive quickly in this tiny Python repo.

Big picture
- This repository is a single-file CLI Python script: `main.py`.
- The script reads user input via `input()` and intends to square a number. There is no package structure, no requirements, and no tests.

Key files
- `main.py` — entry point and only source of program logic. Currently contains an input parsing bug and invalid Python syntax.

What to look for (patterns & examples)
- Input & parsing: `main.py` uses `input()` and assumes numeric types. Convert and validate user input explicitly. Example replacement:

```python
try:
    x = float(input('Enter a number to square: '))
except ValueError:
    print('Invalid number')
    raise SystemExit(1)
print(x, 'squared equals', x ** 2)
```

- Error handling: prefer explicit exception handling (ValueError) and clear exit codes for CLI behavior.
- No frameworks or external integrations are present — keep changes minimal and self-contained.

Developer workflows (commands)
- Run script (use whichever `python` maps to Python 3 on your system):

```bash
python main.py
```

- Quick debug with the Python debugger:

```bash
python -m pdb main.py
```

Repository-specific conventions
- Keep the repo single-file focused: changes should aim to preserve simple CLI behavior unless adding a new module or tests is explicitly requested.
- When modifying `main.py`, include a small docstring at file top describing CLI behavior and expected input/output.

Integration points & dependencies
- There are no external dependencies or integration endpoints in this repo. Treat any addition of new dependencies as a deliberate change and mention it in the PR description.

When creating PRs or commits
- Keep diffs small and focused (fix one bug or add one small feature per commit).
- If adding tests, include `pytest` in a minimal `requirements.txt` and a `tests/` folder; otherwise note that CI is not configured.

If you need clarification
- The repo contains only `main.py`. If you intend larger refactors (packaging, tests, CI), ask the repo owner before broad changes.

Next step
- Ask for feedback on any unclear or incomplete sections so I can iterate this guidance.
