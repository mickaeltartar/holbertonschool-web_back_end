#!/usr/bin/env python3
"""an asynchronous coroutine that takes in an integer argument"""

import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """return delay"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return (delay)
