#!/usr/bin/env python3
""" Returns a tuple with the string k and the square of v """
import typing


def to_kv(k: str, v: typing.Union[int, float]) -> typing.Tuple[str, float]:
    """ function for the tuple """
    return (k, (v ** 2))
