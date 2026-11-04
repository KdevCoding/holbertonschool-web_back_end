#!/usr/bin/env python3
"""Basic async syntax module containing the wait_n coroutine"""
import asyncio
from typing import List

wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """runs wait_random n times and returns list of delays"""
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    delays: List[float] = []
    for task in asyncio.as_completed(tasks):
        delays.append(await task)
    return delays
