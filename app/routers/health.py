from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

from app.crud import check_redis_connection
from app.logger import logger

router = APIRouter()


@router.get("/health", status_code=200)
async def health_check():
    """
    Health check for Redis connection.
    """
    is_alive = await check_redis_connection()
    if not is_alive:
        logger.error("Health check failed: Redis is unhealthy.")
        return JSONResponse(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            content={"status": "unhealthy"},
        )

    return {"status": "ok"}
