#!/usr/bin/env python3
""" Module returns a float as the sum of integers and floats"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ """
    return float(sum(mxd_lst))
