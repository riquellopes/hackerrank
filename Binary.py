"""
    >>> solution(955)
    4
    >>> solution(1)
    1
    >>> solution(10)
    2
    >>> solution(100)
    7
    >>> solution(1000)
    10
    >>> solution(10000)
    14
    >>> solution(100000)
    17
    >>> solution(1000000)
    20
    >>> solution(10000000)
    24
    >>> solution(100000000)
    27
    >>> solution(1000000000)
    30
"""


# 1110111011
# 1 a[0+1] = 1
# 1 a[1+1] = 1
# 1 a[2+1] = 0

# 1 a[0+2] = 1
# 1 a[1+2] = 0

# 1 a[0+3] = 0

# 1 a[0+4] = 1
# 1 a[1+4] = 1


def solution(n):
    array = [0] * 30
    qa = 0

    while (n > 0):
        array[qa] = n % 2
        n //= 2
        qa += 1

    for p in range(1, 1 + qa):
        ok = True

        for i in range(qa - p):
            # array[0] != array[0+1]
            # array[1] != array[1+1]
            # array[2] != array[2+1]
            # array[3] != array[3+1]

            if array[i] != array[i + p]:
                ok = False
                break
        if ok:
            return p
    return -1
