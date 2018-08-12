#!/bin/python3
"""
    >>> plusMinus([-4, 3, -9, 0, 4, 1])
    0.500000
    0.333333
    0.166667
"""

# import math
# import os
# import random
# import re
# import sys


# Complete the plusMinus function below.
def plusMinus(arr):
    positive, negative, zero = 0, 0, 0

    total_items = len(arr)

    for number in arr:
        if number > 0:
            positive += 1
        elif number == 0:
            zero += 1
        else:
            negative += 1

    print('{:.{prec}f}'.format(positive/total_items, prec=6))
    print('{:.{prec}f}'.format(negative/total_items, prec=6))
    print('{:.{prec}f}'.format(zero/total_items, prec=6))


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
