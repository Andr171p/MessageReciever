import aio_pika

from rmq.settings.server_config import ConnectData
from rmq.settings.queue_config import QueueConfig
from rmq.settings.logs import RMQLogs

from loguru import logger

from typing import Any


'''class RMQConnection:
    connection = pika.BlockingConnection(
        pika.URLParameters(ConnectData.RMQ_URL)
    )
    channel = connection.channel()

    @classmethod
    def create_queue(cls) -> None:
        cls.channel.queue_declare(QueueConfig.queue_name)

    @classmethod
    def close(cls) -> None:
        cls.connection.close()'''


class RMQConnection:
    connection = None
    channel = None

    @classmethod
    async def connect(cls) -> None:
        cls.connection = await aio_pika.connect_robust(ConnectData.RMQ_URL)
        cls.channel = await cls.connection.channel()
        logger.info(RMQLogs.SUCCESSFUL_CONNECT_LOG)

    @classmethod
    async def create_queue(cls) -> Any:
        if cls.channel is None:
            await cls.connect()
        queue = await cls.channel.declare_queue(QueueConfig.queue_name)
        return queue

    @classmethod
    async def close(cls) -> None:
        await cls.connection.close()
        logger.info(RMQLogs.CLOSE_LOG)
