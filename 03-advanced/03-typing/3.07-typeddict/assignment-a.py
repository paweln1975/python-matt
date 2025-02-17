"""
Name: Typing Annotations Mapping
Difficulty: easy
Lines: 4
Minutes: 2

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

>>> from typing import get_type_hints, is_typeddict
>>> assert is_typeddict(User), \
'Class `User` must be a `TypedDict`'

>>> get_type_hints(User)
{'firstname': <class 'str'>, 'lastname': <class 'str'>, 'age': <class 'int'>}

>>> data: User = {'firstname': 'Mark', 'lastname': 'Watney', 'age': 41}
>>> data
{'firstname': 'Mark', 'lastname': 'Watney', 'age': 41}

>>> data: User = User(**{'firstname': 'Mark', 'lastname': 'Watney', 'age': 41})
>>> data
{'firstname': 'Mark', 'lastname': 'Watney', 'age': 41}

>>> data: User = User(firstname='Mark', lastname='Watney', age=41)
>>> data
{'firstname': 'Mark', 'lastname': 'Watney', 'age': 41}

"""

# %% SetUp

from typing import TypedDict

# English
# 1. Define `User: TypedDict` with:
#    - `firstname: str`
#    - `lastname: str`
#    - `age: int`
# 2. Run doctests - all must succeed

# Polish
# 1. Zdefiniuj `User: TypedDict` z:
#    - `firstname: str`
#    - `lastname: str`
#    - `age: int`
# 2. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
class User(TypedDict):
    firstname: str
    lastname: str
    age: int