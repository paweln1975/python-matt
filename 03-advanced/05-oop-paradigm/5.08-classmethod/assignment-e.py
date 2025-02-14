"""
Name: OOP MethodClassmethod FromJson
Difficulty: easy
Lines: 4
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
Terminal: `python -m doctest -v assignment-e.py`

Tests:
>>> import sys; sys.tracebacklimit = 0
>>> assert sys.version_info >= (3, 9), \
'Python 3.9+ required'

>>> from inspect import isclass

>>> assert isclass(Movie)
>>> assert isclass(ScienceFiction)
>>> assert isclass(History)
>>> assert isclass(Adventure)

>>> MARTIAN = '{"title":"Martian","director":"Ridley Scott"}'
>>> martian = ScienceFiction.from_json(MARTIAN)
>>> assert type(martian.title) is str
>>> assert type(martian.director) is str
>>> assert martian.title == 'Martian'
>>> assert martian.director == 'Ridley Scott'

>>> DUNE = '{"title":"Dune","director":"Denis Villeneuve"}'
>>> dune = Adventure.from_json(DUNE)
>>> assert type(dune.title) is str
>>> assert type(dune.director) is str
>>> assert dune.title == 'Dune'
>>> assert dune.director == 'Denis Villeneuve'

>>> RIGHT_STUFF = '{"title":"The Right Stuff","director":"Philip Kaufman"}'
>>> right_stuff = History.from_json(RIGHT_STUFF)
>>> assert type(right_stuff.title) is str
>>> assert type(right_stuff.director) is str
>>> assert right_stuff.title == 'The Right Stuff'
>>> assert right_stuff.director == 'Philip Kaufman'

Hints:
`json.loads()`

"""

# %% SetUp

import json

from typing import Callable
Movie: type
from_json: Callable[[type, str], object]

# English
# 1. Modify class `Movie`
# 2. Define classmethod `from_json()`:
#    - parameter `string: str`, example: '{"title":"Martian","director":"Ridley Scott"}'
#    - returns instance of a class on which was called
# 3. Run doctests - all must succeed

# Polish
# 1. Zmodyfikuj klasę `Movie`
# 2. Define classmethod `from_json()`:
#    - parametr `string: str`, przykład: '{"title":"Martian","director":"Ridley Scott"}'
#    - zwraca instancję klasy na której została wykonana
# 3. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
class Movie:
    def __init__(self, title, director):
        self.title = title
        self.director = director

    @classmethod
    def from_json(cls, string: str):
        ...

class ScienceFiction(Movie):
    pass

class History(Movie):
    pass

class Adventure(Movie):
    pass