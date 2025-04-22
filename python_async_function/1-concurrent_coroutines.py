#!/usr/bin/env python3

"""
This module provides a simple string operation for concatenation.
"""
import importlib.util

spec = importlib.util.spec_from_file_location("wait_random_module", "./0-basic_async_syntax.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

import asyncio

async def wait_n(n: int, max_delay: int):
    tasks = [module.wait_random(max_delay) for _ in range(n)]

    delays = []

    async for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return delays 