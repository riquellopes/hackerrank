#!/bin/python3
"""
    >>> staircase(6)
         #
        ##
       ###
      ####
     #####
    ######
"""


# Complete the staircase function below.
def staircase(n):
    total = n

    for line in range(1, total+1):
        spaces = (total - line)

        print("".join([" " if colum < spaces else "#" for colum in range(0, n)]))


if __name__ == '__main__':
    n = int(input())

    staircase(n)
