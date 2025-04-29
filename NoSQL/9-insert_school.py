#!/usr/bin/env python3
"""
This module provides a simple string operation for concatenation.
"""


def insert_school(mongo_collection, **kwargs):
    """
    This module provides a simple string operation for concatenation.
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
