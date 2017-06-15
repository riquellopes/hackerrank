"""
    >>> loops(5)
    0
    1
    4
    9
    16
"""


def loops(n):
    for n in range(0, n):
        if n >= 0:
            print(n ** 2)
