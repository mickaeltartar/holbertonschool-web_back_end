#!/usr/bin/env python3
""" execute multiple coroutines at the same time with async """
from typing import Callable, List
import asyncio

wait_random: Callable = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ return complete in that order """
    tasks: List[asyncio.Task] = [asyncio.create_task
                                (wait_random(max_delay))for _ in range(n)]
    return [await task for task in asyncio.as_completed(tasks)]