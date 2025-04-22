#!/usr/bin/env python3
"""
This module provides a simple string operation for concatenation.
"""
import asyncio
from typing import List
import importlib
wait_random = importlib.import_module('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    This module provides a simple string operation for concatenation.
    """
    delays = []
    tasks = [wait_random(max_delay) for a in range(n)]

    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return delays
