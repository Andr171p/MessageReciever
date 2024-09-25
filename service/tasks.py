from service.send import send_message


async def send_status() -> None:
    await send_message.send()
