"""
Name: Dataclass Mutability list
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

>>> assert isclass(User)
>>> assert hasattr(User, '__annotations__')

>>> assert 'firstname' in User.__dataclass_fields__
>>> assert 'lastname' in User.__dataclass_fields__
>>> assert 'groups' in User.__dataclass_fields__

>>> mark = User('mwatney', 'Ares3')
>>> assert mark.firstname == 'mwatney'
>>> assert mark.lastname == 'Ares3'
>>> assert mark.groups == []

>>> melissa = User('mlewis', 'Nasa1')
>>> assert melissa.firstname == 'mlewis'
>>> assert melissa.lastname == 'Nasa1'
>>> assert melissa.groups == []

>>> assert id(mark.groups) != id(melissa.groups)

Hints:
`field(default_factory=list)`

"""

# %% SetUp

from dataclasses import dataclass, field

User: type

# English
# 1. Create dataclass `User`, with attributes:
#    - `firstname: str` (required)
#    - `lastname: str` (required)
#    - `groups: list[str]` (optional)
# 2. Attributes must be set at the initialization from constructor arguments
# 3. Avoid mutable parameter problem
# 4. Run doctests - all must succeed

# Polish
# 1. Stwórz dataklasę `User`, z atrybutami:
#    - `firstname: str` (wymagane)
#    - `lastname: str` (wymagane)
#    - `groups: list[str]` (opcjonalne)
# 2. Atrybuty mają być ustawiane przy inicjalizacji z parametrów konstruktora
# 3. Uniknij problemu mutowalnych parametrów
# 4. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
@dataclass
class User:
    ...