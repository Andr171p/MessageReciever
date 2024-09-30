import asyncio

from contextlib import suppress


class Periodic:
    is_started = False
    _task = None

    def __init__(self, func: callable, timeout: int) -> None:
        self._timeout = timeout
        self._func = func

    async def start(self) -> None:
        if not self.is_started:
            self.is_started = True
            await self._run()

    async def stop(self) -> None:
        if self.is_started:
            self.is_started = False
            # self._task.cancel()
            # with suppress(asyncio.CancelledError):
            # await self._task

    async def _run(self) -> None:
        while True:
            await asyncio.sleep(self._timeout)
            await self._func()
