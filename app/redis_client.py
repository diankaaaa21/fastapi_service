import redis.asyncio as aioredis

from app.config import REDIS_HOST, REDIS_PORT

redis_client = None


async def init_redis():
    global redis_client
    redis_client = aioredis.from_url(
        f"redis://{REDIS_HOST}:{REDIS_PORT}",
        encoding="utf-8",
        decode_responses=True,
    )


async def close_redis():
    global redis_client
    if redis_client:
        await redis_client.close()


async def get_redis_client():
    if redis_client is None:
        raise Exception("Redis is not initialized.")
    return await redis_client
