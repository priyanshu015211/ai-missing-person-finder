from fastapi import APIRouter

from app.core.config import settings
from app.schemas.health import ApiHealthResponse

router = APIRouter(tags=["Health"])


@router.get("/health", response_model=ApiHealthResponse)
def api_health() -> ApiHealthResponse:
    """Report that the API process is responding, independent of MySQL."""
    return ApiHealthResponse(
        status="ok",
        service=settings.app_name,
        version=settings.app_version,
    )
