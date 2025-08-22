"""
Name: Numpy Algebra Euclidean 2D
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

>>> assert result((0,0), (0,0)) is not Ellipsis, \
'Assign result to function: `euclidean_distance`'

>>> a = (1, 0)
>>> b = (0, 1)
>>> result(a, b)
1.4142135623730951

>>> result((0,0), (1,0))
1.0

>>> result((0,0), (1,1))
1.4142135623730951

>>> result((0,1), (1,1))
1.0

>>> result((0,10), (1,1))
9.055385138137417

"""

# %% SetUp

from math import sqrt

from typing import Callable

import numpy as np

type point = tuple[int,int]
result: Callable[[point, point], point]

# English
# 1. Given are two points `a: tuple[int, int]` and `b: tuple[int, int]`
# 2. Coordinates are in cartesian system
# 3. Points `a` and `b` are in two dimensional space
# 4. Calculate distance between points using Euclidean algorithm
# 5. Run doctests - all must succeed

# Polish
# 1. Dane są dwa punkty `a: tuple[int, int]` i `b: tuple[int, int]`
# 2. Koordynaty są w systemie kartezjańskim
# 3. Punkty `a` i `b` są w dwuwymiarowej przestrzeni
# 4. Oblicz odległość między nimi wykorzystując algorytm Euklidesa
# 5. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
def result(a, b):
    p1 = np.array(a)
    p2 = np.array(b)
    return np.sqrt(np.sum((p1 - p2) ** 2)).item()