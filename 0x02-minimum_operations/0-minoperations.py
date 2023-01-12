#!/usr/bin/python3
'''
Given a number n, write a method that calculates
the fewest number of operations needed to result in
exactly n H characters in the file.
'''


def minOperations(n):
    """minOperations is a method that calculates
    the fewest number of operations needed to result
    in exactly n H characters
    Args:
        n (int): amount of H
    Return:
        minimum number of operations (an integer)
    """
    minOp, div = 0, 2
    while isinstance(n, int) and n > 1:
        while n % div:
            div += 1
        minOp += div
        n = int(n / div)
    return minOp
