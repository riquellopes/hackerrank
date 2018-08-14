#!/bin/python3

"""
    >>> twoStrings("hello", "world")
    'YES'
    >>> twoStrings("hi", "world")
    'NO'
"""

import os


# Complete the twoStrings function below.
def twoStrings(s1, s2):
    word = list(s1)

    for w in word:
        if w in s2:
            return "YES"
    return "NO"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)

        fptr.write(result + '\n')

    fptr.close()
