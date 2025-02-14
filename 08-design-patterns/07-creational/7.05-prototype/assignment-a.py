"""
Name: DesignPatterns Creational PrototypeDate
Difficulty: easy
Lines: 5
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

>>> date = Date(1969, 7, 21)
>>> result = date.clone()

>>> result.year
1969
>>> result.month
7
>>> result.day
21

"""

# %% SetUp

from dataclasses import dataclass

from typing import Callable
Date: type
clone: Callable[[object], object]

# English
# 1. Create class `Date` with:
#    - `year: int`
#    - `month: int`
#    - `day: int`
#    - method `.clone()`
# 2. Method `.clone()` returns another `Date` with the same values
# 3. Do not use `vars(self)`
# 4. Run doctests - all must succeed

# Polish
# 1. Stwórz klasę `Date` z:
#    - `year: int`
#    - `month: int`
#    - `day: int`
#    - metodą `.clone()`
# 2. Metoda `.clone()` zwraca kolejny `Date` z tymi samymi wartościami
# 3. Nie używaj `vars(self)`
# 4. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
@dataclass
class Date:
    year: int
    month: int
    day: int