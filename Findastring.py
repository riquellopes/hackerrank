"""
    >>> count_substring("ABCDCDC", "CDC")
    2
    >>> count_substring("ABCDCDCAAAACDC", "CDC")
    3
    >>> count_substring("ThIsisCoNfUsInG", "is")
    1
"""


def count_substring(string, sub_string):
    occurrences = 0

    for i, __ in enumerate(string):
        cut = string[i:len(sub_string)+i]
        if cut == sub_string:
            occurrences += 1
    return occurrences
