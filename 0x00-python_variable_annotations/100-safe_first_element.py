#!/usr/bin/env python3
"""
Module that augments code with the correct duck-typed annotations.
"""
import typing


def safe_first_element(lst: typing.Sequence[typing.Any]) -> \
                        typing.Union[typing.Any, None]:
    """returns function output"""
    if lst:
        return lst[0]
    else:
        return None
