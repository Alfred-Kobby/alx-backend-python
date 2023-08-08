#!/usr/bin/env python3

''' An asynchronous coroutine that takes in an integer'''


import asyncio
from random import uniform


async def wait_random(max_delay: int = 10) -> float:
    '''Generates a random number and returns it after n delay'''
    delay = uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
