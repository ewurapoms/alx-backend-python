#!/usr/bin/env python3
"""Module performs basic async function"""

import asyncio
import random


async def wait_random(max_delay=10):
    """displays the async function"""
    lapse = random.uniform(0, max_delay)
    await asyncio.sleep(lapse)
    return lapse
