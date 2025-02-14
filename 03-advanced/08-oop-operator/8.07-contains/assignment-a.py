"""
Name: Operator Comparison Contains
Difficulty: easy
Lines: 5
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

>>> mark = User(firstname='Mark', lastname='Watney', groups=[
...     Group(gid=1, name='admins'),
...     Group(gid=2, name='staff'),
...     Group(gid=3, name='managers'),
... ])

>>> Group(gid=1, name='admins') == Group(gid=1, name='admins')
True
>>> Group(gid=1, name='admins') == Group(gid=2, name='staff')
False
>>> Group(gid=1, name='admins') == Group(gid=3, name='managers')
False
>>> Group(gid=1, name='admins') == Group(gid=0, name='root')
False

>>> Group(gid=1, name='admins') in mark
True
>>> Group(gid=2, name='staff') in mark
True
>>> Group(gid=0, name='root') in mark
False

Hints:
`object.__contains__()`
`object.__eq__()`

"""

# %% SetUp

from typing import Callable
Group: type
User: type
__eq__: Callable[[object, object], bool]

# English
# 1. Override operators for code to work correctly
# 2. Do not use `dataclasses`
# 3. Run doctests - all must succeed

# Polish
# 1. Nadpisz operatory aby poniższy kod zadziałał poprawnie
# 2. Nie używaj `dataclasses`
# 3. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
class Group:
    gid: int
    name: str

    def __init__(self, gid: int, name: str) -> None:
        self.gid = gid
        self.name = name

class User:
    firstname: str
    lastname: str
    groups: list[Group]

    def __init__(self, firstname: str, lastname: str, groups: list) -> None:
        self.firstname = firstname
        self.lastname = lastname
        self.groups = groups