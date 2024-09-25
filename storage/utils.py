import json

from storage.connection import RedisConnection


async def is_new(
        redis: RedisConnection.redis, key: str, timeout: int
) -> bool:
    now_time = await redis.time()
    pushed_time = await redis.hget(key, "timestamp")
    pool_time = int(now_time[0])
    set_time = int(pushed_time)
    creation_time = pool_time - set_time
    return True if creation_time <= timeout else False


def dict_to_json(_dict: dict) -> str:
    _json = json.dumps(_dict, ensure_ascii=False)
    return _json

