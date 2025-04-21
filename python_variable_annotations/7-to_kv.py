#!/usr/bin/env python3

"""
This module provides a simple string operation for concatenation.
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    This module provides a simple string operation for concatenation.
    """
    return (k, float(v ** 2))
