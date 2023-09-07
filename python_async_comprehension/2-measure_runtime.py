#!/usr/bin/env python3
"""Function for measuring runtime."""
import asyncio
import time
from typing import List
from importlib import import_module

module = import_module('1-async_comprehension')
async_comprehension = module.aasync_comprehension


async def measure_runtime() -> float:
    """Measure runtime"""
    start_time = time.time()
    tasks = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*tasks)
    end_time = time.time()
    return end_time - start_time
