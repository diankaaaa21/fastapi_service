from app.logger import logger
from app.redis_client import get_redis_client


async def write_data(phone: str, address: str):
    try:
        redis = await get_redis_client()
        exists = await redis.exists(phone)
        await redis.set(phone, address)

        if exists:
            logger.info(f"Phone {phone} updated in Redis.")
            return "updated"
        else:
            logger.info(f"Phone {phone} created in Redis.")
            return "created"
    except Exception:
        logger.error(f"Error writing data", exc_info=True)
        raise


async def get_address(phone: str):
    try:
        redis = await get_redis_client()
        address = await redis.get(phone)
        return address
    except Exception:
        logger.error(f"Error getting data for phone", exc_info=True)
        raise


async def check_redis_connection():
    redis = await get_redis_client()
    try:
        pong = await redis.ping()
        return pong
    except Exception:
        logger.error(f"Redis cannot connect", exc_info=True)
        return False
