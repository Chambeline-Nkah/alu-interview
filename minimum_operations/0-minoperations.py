#!/usr/bin/python3
"""
Minimum Operations testing file
"""


def minOperations(n):
    """
        Calculates the fewest number of operation needed
        to result exactly n H characters in the file
    """

    if n <= 1:
        return 0
    
    character = 1
    copy = character
    min_ops = 0
    while character < n:

        if n % character == 0:

            copy = character
            character = 2 * copy
            min_ops += 2
        else:

            character += copy
            min_ops += 1
    return min_ops
