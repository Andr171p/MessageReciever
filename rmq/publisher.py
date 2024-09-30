import aio_pika

from rmq.settings.queue_config import queue_config
from rmq.connection import RMQConnection

from loguru import logger


class RMQPublishMessage(RMQConnection):

    @classmethod
    async def publish(cls, message: str) -> None:
        if cls.channel is None:
            await cls.connect()
        await cls.channel.default_exchange.publish(
            aio_pika.Message(
                body=message.encode()
            ),
            routing_key=queue_config.queue_name
        )
        logger.info(f"[{queue_config.queue_name}] SENT: {message}")
        await cls.close()
