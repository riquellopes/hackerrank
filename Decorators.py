"""
    >>> sort_phone(["07895462130", "919875641230", "9195969878"])
    +91 78954 62130
    +91 91959 69878
    +91 98756 41230
    >>> sort_phone(["09191919191", "9100256236", "+919593621456"])
    +91 91002 56236
    +91 91919 19191
    +91 95936 21456
"""


def wrapper(f):
    tpl = "+91 {} {}"

    def fun(l):
        for index, number in enumerate(l):
            if len(number) == 10:
                prefix, sufix = number[:5], number[5:10]
            elif number[0] == "0":
                prefix, sufix = number[1:6], number[6:11]
            elif number[0] == "9" and len(number) == 12:
                prefix, sufix = number[2:7], number[7:12]
            else:
                prefix, sufix = number[3:8], number[8:13]
            l[index] = tpl.format(prefix, sufix)
        return f(l)
    return fun


@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')
