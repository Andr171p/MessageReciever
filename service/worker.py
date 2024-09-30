from service.session import Periodic
from service.tasks import send_status
from service.settings.config import service_config

from loguru import logger


async def start() -> None:
    periodic = Periodic(
        func=send_status,
        timeout=service_config.TIMEOUT
    )
    try:
        logger.info("SERVICE WAS STARTED...")
        await periodic.start()
    except Exception as _ex:
        logger.info("SERVICE ERROR")
        logger.warning(_ex)
        await periodic.stop()
        logger.info("SERVICE WAS STOPPED")
    finally:
        await periodic.stop()
        logger.info("SERVICE WAS STOPPED")
