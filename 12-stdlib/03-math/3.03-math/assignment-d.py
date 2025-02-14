"""
Name: Math Algebra Matmul
Difficulty: hard
Lines: 13
Minutes: 21

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
Terminal: `python -m doctest -v assignment-d.py`

Tests:
>>> import sys; sys.tracebacklimit = 0
>>> assert sys.version_info >= (3, 12), \
'Python 3.12+ required'

>>> A = [[1, 0],
...      [0, 1]]
>>>
>>> B = [[4, 1],
...      [2, 2]]
>>>
>>> result(A, B)
[[4, 1], [2, 2]]

>>> A = [[1,0,1,0],
...      [0,1,1,0],
...      [3,2,1,0],
...      [4,1,2,0]]
>>>
>>> B = [[4,1],
...      [2,2],
...      [5,1],
...      [2,3]]
>>>
>>> result(A, B)
[[9, 2], [7, 3], [21, 8], [28, 8]]

Hints:
Zero matrix
Three nested `for` loops

"""

# %% SetUp

from typing import Callable
type matrix = list[list[int]]
result: Callable[[matrix, matrix], matrix]

# English
# 1. Multiply matrices using nested `for` loops
# 2. Do not use any library, such as: `numpy`, `pandas`, itp
# 3. Run doctests - all must succeed

# Polish
# 1. Pomnóż macierze wykorzystując zagnieżdżone pętle `for`
# 2. Nie wykorzystuj żadnej biblioteki, tj.: `numpy`, `pandas`, itp
# 3. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
def result(A, B):
    ...