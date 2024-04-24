#!/usr/bin/env python3
""" measure_runtime should measure the total runtime and return it.
measure_runtime coroutine that will execute
async_comprehension four times
in parallel using asyncio.gather """

import asyncio

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ coroutine that will execute async_comprehension four times
    in parallel using asyncio.gather
    return total runtime in float
    """
    task = [async_comprehension() for _ in range(4)]
    start_time = asyncio.get_event_loop().time()
    await asyncio.gather(*task)
    end_time = asyncio.get_event_loop().time()
    total_runtime = end_time - start_time
    return total_runtime
