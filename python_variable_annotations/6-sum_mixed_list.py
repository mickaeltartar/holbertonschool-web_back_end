#!/usr/bin/env python3
""" complex types of mixed list """
from typing import List, Union


def sum_mixed_list(mixed_list: List[Union[int, float]]) -> float:
    """ return sum of mixed list """
    return (sum(mixed_list))
