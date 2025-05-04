from contextlib import asynccontextmanager

from fastapi import FastAPI, HTTPException, Request
from starlette.middleware.base import BaseHTTPMiddleware

from app.config import RATE_LIMIT, TIME_WINDOW
from app.logger import logger
from app.redis_client import close_redis, get_redis_client, init_redis
from app.routers import data, health


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_redis()
    logger.info("Starting application...")
    yield
    await close_redis()
    logger.info("Closing application...")


app = FastAPI(lifespan=lifespan)


@app.get("/ping_redis")
async def ping_redis():
    redis = await get_redis_client()
    pong = await redis.ping()
    return {"redis_ping": pong}


app.include_router(data.router)
app.include_router(health.router)


class RateLimitMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        redis = await get_redis_client()
        client_ip = request.client.host
        key = f"rate_limit:{client_ip}"

        count = await redis.incr(key)
        if count == 1:
            await redis.expire(key, TIME_WINDOW)
        elif count > RATE_LIMIT:
            raise HTTPException(status_code=429, detail="Too Many Requests")

        response = await call_next(request)
        logger.info(f"{request.method} {request.url} -> {response.status_code}")
        return response


app.add_middleware(RateLimitMiddleware)
