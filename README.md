# ai-dev-tools-zoomcamp

![CI](https://github.com/RuiFSP/ai-dev-zoomcamp/actions/workflows/ci.yml/badge.svg)

Course that helps use AI tools to write better code.

Quick start (preferred `uv` workflow)

- Python: this project targets Python >= 3.12.3 (see `pyproject.toml`).
- Install a dependency (preferred):

```bash
uv add django
```

- Run the app (from project or app folder):

```bash
uv run python3 01-overview/01-todo/manage.py runserver
```

- Run tests:

```bash
uv run python3 01-overview/01-todo/manage.py test
```

Notes:
- `uv` creates and manages a per-project virtualenv and a lockfile. Commit `pyproject.toml` and `uv.lock` after adding dependencies.
- If `uv` is unavailable, you can fall back to `python -m pip install <pkg>` and run `python3` directly, but `uv` is preferred for reproducibility.
