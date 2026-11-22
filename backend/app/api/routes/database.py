import logging

from fastapi import APIRouter, HTTPException, status
from sqlalchemy.exc import SQLAlchemyError

from app.db.session import check_database_connection
from app.schemas.health import DatabaseHealthResponse

logger = logging.getLogger(__name__)
router = APIRouter(tags=["Health"])


@router.get(
    "/health/database",
    response_model=DatabaseHealthResponse,
    responses={503: {"description": "Database is unavailable"}},
)
def database_health() -> DatabaseHealthResponse:
    """Check MySQL separately and do not expose credentials or driver errors."""
    try:
        check_database_connection()
    except SQLAlchemyError as exc:
        logger.exception("MySQL health check failed")
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Database unavailable",
        ) from exc

    return DatabaseHealthResponse(status="ok", database="connected")
