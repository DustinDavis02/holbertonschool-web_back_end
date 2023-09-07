#!/usr/bin/env python3
"""Asynchronous coroutine that runs wait_random multiple times"""
import asyncio
from typing import List
from importlib import import_module

module = import_module('0-basic_async_syntax')
wait_random = module.wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Wait for n seconds, then return a list of delays"""
    tasks = [wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)
