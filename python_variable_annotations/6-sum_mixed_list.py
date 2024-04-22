#!/usr/bin/env python3
"""complex types of list of floats"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """return mied list in float"""
    return (sum(mxd_lst))