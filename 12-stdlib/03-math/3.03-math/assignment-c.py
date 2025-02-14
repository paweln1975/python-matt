"""
Name: Math Algebra DistanceND
Difficulty: easy
Lines: 10
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
Terminal: `python -m doctest -v assignment-c.py`

Tests:
>>> import sys; sys.tracebacklimit = 0
>>> assert sys.version_info >= (3, 12), \
'Python 3.12+ required'

>>> result((0,0,0), (0,0,0))
0.0

>>> result((0,0,0), (1,1,1))
1.7320508075688772

>>> result((0,1,0,1), (1,1,0,0))
1.4142135623730951

>>> result((0,0,1,0,1), (1,1,0,0,1))
1.7320508075688772

>>> result((0,0,1,0,1), (1,1))
Traceback (most recent call last):
ValueError: Points must be in the same dimensions

Hints:
`for n1, n2 in zip(A, B)`

"""

# %% SetUp

from math import sqrt

from typing import Callable
type point = tuple[int,...]
result: Callable[[point, point], float]

# English
# 1. Given are two points `A: Sequence[int]` and `B: Sequence[int]`
# 2. Coordinates are in cartesian system
# 3. Points `A` and `B` are in `N`-dimensional space
# 4. Points `A` and `B` must be in the same space
# 5. Calculate distance between points using Euclidean algorithm
# 6. Run doctests - all must succeed

# Polish
# 1. Dane są dwa punkty `A: Sequence[int]` i `B: Sequence[int]`
# 2. Koordynaty są w systemie kartezjańskim
# 3. Punkty `A` i `B` są w `N`-wymiarowej przestrzeni
# 4. Punkty `A` i `B` muszą być w tej samej przestrzeni
# 5. Oblicz odległość między nimi wykorzystując algorytm Euklidesa
# 6. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
def result(A, B):
    ...