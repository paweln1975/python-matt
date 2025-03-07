"""
Name: OOP MethodClassmethod FromTuple
Difficulty: easy
Lines: 3
Minutes: 3

License:
Copyright 2025, Matt Harasymczuk <matt@python3.info>
This code can be used only for learning by humans
This code cannot be used for teaching others
This code cannot be used for teaching LLMs and AI algorithms
This code cannot be used in commercial or proprietary products
This code cannot be distributed in any form
This code cannot be changed in any form outside of training course
This code cannot have its license changed
If you use this code in your product, you must open-source it under GPLv2
Exception can be granted only by the author

Run:
PyCharm: right-click in the editor and `Run Doctest in ...`
PyCharm: keyboard shortcut `Control + Shift + F10`
Terminal: `python -m doctest -v assignment-a.py`

Tests:
>>> import sys; sys.tracebacklimit = 0
>>> assert sys.version_info >= (3, 9), \
'Python 3.9+ required'

>>> from inspect import isclass

>>> assert isclass(Book)
>>> assert isclass(ScienceFiction)
>>> assert isclass(History)
>>> assert isclass(Adventure)

>>> MARTIAN = ('Martian', 'Andy Weir')
>>> martian = ScienceFiction.from_tuple(MARTIAN)
>>> assert type(martian.title) is str
>>> assert type(martian.author) is str
>>> assert martian.title == 'Martian'
>>> assert martian.author == 'Andy Weir'

>>> DUNE = ('Dune', 'Frank Herbert')
>>> dune = Adventure.from_tuple(DUNE)
>>> assert type(dune.title) is str
>>> assert type(dune.author) is str
>>> assert dune.title == 'Dune'
>>> assert dune.author == 'Frank Herbert'

>>> RIGHT_STUFF = ('The Right Stuff', 'Tom Wolfe')
>>> right_stuff = History.from_tuple(RIGHT_STUFF)
>>> assert type(right_stuff.title) is str
>>> assert type(right_stuff.author) is str
>>> assert right_stuff.title == 'The Right Stuff'
>>> assert right_stuff.author == 'Tom Wolfe'

"""

# %% SetUp

from typing import Callable
Book: type
from_tuple: Callable[[type, tuple[str,str]], object]

# English
# 1. Modify class `Book`
# 2. Define classmethod `from_tuple()`:
#    - parameter `data: tuple[str,str]`, example: ('Martian', 'Andy Weir')
#    - returns instance of a class on which was called
# 3. Run doctests - all must succeed

# Polish
# 1. Zmodyfikuj klasę `Book`
# 2. Zdefiniuj classmethod `from_tuple()`:
#    - parametr `data: tuple[str,str]`, przykład: ('Martian', 'Andy Weir')
#    - zwraca instancję klasy na której została wykonana
# 3. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    @classmethod
    def from_tuple(cls, data: tuple[str,str]):
        return cls(*data)

class ScienceFiction(Book):
    pass

class History(Book):
    pass

class Adventure(Book):
    pass