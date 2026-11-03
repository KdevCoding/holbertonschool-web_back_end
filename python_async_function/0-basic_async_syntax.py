#!/usr/bin/env python3
"""func for async"""
from time import sleep
from random import randrange


async def wait_random(max_delay=10):
    """waits a random time and returns said time

    Args:
        max_delay (int, optional): max wait time. Defaults to 10.
    """
    delay = randrange(0, max_delay)
    sleep(delay)
    return delay
