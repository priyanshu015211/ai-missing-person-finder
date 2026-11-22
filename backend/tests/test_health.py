from fastapi.testclient import TestClient
from sqlalchemy.exc import OperationalError

from app.api.routes import database as database_routes
from app.main import app

client = TestClient(app)


def test_root_endpoint_returns_service_information() -> None:
    response = client.get("/")

    assert response.status_code == 200
    body = response.json()
    assert body["message"] == "AI Missing Person Finder API is running"
    assert body["version"]
    assert body["docs"] == "/docs"


def test_api_health_endpoint_returns_ok() -> None:
    response = client.get("/api/v1/health")

    assert response.status_code == 200
    assert response.json()["status"] == "ok"
    assert response.json()["service"] == "AI Missing Person Finder API"


def test_database_health_endpoint_returns_connected_when_check_passes(
    monkeypatch,
) -> None:
    monkeypatch.setattr(database_routes, "check_database_connection", lambda: None)

    response = client.get("/api/v1/health/database")

    assert response.status_code == 200
    assert response.json() == {"status": "ok", "database": "connected"}


def test_database_health_endpoint_hides_connection_details_on_failure(
    monkeypatch,
) -> None:
    def fail_connection() -> None:
        raise OperationalError("SELECT 1", {}, Exception("private detail"))

    monkeypatch.setattr(database_routes, "check_database_connection", fail_connection)

    response = client.get("/api/v1/health/database")

    assert response.status_code == 503
    assert response.json() == {"detail": "Database unavailable"}
