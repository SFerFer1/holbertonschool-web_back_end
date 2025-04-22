#!/usr/bin/env python3
"""
This module provides a simple string operation for concatenation.
"""
import asyncio
from typing import List
import importlib
wait_random = importlib.import_module('0-basic_async_syntax').wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    This module provides a simple string operation for concatenation.
    """
    delays = []
    tasks = [wait_random(max_delay) for a in range(n)]

    delays = await asyncio.gather(*tasks)
    return sorted(delays)
