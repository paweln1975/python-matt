"""
Name: DesignPatterns Behavioral Iterator
Difficulty: easy
Lines: 9
Minutes: 5

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

>>> crew = Crew()
>>> crew += 'Mark Watney'
>>> crew += 'Jose Jimenez'
>>> crew += 'Melissa Lewis'
>>>
>>> for member in crew:
...     print(member)
Mark Watney
Jose Jimenez
Melissa Lewis

"""

# %% SetUp

from typing import Callable
Crew: type
__iadd__: Callable[[object, str], object]
__iter__: Callable[[object], object]
__next__: Callable[[object], str]

# English
# 1. Implement Iterator pattern
# 2. Run doctests - all must succeed

# Polish
# 1. Zaimplementuj wzorzec Iterator
# 2. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
class Crew:
    def __init__(self):
        self.members = list()

    def __iadd__(self, other):
        self.members.append(other)
        return self