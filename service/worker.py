from service.session import Periodic
from service.tasks import send_status
from service.settings.config import service_config


import logging


logging.basicConfig(level=logging.INFO)


async def start() -> None:
    periodic = Periodic(
        func=await send_status(),
        timeout=service_config.TIMEOUT
    )
    try:
        logging.info("SERVICE WAS STARTED...")
        await periodic.start()
    except Exception as _ex:
        logging.info("SERVICE ERROR")
        logging.warning(_ex)
        await periodic.stop()
        logging.info("SERVICE WAS STOPPED")
    finally:
        await periodic.stop()
        logging.info("SERVICE WAS STOPPED")
