#!/usr/bin/python3
""" Minimum operations
"""


def minOperations(n):

    if n <= 1:
        return 0
    else:
        for i in range(2, n + 1):
            if n % i == 0:
                return minOperations(n // i) + i
