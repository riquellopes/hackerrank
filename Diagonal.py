"""
    >>> diagonal(3, [[11, 2, 4],[4, 5, 6],[10, 8, -12]])
    15
"""


def diagonal(n, matrix):
    start, end = 0, 1
    x, y = [], []

    for row in range(n):
        for col in range(start, end):
            x.append(matrix[row][col])
        start += 1
        end += 1

    start, end = 0, 1

    for row in range(n):
        line = list(reversed(matrix[row]))

        for col in range(start, end):
            y.append(line[col])
        start += 1
        end += 1

    return abs(sum(x) - sum(y))
