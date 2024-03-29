#!/usr/bin/env python3
"""Module makes a multiplier """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ multiplier function """
    return lambda x: x * multiplier
