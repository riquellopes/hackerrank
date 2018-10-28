#!/bin/python3
"""
    >>> miniMaxSum([1, 2, 3, 4, 5])
    10 14
    >>> miniMaxSum([7, 69, 2, 221, 8974])
    299 9271
    >>> miniMaxSum([5, 5, 5, 5, 5])
    20 20
"""


# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    numbers = {}

    for x in range(0, 5):
        if x not in numbers:
            numbers[x] = 0

        sums = arr[:]
        sums.remove(sums[x])

        for y in sums:
            numbers[x] += y

    numbers = sorted(numbers.items(), key=lambda x: x[1])
    print("{} {}".format(numbers[0][1], numbers[-1][1]))


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
