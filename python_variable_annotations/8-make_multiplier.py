#!/usr/bin/env python3

"""
This module provides a simple string operation for concatenation.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    This module provides a simple string operation for concatenation.
    """
    def multiplier_function(value: float) -> float:
        """
        This module provides a simple string operation for concatenation.
        """
        return value * multiplier
    return multiplier_function
