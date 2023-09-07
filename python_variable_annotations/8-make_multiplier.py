#!/usr/bin/env python3
"""Return another function that multiplies a float by a number."""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Return a function that multiplies a float by a number."""
    def multipler_func(n: float) -> float:
        return n * multiplier
    return multipler_func
