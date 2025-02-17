"""
Name: Typing Annotations NamedTuple
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
Terminal: `python -m doctest -v assignment-a.py`

Tests:
>>> import sys; sys.tracebacklimit = 0
>>> assert sys.version_info >= (3, 5), \
'Python 3.5+ required'

>>> from typing import get_type_hints
>>> get_type_hints(User)
{'firstname': <class 'str'>, 'lastname': <class 'str'>, 'age': <class 'int'>}

>>> data: User = User(firstname='Mark', lastname='Watney', age=42)
>>> data
User(firstname='Mark', lastname='Watney', age=42)

>>> data: User = User('Mark', 'Watney', 42)
>>> data
User(firstname='Mark', lastname='Watney', age=42)

>>> data: User = ('Mark', 'Watney', 42)
>>> data
('Mark', 'Watney', 42)

"""

# %% SetUp

from typing import NamedTuple

# English
# 1. Define `User: NamedTuple` with:
#    - `firstname: str`
#    - `lastname: str`
#    - `age: int`
# 2. Run doctests - all must succeed

# Polish
# 1. Zdefiniuj `User: NamedTuple` z:
#    - `firstname: str`
#    - `lastname: str`
#    - `age: int`
# 2. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
class User(NamedTuple):
    firstname: str
    lastname: str
    age: int
