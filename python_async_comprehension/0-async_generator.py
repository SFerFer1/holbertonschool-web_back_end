#!/usr/bin/env python3
"""
This module provides a simple string operation for concatenation.
"""
import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    This module provides a simple string operation for concatenation.
    """
    for a in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
