#!/usr/bin/env python3
"""Basic async syntax module containing the wait_n coroutine"""
import asyncio

wait_random = __import__("0-basic_async_syntax").wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """runs wait_n n times and tracks time to complete using time module"""
    task = asyncio.create_task(wait_random(max_delay))
    return task
