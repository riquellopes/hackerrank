#!/bin/python3
"""
    >>> stringConstruction("abcd")
    4
    >>> stringConstruction("abab")
    2
"""
import os


# Complete the stringConstruction function below.
def stringConstruction(s):
    return len(list(set(s)))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = stringConstruction(s)

        fptr.write(str(result) + '\n')

    fptr.close()
