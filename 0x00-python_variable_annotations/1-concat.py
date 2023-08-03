#!/usr/bin/env python3


''' Concatenates two strings'''


def concat(str1: str, str2: str) -> str:
    '''Concatenates 2 strings'''
    return str1 + str2


if __name__ == '__main__':

    str1 = 'Hello'
    str2 = 'World'

    print(concat(str1, str2) == "{}{}".format(str1, str2))
    print(concat.__annotations__)
