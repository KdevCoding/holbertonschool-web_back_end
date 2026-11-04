#!/usr/bin/env python3
"""Basic async syntax module containing the wait_n coroutine."""
import asyncio

wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int):
    """runs wait_random n times and returns list of delays"""
    tasks = [wait_random(max_delay) for _ in range(n)]
    delays = []
    for task in asyncio.as_completed(tasks):
        delays.append(await task)
    return delays
