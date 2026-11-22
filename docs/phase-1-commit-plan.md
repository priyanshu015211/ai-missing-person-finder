# Phase 1 — Suggested commit sequence

Make these nine focused commits on `feat/phase-1-foundation`. Each commit groups a meaningful part of the implementation; do not create empty commits just to increase the count.

Run commands from the repository root. Review each staged change with `git diff --cached` before committing.

## 1. Repository hygiene and environment templates

```powershell
git add .gitignore backend/.env.example frontend/.env.example
git diff --cached
git commit -m "chore: add repository ignores and environment templates"
```

## 2. Add the complete FastAPI and MySQL backend foundation

```powershell
git add backend/requirements.txt backend/app
git diff --cached
git commit -m "feat(backend): add FastAPI and MySQL foundation"
```

## 3. Add backend automated tests

```powershell
git add backend/tests backend/pyproject.toml
git diff --cached
git commit -m "test(backend): cover API and database health checks"
```

## 4. Add React JavaScript frontend and API status integration

```powershell
git add frontend/package.json frontend/package-lock.json frontend/index.html frontend/vite.config.js frontend/src
git diff --cached
git commit -m "feat(frontend): scaffold React app and API status check"
```

## 5. Document the application architecture

```powershell
git add docs/architecture.md
git diff --cached
git commit -m "docs: define Phase 1 application architecture"
```

## 6. Document local setup and troubleshooting

```powershell
git add docs/phase-1-setup.md
git diff --cached
git commit -m "docs: add local development setup guide"
```

## 7. Add the Phase 1 commit guide

```powershell
git add docs/phase-1-commit-plan.md
git diff --cached
git commit -m "docs: add structured Phase 1 commit plan"
```

## 8. Add backend CI

```powershell
git add .github/workflows/backend-ci.yml
git diff --cached
git commit -m "ci: run backend checks on pull requests"
```

## 9. Record actual verification results

After running the backend tests and frontend production build on your machine, create `docs/phase-1-completion.md`. Record the actual Python, Node, npm and MySQL versions, the exact test/build commands, their results, and any environment-specific caveat. Do not state that a check passed unless you ran it. Then:

```powershell
git add docs/phase-1-completion.md
git diff --cached
git commit -m "docs: record Phase 1 verification results"
```

After all nine commits:

```powershell
git status
git log -9 --oneline
```

The root Flask `app.py`, `templates/`, and root `requirements.txt` intentionally remain unchanged until their workflows are migrated and tested in a later phase.
