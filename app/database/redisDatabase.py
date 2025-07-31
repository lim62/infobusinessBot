from redis.asyncio import Redis
from aiogram.fsm.storage.redis import RedisStorage
from app.config import Config

def get_storage(config: Config) -> RedisStorage:
    return RedisStorage(
        redis=Redis(
            host=config.redis.HOST,
            port=config.redis.PORT
        )
    )