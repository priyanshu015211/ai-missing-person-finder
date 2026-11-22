# Phase 1 — Foundation and setup

This guide assumes Windows PowerShell and the repository root as the current directory.

## Prerequisites

- Python 3.11 or 3.12 recommended
- Node.js 22.12+ (or a supported newer LTS release) and npm
- MySQL 8.x service running locally
- Git

The old Flask MVP remains in the repository root. The new implementation is developed separately under `backend/` and `frontend/` during migration.

## 1. Backend environment

```powershell
cd backend
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
Copy-Item .env.example .env
```

Edit `backend/.env` and set the password for the dedicated MySQL user created below. Do not commit `.env`.

Create the database and application account in MySQL as an administrator:

```sql
CREATE DATABASE missing_person_finder
  CHARACTER SET utf8mb4
  COLLATE utf8mb4_unicode_ci;

CREATE USER 'mpf_app'@'localhost' IDENTIFIED BY 'REPLACE_WITH_A_STRONG_PASSWORD';
GRANT ALL PRIVILEGES ON missing_person_finder.* TO 'mpf_app'@'localhost';
```

Use the same password in `DATABASE_URL` in `backend/.env`. URL-encode reserved characters in the password if used in the connection URL. Do not use the MySQL root account from the application.

Start FastAPI from the `backend/` directory:

```powershell
uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

Check these endpoints:

- `http://127.0.0.1:8000/`
- `http://127.0.0.1:8000/api/v1/health`
- `http://127.0.0.1:8000/api/v1/health/database`
- `http://127.0.0.1:8000/docs`

The API health endpoint can be healthy while MySQL is unavailable. The database endpoint separately returns HTTP 503 when the database check fails. This separation makes service diagnosis clearer.

Run backend tests from `backend/`:

```powershell
python -m pytest
```

## 2. Frontend environment

Open a second PowerShell terminal at the repository root:

```powershell
cd frontend
npm install
Copy-Item .env.example .env.local
npm run dev
```

Open `http://localhost:5173`. The screen calls the API health endpoint and displays whether the backend is reachable.

Create a production build check with:

```powershell
npm run build
```

## 3. Common issues

- **PowerShell blocks activation:** run `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass` in that terminal, then activate again.
- **MySQL connection refused:** verify the Windows MySQL service is running and listening on port 3306.
- **Access denied:** verify the `mpf_app` password, host (`localhost`), database name, and grants.
- **CORS error:** ensure the frontend uses `http://localhost:5173` or `http://127.0.0.1:5173`, both of which are configured by default.
- **Backend imports fail:** ensure the virtual environment is active, dependencies are installed, and the server was started from the `backend/` directory.

## 4. Scope guard

Do not upload real missing-person photographs or biometric data during Phase 1. The endpoints in this phase are infrastructure checks only. Real data workflows require authentication, authorization, consent, audit logging, secure storage, retention/deletion controls, and human review, which are planned for later phases.
