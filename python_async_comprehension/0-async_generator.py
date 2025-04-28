#!/usr/bin/env python3
"""
This module provides a simple string operation for concatenation.
"""
import random
import asyncio
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[int, None]:
    """
    This module provides a simple string operation for concatenation.
    """
    for a in range(10):
        await asyncio.sleep(1)
        yield random.randint(0, 10)
