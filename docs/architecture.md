# Architecture — Phase 1

## System boundaries

```text
Browser
  React + JavaScript + Vite (localhost:5173)
          |
          | HTTP / JSON, /api/v1
          v
  FastAPI application (localhost:8000)
          |
          +---- SQLAlchemy session layer
          |          |
          |          v
          |       MySQL 8
          |
          +---- AI recognition service (later phase)
          |
          +---- Private image storage (later phase)
```

## Current repository and migration boundary

The existing Flask MVP (`app.py`, `templates/`, root `requirements.txt`) remains at the repository root as a reference implementation during Phase 1. The new API and web client live in `backend/` and `frontend/`. Do not remove or relocate the Flask files until their required workflows have been migrated and tested in a later phase.

## Backend responsibilities

- `app/main.py`: FastAPI application and CORS policy.
- `app/core/config.py`: environment-backed application configuration.
- `app/api/`: versioned HTTP routes.
- `app/db/session.py`: SQLAlchemy engine, session factory and DB connectivity probe.
- `app/schemas/`: response contracts.
- `app/models/`: reserved for SQLAlchemy models in a later milestone.
- `app/services/`: reserved for business logic and AI orchestration.

## Data and privacy principles

- MySQL is the system of record for structured application data.
- Images and biometric templates must not be made public or committed to Git.
- Access to sensitive records will be role-restricted and audited.
- AI output is a candidate lead, not an identity determination.
- A trained/authorized human reviewer must review potential matches before any family-facing confirmation.
- Retention, deletion, consent, and incident-response controls must be designed before real-person data is accepted.

## Current scope

Phase 1 implements only service foundations, CORS, an API health endpoint, a separate MySQL connectivity endpoint, a React connection-status screen, and automated backend tests. It does not yet implement login, case records, image ingestion, face recognition, or production deployment.
