#!/usr/bin/env python3
"""Function to measure total execution time."""
import time
import asyncio
from importlib import import_module

module = import_module('1-concurrent_coroutines')
wait_n = module.wait_random


def measure_time(n: int, max_delay: int) -> float:
    """Measure total execution time."""
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    
    total_time = end_time - start_time
    return total_time / n
