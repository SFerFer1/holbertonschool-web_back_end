#!/usr/bin/env python3

"""
This module provides a simple string operation for concatenation.
"""
from typing import Iterable, Tuple, List


def element_length(lst: Iterable[str]) -> List[Tuple[str, int]]:
    """
    This module provides a simple string operation for concatenation.
    """
    return [(i, len(i)) for i in lst]
