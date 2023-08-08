#!/usr/bin/env python3

''' An asynchronous coroutine that takes in an integer'''


import asyncio



def task_wait_random(max_delay: int) -> asyncio.Task:
    '''A function that creates a task for the scheduler'''

    wait_random = __import__('0-basic_async_syntax').wait_random

    return asyncio.create_task(wait_random(max_delay))
