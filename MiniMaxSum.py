#!/bin/python3
"""
    >>> miniMaxSum([1, 2, 3, 4, 5])
    10 14
    >>> miniMaxSum([7, 69, 2, 221, 8974])
    299 9271
"""


# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    numbers = {}

    for x in arr:
        if x not in numbers:
            numbers[x] = 0

        for y in arr:
            if x == y:
                continue
            numbers[x] += y

    numbers = sorted(numbers.items(), key=lambda x: x[1])
    print("{} {}".format(numbers[0][1], numbers[-1][1]))


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
