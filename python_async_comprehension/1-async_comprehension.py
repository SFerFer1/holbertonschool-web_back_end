#!/usr/bin/env python3
"""
This module provides a simple string operation for concatenation.
"""
from typing import AsyncGenerator
import importlib
async_generator = importlib.import_module('0-async_generator').async_generator


async def async_comprehension() -> AsyncGenerator[int, None]:
    """
    This module provides a simple string operation for concatenation.
    """
    return [number async for number in async_generator()]
