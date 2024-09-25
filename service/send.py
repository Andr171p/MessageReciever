from rmq.publisher import RMQPublishMessage

from storage.connection import RedisConnection
from storage.get import RedisGetData
from storage.utils import dict_to_json

from service.settings.logs import logs_info

from loguru import logger


class SendMessage:
    connection = RedisConnection()
    redis = None
    rmq = RMQPublishMessage()

    @classmethod
    async def connect(cls) -> RedisGetData:
        redis = await cls.connection.connect()
        cls.redis = RedisGetData(redis=redis)
        return cls.redis

    @classmethod
    async def send(cls) -> None:
        cls.redis = await cls.connect()
        data = await cls.redis.get_data()
        logger.info(data)
        logger.info(logs_info.GET_MESSAGE)
        for message in data:
            logger.info(message)
            body = dict_to_json(_dict=message)
            cls.rmq.publish(message=body)
            logger.info(logs_info.SEND_TO_RMQ)


send_message = SendMessage()
