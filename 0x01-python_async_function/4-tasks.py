#!/usr/bin/env python3
""" Module imports task 3 to perform more tasks """
import asyncio
import random

task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n, max_delay):
    """ displays function"""
    delays = []

    tasks = [task_wait_random(max_delay) for _ in range(n)]
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return delays
