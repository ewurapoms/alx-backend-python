#!/usr/bin/env python3
""" Module that chooses async comprehension over aysnc generator """

from typing import List

async_generator = __import__("0-async_generator").async_generator


async def async_comprehension() -> List[float]:
    """function content """
    return [number async for number in async_generator()]
