#!/usr/bin/env python3

'''A module for summation of two float numbers'''


def add(a: float, b: float) -> float:
    '''returns the summation of two float numbers'''
    return a + b


if __name__ == '__main__':

    print(add(1.11, 2.22) == 1.11 + 2.22)
    print(add.__annotations__)
