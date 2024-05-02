#!/usr/bin/env python3
"""retur a list with a specific topic"""


def schools_by_topic(mongo_collection, topic):
    """return the list of school"""
    result = mongo_collection.find({"topics": topic})
    return result
