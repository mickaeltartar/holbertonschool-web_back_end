#!/usr/bin/env python3
""" complex types functions """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ return a function that multiplies """
    return (lambda x: x * multiplier)
