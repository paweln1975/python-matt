"""
Name: Numpy Sort
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

>>> assert result_a is not Ellipsis, \
'Assign result to variable: `result_a`'
>>> assert type(result_a) is np.ndarray, \
'Variable `result_a` has invalid type, expected: np.ndarray'

>>> assert result_b is not Ellipsis, \
'Assign result to variable: `result_b`'
>>> assert type(result_b) is np.ndarray, \
'Variable `result_b` has invalid type, expected: np.ndarray'

>>> result_a
array([[44, 47, 64, 67],
       [ 9, 21, 67, 83],
       [36, 70, 87, 88]])

>>> result_b
array([[36, 87, 70, 88],
       [67,  9, 83, 21],
       [44, 47, 64, 67]])

Hints:
`.sort()` returns `None`

"""

# %% SetUp

import numpy as np

result_a: np.ndarray
result_b: np.ndarray

DATA = np.array([[44, 47, 64, 67],
                 [67,  9, 83, 21],
                 [36, 87, 70, 88]])

# English
# 1. Define `result_a` with sorted `DATA` by columns
# 2. Define `result_b` with flipped `DATA` by rows
# 3. Run doctests - all must succeed

# Polish
# 1. Zdefiniuj `result_a` z posortowanym `DATA` po kolumnach
# 2. Zdefiniuj `result_b` z flipniętym `DATA` po wierszach
# 3. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
result_a = ...
result_b = ...