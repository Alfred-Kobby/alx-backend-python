#!/usr/bin/env python3

''' An asynchronous coroutine that takes in an integer'''


from typing import List


async def wait_n(n: int, max_delay: int) -> List[float]:
    ''' returns a sorted list of float numbers gotten randomly'''
    wait_random = __import__('0-basic_async_syntax').wait_random

    delay_list = []
    i = 0

    while i < n:
        delay_list.append(await wait_random(max_delay))
        i += 1

    return sorted(delay_list)
