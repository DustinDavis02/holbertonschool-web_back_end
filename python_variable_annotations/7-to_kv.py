#!/usr/bin/env python3
"""Function that returns a tuple of a string and the square of a number"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Function that returns a tuple of a string and the square of a number"""
    return (k, float(v ** 2))
