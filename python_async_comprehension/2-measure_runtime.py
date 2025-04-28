#!/usr/bin/env python3
"""
This module provides a simple string operation for concatenation.
"""
import time
import importlib
import asyncio
a = importlib.import_module('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    This module provides a simple string operation for concatenation.
    """
    start = time.time()

    tasks = [a() for a in range(4)]
    await asyncio.gather(*tasks)

    end = time.time()

    return end - start
