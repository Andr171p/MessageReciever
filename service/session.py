import asyncio

from contextlib import suppress


class Periodic:
    is_started = False
    _task = None

    def __init__(self, func, timeout: int) -> None:
        self.timeout = timeout
        self.func = func

    async def start(self) -> None:
        if not self.is_started:
            self.is_started = True
            # self._task = asyncio.ensure_future(self._run())
            await self.func()

    async def stop(self) -> None:
        if self.is_started:
            self.is_started = False
            self._task.cancel()
            with suppress(asyncio.CancelledError):
                await self._task

    async def _run(self) -> None:
        while True:
            await asyncio.sleep(self.timeout)
            await self.func()
