"""
Name: Math Algebra Distance2D
Difficulty: easy
Lines: 5
Minutes: 8

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
>>> assert sys.version_info >= (3, 12), \
'Python 3.12+ required'

>>> A = (1, 0)
>>> B = (0, 1)
>>> result(A, B)
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
type point = tuple[int,int]
result: Callable[[point, point], float]

# English
# 1. Given are two points `A: tuple[int, int]` and `B: tuple[int, int]`
# 2. Coordinates are in cartesian system
# 3. Points `A` and `B` are in two dimensional space
# 4. Calculate distance between points using Euclidean algorithm
# 5. Run doctests - all must succeed

# Polish
# 1. Dane są dwa punkty `A: tuple[int, int]` i `B: tuple[int, int]`
# 2. Koordynaty są w systemie kartezjańskim
# 3. Punkty `A` i `B` są w dwuwymiarowej przestrzeni
# 4. Oblicz odległość między nimi wykorzystując algorytm Euklidesa
# 5. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
def result(A, B):
    ...