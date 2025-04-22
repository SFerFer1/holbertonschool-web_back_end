#!/usr/bin/env python3
"""
This module provides a simple string operation for concatenation.
"""
import asyncio
from typing import List
import importlib
wait_random = importlib.import_module('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    This module provides a simple string operation for concatenation.
    """
    return asyncio.create_task(wait_random(max_delay))
