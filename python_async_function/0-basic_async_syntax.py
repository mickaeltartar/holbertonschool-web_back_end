#!/usr/bin/env python3
""" Create a générator """
import asyncio
from random import uniform


async def wait_random(max_delay: int = 10) -> float:
    """ return delay """
    delay: float = uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
