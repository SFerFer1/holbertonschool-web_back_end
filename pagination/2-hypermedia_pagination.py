#!/usr/bin/env python3
"""
This module provides a simple string operation for concatenation.
"""
import csv
from math import ceil
from typing import List, Tuple
import os


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    This module provides a simple string operation for concatenation.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)


class Server:
    """
    This module provides a simple string operation for concatenation.
    """
    DATA_FILE = os.path.join(
        os.path.dirname(__file__),
        "Popular_Baby_Names.csv"
    )

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        This module provides a simple string operation for concatenation.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        This module provides a simple string operation for concatenation.
        """

        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start_index, end_index = index_range(page, page_size)
        dataset = self.dataset()
        return dataset[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """
        This module provides a simple string operation for concatenation.
        """
        data = self.get_page(page, page_size)
        total_items = len(self.dataset())
        all_pages = ceil(total_items / page_size)

        return {
            'page_size': len(data),
            'page': page,
            'data': data,
            'next_page': page + 1 if page < all_pages else None,
            'prev_page': page - 1 if page > 1 else None,
            'total_pages': all_pages
        }
