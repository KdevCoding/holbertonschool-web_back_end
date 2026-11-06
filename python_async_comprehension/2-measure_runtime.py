#!/usr/bin/env python3
"""measure runtime of 4 async_comprehension
"""
import time
import asyncio

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """measures runtime of multiple instance of async func

    Returns:
        float: runtime
    """
    start = time.perf_counter()
    await asyncio.gather(async_comprehension(), async_comprehension(),
                         async_comprehension(), async_comprehension())
    elapsed = time.perf_counter() - start
    return elapsed
