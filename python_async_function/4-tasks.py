#!/usr/bin/env python3
"""Function that runs task_wait_random multiple times"""
import asyncio
from typing import List
from importlib import import_module

module = import_module('3-tasks')
task_wait_random = module.task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Run task_wait_random n times with the specified max_delay."""
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)
