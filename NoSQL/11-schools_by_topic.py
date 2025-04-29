#!/usr/bin/env python3
"""
This module provides a simple string operation for concatenation.
"""


def schools_by_topic(mongo_collection, topic):
    """
    This module provides a simple string operation for concatenation.
    """
    return list(mongo_collection.find({"topics": topic}))