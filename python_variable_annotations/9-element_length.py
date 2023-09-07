#!/usr/bin/env python3
"""function that returns a list of tuples with its length and sequence"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Returns a list of tuples containing its length and sequence."""
    return [(i, len(i)) for i in lst]
