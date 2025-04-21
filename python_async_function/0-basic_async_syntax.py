#!/usr/bin/env python3

"""
This module provides a simple string operation for concatenation.
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    This module provides a simple string operation for concatenation.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
