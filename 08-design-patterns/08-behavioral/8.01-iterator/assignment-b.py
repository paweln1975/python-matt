"""
Name: Protocol Iterator Implementation
Difficulty: easy
Lines: 9
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
Terminal: `python -m doctest -v assignment-b.py`

Tests:
>>> import sys; sys.tracebacklimit = 0
>>> assert sys.version_info >= (3, 9), \
'Python 3.9+ required'

>>> from inspect import isclass, ismethod

>>> assert isclass(User)

>>> mark = User('Mark', 'Watney')
>>> assert hasattr(mark, 'firstname')
>>> assert hasattr(mark, 'lastname')
>>> assert hasattr(mark, 'groups')
>>> assert hasattr(mark, '__iter__')
>>> assert hasattr(mark, '__next__')
>>> assert ismethod(mark.__iter__)
>>> assert ismethod(mark.__next__)

>>> mark = User('Mark', 'Watney', groups=(
...     Group(gid=1, name='admins'),
...     Group(gid=2, name='staff'),
...     Group(gid=3, name='managers'),
... ))

>>> for mission in mark:
...     print(mission)
Group(gid=1, name='admins')
Group(gid=2, name='staff')
Group(gid=3, name='managers')

"""

# %% SetUp

from dataclasses import dataclass

from typing import Callable
User: type
__iter__: Callable[[object], object]
__next__: Callable[[object], object]

@dataclass
class Group:
    gid: int
    name: str

# English
# 1. Modify classes to implement iterator protocol
# 2. Iterator should return instances of `Group`
# 3. Run doctests - all must succeed

# Polish
# 1. Zmodyfikuj klasy aby zaimplementować protokół iterator
# 2. Iterator powinien zwracać instancje `Group`
# 3. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
@dataclass
class User:
    firstname: str
    lastname: str
    groups: tuple = ()