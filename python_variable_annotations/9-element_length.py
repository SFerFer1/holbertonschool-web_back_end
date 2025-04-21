#!/usr/bin/env python3

"""
This module provides a simple string operation for concatenation.
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    This module provides a simple string operation for concatenation.
    """
    return [(i, len(i)) for i in lst]
