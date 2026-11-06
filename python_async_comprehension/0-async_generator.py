#!/usr/bin/env python3
"""A coroutine will loop 10 times,
then yield a random number between 0 and 10
"""

import asyncio
import random


async def async_generator() -> float:
    """loops 10 time asynchronously waiting 1 second each time
    Yields: random float from 0 and 10
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
