#!/usr/bin/env python3


import asyncio


''' Import wait_random from 0-basic_async_syntax.

    Write a function task_wait_random that takes an integer
    max_delay and returns a asyncio.Task.
'''


def task_wait_random(max_delay: int) -> asyncio.Task:
    '''A function that creates a task for the scheduler'''

    wait_random = __import__('0-basic_async_syntax').wait_random

    return asyncio.create_task(wait_random(max_delay))
