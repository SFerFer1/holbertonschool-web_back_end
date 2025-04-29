#!/usr/bin/env python3
"""
This module provides a simple string operation for concatenation.
"""

def update_topics(mongo_collection, name, topics):
    mongo_collection.update_many(
        { "name": name },
        { "$set": { "topics": topics } }
    )
