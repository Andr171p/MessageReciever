from rmq.settings.queue_config import queue_config
from rmq.connection import RMQConnection

import logging


logging.basicConfig(level=logging.INFO)


class RMQPublishMessage(RMQConnection):

    def publish(self, message: str) -> None:
        self.channel.basic_publish(
            exchange='',
            routing_key=queue_config.queue_name,
            body=message
        )
        logging.info(f"[{queue_config.queue_name}] SENT: {message}")
