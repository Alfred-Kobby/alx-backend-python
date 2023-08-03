#!/usr/bin/env python3


'''Takes a float as argument and returns a string'''


def to_str(n: float) -> str:
    '''Returns the string quivalent of any float argument'''
    return str(n)


if __name__ == '__main__':
    print(f'to_str(3.14)')
    print(to_str(0.00))

    print(to_str.__annotations__)
