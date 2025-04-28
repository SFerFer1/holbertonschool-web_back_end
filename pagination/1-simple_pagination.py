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

def get_page(page=1, page_size=10):
    assert isinstance(page, int) and page > 0
    assert isinstance(page_size, int) and page_size > 0

    return index_range(page, page_size)