from redis import asyncio as aioredis
from redis import Redis

from storage.settings.network import ConnectData


class RedisConnection:
    REDIS_URL = ConnectData.REDIS_URL
    redis = None

    @classmethod
    async def connect(cls) -> Redis:
        cls.redis = await aioredis.from_url(cls.REDIS_URL)
        return cls.redis

    @classmethod
    async def close(cls) -> None:
        cls.redis.close()
        await cls.redis.wait_closed()
