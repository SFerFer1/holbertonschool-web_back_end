#!/usr/bin/env python3
"""
This module provides a simple string operation for concatenation.
"""
import asyncio
import time
from typing import List
import importlib
wait_n = importlib.import_module('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    This module provides a simple string operation for concatenation.
    """
    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end = time.perf_counter()
    total = end - start
    return total / n
