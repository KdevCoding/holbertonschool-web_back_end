#!/usr/bin/env python3
"""func for async"""
from random import uniform
from asyncio import sleep


async def wait_random(max_delay=10):
    """waits a random time and returns said time

    Args:
        max_delay (int, optional): max wait time. Defaults to 10.
    """
    delay = uniform(0, max_delay)
    await sleep(delay)
    return delay
