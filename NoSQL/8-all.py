#!/usr/bin/env python3
"""List all document in a collection"""


def list_all(mongo_collection):
    """return list of collection mongo"""
    if mongo_collection is None:
        return []
    return list(mongo_collection.find())