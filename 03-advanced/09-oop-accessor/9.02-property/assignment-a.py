"""
Name: Accessor Property Deleter
Difficulty: easy
Lines: 6
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

>>> pt = Point()
>>> pt.x = 1
>>> pt.y = 2
>>> pt.z = 3

>>> del pt.position
>>> assert pt.x == 0
>>> assert pt.y == 0
>>> assert pt.z == 0

"""

# %% SetUp

from typing import Callable
Point: type
position: Callable[[object], None]

# English
# 1. Define class `Point` with `x`, `y`, `z` attributes
# 2. Define property `position` in class `Point`
# 3. Deleting `position` sets all attributes to 0 (`x=0`, `y=0`, `z=0`)
# 4. Run doctests - all must succeed

# Polish
# 1. Zdefiniuj klasę `Point` z atrybutami `x`, `y`, `z`
# 2. Zdefiniuj property `position` w klasie `Point`
# 3. Usunięcie `position` ustawia wszystkie atrybuty na 0 (`x=0`, `y=0`, `z=0`)
# 4. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
class Point:
    x: int
    y: int
    z: int

    def position():
        ...