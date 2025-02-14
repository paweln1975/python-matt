"""
Name: Accessor Reflection Setattr
Difficulty: easy
Lines: 4
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
Terminal: `python -m doctest -v assignment-b.py`

Tests:
>>> import sys; sys.tracebacklimit = 0
>>> assert sys.version_info >= (3, 9), \
'Python 3.9+ required'

>>> pt = Point(1, 2, 3)
>>> pt.x, pt.y, pt.z
(1, 2, 3)
>>> pt.notexisting = 10
Traceback (most recent call last):
PermissionError: Cannot set other attributes than x, y, z
>>> pt.x = 10
>>> pt.y = 20
>>> pt.z = 30
>>> pt.x, pt.y, pt.z
(10, 20, 30)

"""

# %% SetUp

from dataclasses import dataclass

from typing import Callable
Point: type
__setattr__: Callable[[object, str, int], None]

# English
# 1. Create class `Point` with `x`, `y`, `z` attributes
# 2. Prevent creation of new attributes
# 3. Allow to modify values of `x`, `y`, `z`
# 4. Run doctests - all must succeed

# Polish
# 1. Stwórz klasę `Point` z atrybutami `x`, `y`, `z`
# 2. Zablokuj tworzenie nowych atrybutów
# 3. Zezwól na modyfikowanie wartości `x`, `y`, `z`
# 4. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
@dataclass
class Point:
    x: int
    y: int
    z: int