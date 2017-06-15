"""
    >>> mutate_string("abracadabra", 5, "k")
    'abrackdabra'
    >>> mutate_string("abracadabra", 0, "k")
    'kbracadabra'
"""


def mutate_string(string, position, character):
    return "".join(character if index == position else value for index, value in enumerate(string))
