"""
Name: Dataclass Definition AccessModifiers
Difficulty: easy
Lines: 6
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
>>> assert sys.version_info >= (3, 9), \
'Python 3.9+ required'

>>> from inspect import isclass

>>> assert isclass(User)
>>> assert hasattr(User, '__annotations__')

>>> assert 'firstname' in User.__dataclass_fields__
>>> assert 'lastname' in User.__dataclass_fields__

Hints:
Public attribute name starts with a lowercase letter

"""

# %% SetUp

from dataclasses import dataclass

User: type

# English
# 1. Modify dataclass `User` to add attributes:
#    - Public: `firstname`, `lastname`
# 2. Run doctests - all must succeed

# Polish
# 1. Zmodyfikuj dataclass `User` aby dodać atrybuty:
#    - Publiczne: `firstname`, `lastname`
# 2. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
@dataclass
class User:
    ...