#!/usr/bin/env python3
"""asynchronous coroutine waits for a delay and returns it."""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Wait for a random delay"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
