#!/usr/bin/python3
"""
Minimum Operations testing file
"""


def minOperations(n):
    """
        Calculates the fewest number of operation needed
        to result exactly n H characters in the file
    """

    if not n or n <= 1:
        return 0
    operations = 0
    for time in range(2, n+1):
        while(n % time == 0):
            operations += time
            n = n / time
    return operations
