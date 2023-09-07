#!/usr/bin/env python3
"""This module contains an asynchronous coroutine that waits for a random delay and returns it."""
import asyncio
import random

async def wait_random(max_delay: int = 10) -> int:
    """Wait for a random delay"""
    delay = random.randint(0, max_delay)
    await asyncio.sleep(delay)
    return delay
