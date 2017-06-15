"""
    >>> most_common("aabbbccde")
    b 3
    a 2
    c 2
"""


def most_common(string):
    string_dict = {}

    for s in string:
        if s in string_dict:
            string_dict[s] += 1
        else:
            string_dict[s] = 1

    string_dict = sorted(string_dict.items(), key=lambda x: x[1], reverse=True)

    for string in string_dict[:3]:
        print string[0], string[1]
