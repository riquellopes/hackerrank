# coding: utf-8
"""
    >>> solution([1, 3, 6, 4, 1, 2])
    5
    >>> solution([1, 2, 3])
    4
    >>> solution([−1, −3])
    1
"""
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(A):
    # write your code in Python 3.6
    items = list(set(A))

    for index, value in enumerate(items):
        if value >= 0:
            try:
                next_position = index + 1
                if items[next_position] == value + 1:
                    continue
                else:
                    return value + 1
            except:
                return value + 1
    return 1
