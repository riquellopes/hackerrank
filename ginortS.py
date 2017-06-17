"""
    >>> Gisorts("Sorting1234")()
    'ginortS1324'
"""
import string


class Gisorts:

    def __init__(self, s):
        self._s = s
        self._numerical, self._alpha_low, self._alpha_up = [], [], []

        self._split_string()
        self._sort_alphabet_lower()
        self._sort_alphabet_upper()
        self._sort_numerical()

    def __call__(self):
        return "".join(
            self._alpha_low+self._alpha_up+self._numerical)

    def _split_string(self):
        for character in self._s:
            if character.isdigit():
                self._numerical.append(character)
            elif character.islower():
                self._alpha_low.append(character)
            else:
                self._alpha_up.append(character)

    def _sort_numerical(self):
        odd, even = [], []
        for number in self._numerical:
            to_int = int(number)
            if to_int % 2 == 0 and to_int != 0:
                even.append(number)
            else:
                odd.append(number)
        self._numerical = odd+even

    def _sort_alphabet_lower(self):
        alpha_low = []
        for char in string.ascii_lowercase:
            for alpha in self._alpha_low:
                if char == alpha:
                    alpha_low.append(char)
        self._alpha_low = alpha_low

    def _sort_alphabet_upper(self):
        alpha_up = []
        for char in string.ascii_uppercase:
            for alpha in self._alpha_up:
                if char == alpha:
                    alpha_up.append(char)
        self._alpha_up = alpha_up


if __name__ == "__main__":
    s = Gisorts(input())()
    print(s)
