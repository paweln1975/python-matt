"""
Name: Accessor Reflection Delattr
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
Terminal: `python -m doctest -v assignment-a.py`

Tests:
>>> import sys; sys.tracebacklimit = 0
>>> assert sys.version_info >= (3, 9), \
'Python 3.9+ required'

>>> pt = Point(1, 2, 3)
>>> pt.x, pt.y, pt.z
(1, 2, 3)

>>> del pt.x
Traceback (most recent call last):
PermissionError: Cannot delete attributes

>>> del pt.notexisting
Traceback (most recent call last):
PermissionError: Cannot delete attributes

"""

# %% SetUp

from dataclasses import dataclass

from typing import Callable
Point: type
__delattr__: Callable[[object, str], None]

# English
# 1. Create class `Point` with `x`, `y`, `z` attributes
# 2. Prevent deleting attributes
# 3. Run doctests - all must succeed

# Polish
# 1. Stwórz klasę `Point` z atrybutami `x`, `y`, `z`
# 2. Zablokuj usuwanie atrybutów
# 3. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
@dataclass
class Point:
    x: int
    y: int
    z: int