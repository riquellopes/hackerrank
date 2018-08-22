# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

"""
    >>> solution(123456)
    162534
    >>> solution(162534)
    146325
"""


def solution(A):
    # write your code in Python 3.6

    numbers = list(str(A))
    size = len(numbers)
    to_remove = 0

    digit = []

    while True:

        if len(digit) == size:
            break

        if to_remove == 0:
            num = numbers.pop(to_remove)

            to_remove = -1
        else:
            num = numbers.pop()
            to_remove = 0
        digit.append(num)
    return int("".join(digit))
