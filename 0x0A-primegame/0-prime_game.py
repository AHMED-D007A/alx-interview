#!/usr/bin/python3
"""Prime Game"""


def is_prime(n):
    """Check if a number is prime"""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def isWinner(x, nums):
    """Prime Game"""
    if x < 1 or nums is None:
        return None
    Maria = Ben = 0
    for n in nums:
        if is_prime(n):
            Maria += 1
        else:
            Ben += 1
    if Maria == Ben:
        return None
    return "Maria" if Maria < Ben else "Ben"


if __name__ == "__main__":
    print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))
