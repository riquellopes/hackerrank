"""
    >>> name_format([["Mike", "Thomson", "20", "M"], ])
    ['Mr. Mike Thomson']
    >>> name_format([["Mike", "Thomson", "20", "M"], ["Robert", "Bustle", "32", "M"], ["Andria", "Bustle", "30", "F"]])
    ['Mr. Mike Thomson', 'Ms. Andria Bustle', 'Mr. Robert Bustle']
"""
import operator


def person_lister(f):
    def inner(people):
        persons = [[index, int(person[2]), f(person)] for index, person in enumerate(people)]
        persons.sort(key=operator.itemgetter(1))

        return [person[2] for person in persons]
    return inner


@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]
