"""
    >>> print_function(3)
    123
    >>> print_function(5)
    12345
"""


def print_function(number):
    print "".join([str(n) for n in range(1, number+1)])


if __name__ == '__main__':
    n = int(input())
    print_function(n)
