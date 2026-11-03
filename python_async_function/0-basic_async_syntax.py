#!/usr/bin/env python3
"""Basic async syntax module containing the wait_random coroutine."""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """waits a random time and returns said time"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
