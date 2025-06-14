#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """
        This module provides a simple string operation for concatenation.
        """
        self.__dataset = None
        self.__indexed_dataset = None

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

    def indexed_dataset(self) -> Dict[int, List]:
        """
        This module provides a simple string operation for concatenation.
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        This module provides a simple string operation for concatenation.
        """
        dataset = self.indexed_dataset()
        total_items = len(dataset)

        assert 0 <= index < total_items, f"Index {index} is out of range"

        page_data = []
        current_index = index

        while len(page_data) < page_size:
            if dataset.get(current_index) is not None:
                page_data.append(dataset[current_index])
            current_index += 1

        next_index = current_index

        return {
            'index': index,
            'next_index': next_index,
            'page_size': len(page_data),
            'data': page_data
        }
