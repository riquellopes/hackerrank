"""
    >>> capitalize("hello word")
    'Hello Word'
    >>> capitalize("12abc")
    '12abc'
    >>> capitalize("1 2 3 4 5 6 8")
    '1 2 3 4 5 6 8'
    >>> capitalize('132 456 Wq  m e')
    '132 456 Wq  M E'
    >>> capitalize('q w e r t y u i o p a s d f g h j  k l z x c v b n m Q W E R T Y U I O P A S D F G H J  K L Z X C V B N M')
    'Q W E R T Y U I O P A S D F G H J  K L Z X C V B N M Q W E R T Y U I O P A S D F G H J  K L Z X C V B N M'
"""


def capitalize(string):
    return " ".join(s if not s or s[0].isdigit() else s.title() for s in string.split(" "))
