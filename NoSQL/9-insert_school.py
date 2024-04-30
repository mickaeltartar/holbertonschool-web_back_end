#!/usr/bin/env python3
"""Insert a document in a collection with kwarg"""


def insert_school(mongo_collection, **kwargs):
    """Insert the document into the collection"""
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id