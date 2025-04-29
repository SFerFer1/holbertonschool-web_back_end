#!/usr/bin/env python3
"""
This module provides a simple string operation for concatenation.
"""


def schools_by_topic(mongo_collection, topic):
    return list(mongo_collection.find({"topics": topic}))