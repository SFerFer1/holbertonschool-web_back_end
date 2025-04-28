#!/usr/bin/env python3
"""
This module provides a simple string operation for concatenation.
"""


def index_range(page, page_size):
    """
    This module provides a simple string operation for concatenation.
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)
