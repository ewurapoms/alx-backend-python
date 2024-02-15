#!/usr/bin/env python3
""" 
Module that annotate the below function’s parameters 
and return values with the appropriate types
"""


import typing


def element_length(lst: typing.Iterable[typing.Sequence]) -> \
                    typing.List[typing.Tuple[typing.Sequence, int]]:
    """ returns a list of tuples"""
    return [(i, len(i)) for i in lst]
