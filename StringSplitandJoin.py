"""
    >>> split_and_join("this is a string")
    'this-is-a-string'
"""


def split_and_join(line):
    return "-".join(line.split(" "))
