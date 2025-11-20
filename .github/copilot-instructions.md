<!-- .github/copilot-instructions.md -->
# Repository guide for AI coding agents

This file contains concise, actionable guidance for AI coding agents working in this repository. Focus on discoverable patterns and concrete file references so an agent can be productive immediately.


1. Big picture
- **Purpose**: This repo is a course / workshop repository (`ai-dev-zoomcamp`) containing 6 learning modules and homework prompts. Each module has its own folder (e.g., `01-overview/`, `02-snake/`, etc.) and README. The codebase starts with a sample `main.py`, a `pyproject.toml`, and module content under `01-overview/`.
- **Primary artifacts**: `main.py` (simple Python entry), `pyproject.toml` (project metadata, Python >=3.12.3), markdown course content in each module folder (e.g., `01-overview/README_Module_1.md`).

2. How to run and verify small changes
- **Run the sample program**: execute `main.py` directly: `python main.py` (ensure Python >= 3.12.3 to match `pyproject.toml`).
- **No test harness present**: there are no tests in the repo. If you add tests, run them with `pytest` and add instructions to README.

3. Dependency and environment rules
- **Python version**: `pyproject.toml` declares `requires-python = ">=3.12.3"`. Prefer solutions that work under this interpreter.
- **Installing packages**: this workspace commonly uses the `uv` tool to manage project packages. Prefer `uv add <package>` for adding runtime or dev dependencies (for example `uv add django`). If `uv` is not available in the contributor's environment, fall back to `python -m pip install <pkg>`.

	Examples:

	- Add a package with `uv`:

		```bash
		uv add django
		```

	- Fallback using pip:

		```bash
		python -m pip install django
		```

- **When adding deps**: update `pyproject.toml` (add the dependency to `[project].dependencies`) and include a short PR note describing why the dependency is required. Avoid adding heavy infra without maintainer approval.

- **Running commands with uv**: Prefer `uv run <command>` so execution happens inside the project environment (e.g., tests, scripts, Django manage tasks).

	Examples:

	```bash
	# Django (Module 1)
	uv run python3 01-overview/01-todo/manage.py runserver
	uv run python3 01-overview/01-todo/manage.py test

	# Pre-commit hooks
	uv run pre-commit install
	uv run pre-commit run --all-files
	```


4. Project-specific conventions and patterns
- **Course content lives in module folders**: Each module (e.g., `01-overview/`, `02-snake/`, etc.) contains lesson plans, homework prompts, and example commands in markdown files (e.g., `01-overview/README_Module_1.md`). When making content edits, keep examples and shell snippets intact unless you verify them locally. Future modules may use different languages, frameworks, and test setups—refer to each module's README for details.
- **Small, focused changes**: This repo is educational — prefer small edits (one file / one lesson) per change. For code additions, include a short usage example in the top-level `README.md` or the module README.

5. Multi-file edits and PR guidance
- **When adding a new feature or homework solution**: include a short runnable example and update `README.md` pointing to the new folder (e.g., `01-todo/` for a Django homework solution).
- **Safety**: don't invent CI configurations or tests that don't match the maintainer's intent. If you propose adding CI or test automation, summarize the benefit and request confirmation in the PR description.

6. Integration points & external dependencies
- **External links only**: Module markdown references external tools (YouTube, AI vendor links). These are for learning context and don't imply runtime integration.
- **No external services configured**: there are no API keys, Dockerfiles, or cloud deployment manifests in the repo. If changes require external integration, document required secrets and request maintainer approval.

7. Examples an agent should follow
- **Editing content**: update `01-overview/README_Module_1.md` when improving module text. Preserve existing code blocks and command examples.
- **Adding a runnable example**: add a small folder (e.g., `01-todo/`) containing the code, a minimal `README.md` with run steps, and note Python version and any install commands.
- **Quick code fix pattern**: to change `main.py`, produce a single focused patch and then verify by running `python main.py` locally.

8. What NOT to do (practical constraints)
- Do not assume tests exist — add them explicitly if you introduce behavior requiring verification.
- Do not add or publish secrets or keys. If credentials are needed, describe required variables and add instructions to the repo docs instead.
- Avoid changing global project tooling (CI, packaging backends) without explicit agreement from repository maintainers.

9. Typical PR message template an agent can use
```
Title: <short description of change>

Summary:
- What changed and why (2-3 lines)
- Files touched: list

How to test locally:
- Steps to reproduce (commands)

Notes:
- Any follow-up or maintainer decisions required
```

If anything in this file is unclear or you'd like additional examples (e.g., a sample `01-todo/` solution scaffold or a recommended test setup), ask and I will iterate.
