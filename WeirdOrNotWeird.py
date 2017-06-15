"""
    >>> WeirdOrNotWeird(3)()
    'Weird'
    >>> WeirdOrNotWeird(2)()
    'Not Weird'
    >>> WeirdOrNotWeird(24)()
    'Not Weird'
    >>> WeirdOrNotWeird(18)()
    'Weird'
    >>> WeirdOrNotWeird(22)()
    'Not Weird'
    >>> WeirdOrNotWeird(100)()
    'Not Weird'
"""


class WeirdOrNotWeird:

    def __init__(self, number):
        self.number = number

    def __call__(self):
        return self._process()

    def _even_number(self):
        return self.number % 2 == 0

    def _range(self, start, end):
        return self.number in range(start, end+1)

    def _process(self):
        message = "Not Weird"
        if not self._even_number():
            message = "Weird"
        elif self._even_number() and self._range(2, 5):
            message = "Not Weird"
        elif self._even_number() and self._range(6, 20):
            message = "Weird"
        return message


if __name__ == '__main__':
    n = int(input())
