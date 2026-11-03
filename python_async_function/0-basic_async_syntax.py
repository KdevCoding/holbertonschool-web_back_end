#!/usr/bin/env python3
"""coroutine for async task"""
import asyncio
import random


async def wait_random(max_delay=10) -> float:
    """waits a random time and returns said time

    Args:
        max_delay (int, optional): max wait time. Defaults to 10.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
