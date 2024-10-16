#!/usr/bin/python3
"""
Minimum operations
"""


def minOperations(n):
    """
    Minimum operations
    """
    if n <= 1:
        return 0
    for i in range(2, n + 1):
        if n % i == 0:
            return minOperations(n // i) + i
    return 0


if __name__ == "__main__":
    print(minOperations(4))
    print(minOperations(12))
    print(minOperations(9))
