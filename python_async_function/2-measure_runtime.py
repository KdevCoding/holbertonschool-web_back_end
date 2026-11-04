#!/usr/bin/env python3
"""Basic async syntax module containing the wait_n coroutine"""
import time
import asyncio

wait_n = __import__("1-concurrent_coroutines").wait_n


def measure_time(n: int, max_delay: int) -> float:
    """runs wait_n n times and tracks time to complete using time module"""
    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    elapsed = time.perf_counter() - start
    return elapsed / n
