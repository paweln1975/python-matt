"""
Name: OOP ObjectConstructor Syntax
Difficulty: easy
Lines: 6
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
Terminal: `python -m doctest -v assignment-a.py`

Tests:
>>> import sys; sys.tracebacklimit = 0
>>> assert sys.version_info >= (3, 9), \
'Python 3.9+ required'

>>> from inspect import isclass

>>> assert isclass(Point)
>>> assert hasattr(Point, '__new__')
>>> assert hasattr(Point, '__init__')
>>> pt = Point(1, 2)
>>> assert type(pt) is Point
>>> assert pt.x == 1
>>> assert pt.y == 2

"""

# %% SetUp

from typing import Callable
Point: type
__new__: Callable[[type, int, int], type]
__init__: Callable[[object, int, int], None]

# English
# 1. Define class `Point` with methods:
#    - `__new__()` taking `x` and `y` and returns new class instance
#    - `__init__()` takes `x` and `y` and stores them as attributes
# 2. Run doctests - all must succeed

# Polish
# 1. Zdefiniuj klasę `Point` z metodami:
#    - `__new__()` przyjmuje  `x` i `y` i zwraca nową instancję klasy
#    - `__init__()` przyjmuje `x` i `y` i zapisuje je jako atrybuty
# 2. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
class Point:
    ...