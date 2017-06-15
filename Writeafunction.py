"""
    >>> is_leap(2000)
    True
    >>> is_leap(2400)
    True
    >>> is_leap(1800)
    False
    >>> is_leap(1900)
    False
    >>> is_leap(2100)
    False
    >>> is_leap(2200)
    False
    >>> is_leap(2300)
    False
    >>> is_leap(2500)
    False
"""


def is_leap(year):
    leap = False

    # The year can be evenly divided by 4, unless;
    divisible_by_4 = year % 4 == 0

    # The year can be evenly divided by 100, it is NOT a leap year, unless;
    divisible_by_100 = year % 100 != 0

    # The year is also evenly divisible by 400. Then it is a leap year.
    if divisible_by_4 and divisible_by_100 or (year % 400 == 0):
        leap = True
    return leap
