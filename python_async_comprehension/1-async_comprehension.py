#!/usr/bin/env python3
"""async comprehensing for task 1
"""

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> list:
    """collects 10 random numbers from async_generator
    """
    result = []
    async for i in async_generator():
        result.append(i)
    return result
