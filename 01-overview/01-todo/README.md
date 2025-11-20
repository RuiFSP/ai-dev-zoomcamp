# 01-todo (Homework)

Minimal Django TODO app used for the course homework.

Run instructions

1. Install dependencies (preferred: `uv`):

```bash
uv add django
```

2. Create a superuser (optional, to access admin):

```bash
uv run python3 manage.py createsuperuser
```

3. Run the development server:

```bash
uv run python3 manage.py runserver
```

Visit `http://127.0.0.1:8000/` for the TODO UI and `http://127.0.0.1:8000/admin/` for admin.

Run tests:

```bash
uv run python3 manage.py test
```

Notes
- Templates are located in `templates/` at the project root and the app is `todos`.
- If `uv` is not available, use `python3 -m pip install django` and `python3 manage.py ...`.
