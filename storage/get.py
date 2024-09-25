from storage.connection import RedisConnection
from storage.settings.cluster import ClusterConfig
from storage.struct import RedisMessageStruct
from storage.utils import is_new

from typing import List, Any


class RedisGetData:
    EXPIRE_TIMEOUT = ClusterConfig.EXPIRE_TIMEOUT

    def __init__(
            self, redis: RedisConnection.redis
    ) -> None:
        self.redis = redis

    async def keys(self) -> Any:
        keys = await self.redis.keys('*')
        return keys

    async def zipped_data(self, keys: Any) -> zip:
        values = [await self.redis.hget(key, "value") for key in keys]
        numbers = [await self.redis.hget(key, "telefon") for key in keys]
        pay_links = [await self.redis.hget(key, "pay_link") for key in keys]
        projects = [await self.redis.hget(key, "project") for key in keys]
        return zip(values, numbers, pay_links, projects)

    async def get_data(self) -> List[dict]:
        keys = await self.keys()
        zipped_data = await self.zipped_data(keys=keys)
        data = [
            RedisMessageStruct(key, value, number, pay_link, project).data()
            for key, value, number, pay_link, project in zipped_data
            if await is_new(
                redis=self.redis,
                key=key,
                timeout=self.EXPIRE_TIMEOUT
            )
        ]
        return data
