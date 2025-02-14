"""
Name: DesignPatterns Creational PrototypeTime
Difficulty: easy
Lines: 2
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

>>> from pprint import pprint

>>> time = Time(2, 56, 15)
>>> result = time.clone()

>>> result.hour
2
>>> result.minute
56
>>> result.second
15
>>> result.microsecond
0

"""

# %% SetUp

from dataclasses import dataclass

from typing import Callable
Date: type
clone: Callable[[object], object]

# English
# 1. Create class `Time` with:
#    - `hour: int`
#    - `minute: int`
#    - `second: int`
#    - `microsecond: int`
#    - method `.clone()`
# 2. Method `.clone()` returns another `Time` with the same values
# 3. Use `vars(self)`
# 4. Run doctests - all must succeed

# Polish
# 1. Stwórz klasę `Time` z:
#    - `hour: int`
#    - `minute: int`
#    - `second: int`
#    - `microsecond: int`
#    - metodą `.clone()`
# 2. Metoda `.clone()` zwraca kolejny `Time` z tymi samymi wartościami
# 3. Użyj `vars(self)`
# 4. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
@dataclass
class Time:
    hour: int = 0
    minute: int = 0
    second: int = 0
    microsecond: int = 0