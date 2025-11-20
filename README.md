
# ai-dev-tools-zoomcamp

![CI](https://github.com/RuiFSP/ai-dev-zoomcamp/actions/workflows/ci.yml/badge.svg)

**AI Dev Zoomcamp** — Learn modern AI-powered coding workflows, tools, and automation through hands-on modules and homeworks.

## Course Structure

This course is organized into 6 modules, each focused on a different aspect of AI-assisted development. Each module includes practical examples and a homework project:

### Module 1 — Introduction to Vibe Coding / AI Tools Overview
- AI-assisted development with Snake game example (React + JS)
- Chat applications: ChatGPT, Claude, DeepSeek, Microsoft Copilot
- Coding assistants / IDEs: Claude Code, GitHub Copilot, Cursor, Pear
- Project bootstrappers: Bolt, Lovable
- Agents: Anthropic Computer Use, PR Agent, others

### Module 2 — End-to-End Project (Snake)
- Use a coding assistant for an end-to-end project
- Build Snake in React/TS
- Define API with OpenAPI
- Generate FastAPI server from OpenAPI specs
- Add CI/CD
- Deploy the application

### Module 3 — Model-Context Protocol
- Enhancing AI assistants with tools
- Core servers: GitHub, Filesystem, DB/SQL, HTTP/API, CI
- Practical workflows: repo triage, PR summarization, scripted edits, data queries
- Local vs. remote servers
- Security/permissions

### Module 4 — Build an AI Coding Agent (for Django)
- Build your own coding agent that can scaffold and extend projects
- Use a Django template as the base project
- Learn how agents act as project bootstrappers
- Explore multiple agent orchestration frameworks
- Outcome: a Django app created and modified by your AI agent

### Module 5 — AI for Testing, CI/CD & DevOps
- AI-assisted PR reviews/summaries and change-risk hints
- Automated test generation, coverage gates, and LLM evals in CI
- Release notes, changelog drafting, and deployment runbooks
- Incident postmortems and on-call copilots

### Module 6 — Automation with Low-Code and No-Code AI (n8n)
- When to automate vs. code; composable AI tasks
- Build an n8n workflow using LLM nodes and webhooks
- Connectors: email, Slack, GitHub/Jira/Notion, databases
- Ship lightweight assistants without maintaining servers


Each module will have its own folder and homework/app example.

### Module 1 resources
- [Module 1 folder: 01-overview/](01-overview/)
- [Module 1 README & homework details](01-overview/README_Module_1.md)

---

## Quick start for Module 1 (Django TODO app)

The instructions below are for running the Module 1 homework (Django TODO app). Other modules will have their own setup and run instructions in their respective folders and READMEs.

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
