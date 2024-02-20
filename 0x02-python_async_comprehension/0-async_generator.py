#!/usr/bin/env python3
"""Module that generates random numbers 10x """

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """ function content """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
