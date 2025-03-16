"""
Name: Operator Increment Add
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

>>> from pprint import pprint

>>> mark = User(firstname='Mark', lastname='Watney', groups=[])
>>> mark += Group(1, 'admins')
>>> mark += Group(2, 'staff')

>>> pprint(mark, width=50)
User(firstname='Mark',
     lastname='Watney',
     groups=[Group(gid=1, name='admins'),
             Group(gid=2, name='staff')])

Hints:
`object.__iadd__() -> self`

"""

# %% SetUp

from dataclasses import dataclass

Group: type
User: type

@dataclass
class Group:
    gid: int
    name: str

# English
# 1. Overload operator `+=`
# 2. Make `User` objects able to add `Groups`, for example:
#    - `mark = User(firstname='Mark', lastname='Watney')`
#    - `mark += Group(1, 'admins')`
#    - `mark += Group(2, 'staff')`
# 3. Run doctests - all must succeed

# Polish
# 1. Przeciąż operator `+=`
# 2. Spraw aby do obiektów klasy `User` można dodać `Group`, przykład:
#    - `mark = User(firstname='Mark', lastname='Watney')`
#    - `mark += Group(1, 'admins')`
#    - `mark += Group(2, 'staff')`
# 3. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
@dataclass
class User:
    firstname: str
    lastname: str
    groups: list[Group]

    def __iadd__(self, other):
        if isinstance(other, Group):
            if not other in self.groups:
                self.groups.append(other)
        return self
