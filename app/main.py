from fastapi import FastAPI, Request

from app.logger import logger
from app.redis_client import close_redis, get_redis_client, init_redis
from app.routers import data, health

app = FastAPI()


@app.on_event("startup")
async def startup_event():
    await init_redis()
    logger.info("Starting application...")


@app.on_event("shutdown")
async def shutdown_event():
    await close_redis()
    logger.info("Closing application...")


@app.get("/ping_redis")
async def ping_redis():
    redis = get_redis_client()
    pong = await redis.ping()
    return {"redis_ping": pong}


app.include_router(data.router)
app.include_router(health.router)


@app.middleware("http")
async def log_requests(request: Request, call_next):
    response = await call_next(request)
    logger.info(f"{request.method} {request.url} -> {response.status_code}")
    return response
