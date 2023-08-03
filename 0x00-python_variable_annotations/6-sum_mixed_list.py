#!/usr/bin/env python3


'''Takes a list mxd_lst of integers
   and floats and returns their sum as a float.
'''


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    '''Returns float sum of mxd_lst'''

    total = 0.00
    for i in mxd_lst:
        total += i
    return total


if __name__ == '__main__':
    print(sum_mixed_list.__annotations__)
    mixed = [5, 4, 3.14, 666, 0.99]
    ans = sum_mixed_list(mixed)
    print(ans == sum(mixed))
    print("sum_mixed_list(mixed) returns {} which is a {}"
          .format(ans, type(ans)))