#!/usr/bin/env python3
"""Module for async_generator."""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Generate random numbers 0 to 10 every second for 10 seconds."""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
