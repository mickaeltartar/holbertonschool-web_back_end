#!/usr/bin/env python3
""" let's duck type an iterable object """
from typing import List, Iterable, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ return list of tuples of item & item length """
    return [(index, len(index)) for index in lst]
