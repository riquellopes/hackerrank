"""
    >>> Arithmetic(3, 2)()
    5
    1
    6
    >>> Arithmetic(5, 2)()
    7
    3
    10
    >>> Arithmetic(9, 3)()
    12
    6
    27
"""


class Arithmetic:

    def __init__(self, first, second):
        self._first = first
        self._second = second

    def __call__(self):
        self._calculate()

    def _sum(self):
        print(self._first + self._second)

    def _difference(self):
        print(self._first - self._second)

    def _product(self):
        print(self._first * self._second)

    def _calculate(self):
        self._sum()
        self._difference()
        self._product()
