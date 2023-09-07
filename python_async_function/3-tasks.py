#!/usr/bin/env python3
"""function that creats an asyncio.Task."""
import asyncio
from importlib import import_module

module = import_module('0-basic_async_syntax')
wait_random = module.wait_random

def task_wait_random(max_delay: int) -> asyncio.Task:
    """function that creats an asyncio.Task."""
    return asyncio.create_task(wait_random(max_delay))
