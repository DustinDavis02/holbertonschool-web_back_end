#!/usr/bin/env python3
"""function for async_comprehension"""
import asyncio
from typing import List
from importlib import import_module

module = import_module('0-async_generator')
async_generator = module.async_generator


async def async_comprehension() -> List[float]:
    """async_comprehension"""
    return [i async for i in async_generator()]
