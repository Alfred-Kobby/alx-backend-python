#!/usr/bin/env python3


from typing import List


''' An asynchronous coroutine that takes in an integer'''


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''Runs an async function for n times and adds the results into a list'''
    modified_random = __import__('3-tasks').task_wait_random

    delay_list = []
    i = 0

    while i < n:
        delay_list.append(await modified_random(max_delay))
        i += 1

    return sorted(delay_list)
