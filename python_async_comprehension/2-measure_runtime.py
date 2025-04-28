#!/usr/bin/env python3
"""
This module provides a simple string operation for concatenation.
"""
import time
import asyncio
a = __import__('1-async_comprehension').async_comprehension

async def measure_runtime() -> float:
    """
    This module provides a simple string operation for concatenation.
    """
    start = time.time()

    tasks = [a() for a in range(4)]
    await asyncio.gather(*tasks)

    end = time.time()

    return end - start
