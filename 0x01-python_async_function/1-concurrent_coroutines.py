#!/usr/bin/env python3
"""
Module executes multiple coroutines
at the same time with async
"""
import asyncio
import random

wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n, max_delay):
    '''displays the function'''
    delays = []

    tasks = [wait_random(max_delay) for _ in range(n)]
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return delays
