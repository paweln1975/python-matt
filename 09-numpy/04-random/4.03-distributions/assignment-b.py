"""
Name: Numpy Random Int
Difficulty: easy
Lines: 1
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

>>> assert result is not Ellipsis, \
'Assign result to variable: `result`'
>>> assert type(result) is np.ndarray, \
'Variable `result` has invalid type, expected: np.ndarray'

>>> result
array([[5, 0, 3, 3, 7, 9, 3, 5, 2, 4, 7, 6, 8, 8, 1, 6],
       [7, 7, 8, 1, 5, 9, 8, 9, 4, 3, 0, 3, 5, 0, 2, 3],
       [8, 1, 3, 3, 3, 7, 0, 1, 9, 9, 0, 4, 7, 3, 2, 7],
       [2, 0, 0, 4, 5, 5, 6, 8, 4, 1, 4, 9, 8, 1, 1, 7],
       [9, 9, 3, 6, 7, 2, 0, 3, 5, 9, 4, 4, 6, 4, 4, 3],
       [4, 4, 8, 4, 3, 7, 5, 5, 0, 1, 5, 9, 3, 0, 5, 0],
       [1, 2, 4, 2, 0, 3, 2, 0, 7, 5, 9, 0, 2, 7, 2, 9],
       [2, 3, 3, 2, 3, 4, 1, 2, 9, 1, 4, 6, 8, 2, 3, 0],
       [0, 6, 0, 6, 3, 3, 8, 8, 8, 2, 3, 2, 0, 8, 8, 3],
       [8, 2, 8, 4, 3, 0, 4, 3, 6, 9, 8, 0, 8, 5, 9, 0],
       [9, 6, 5, 3, 1, 8, 0, 4, 9, 6, 5, 7, 8, 8, 9, 2],
       [8, 6, 6, 9, 1, 6, 8, 8, 3, 2, 3, 6, 3, 6, 5, 7],
       [0, 8, 4, 6, 5, 8, 2, 3, 9, 7, 5, 3, 4, 5, 3, 3],
       [7, 9, 9, 9, 7, 3, 2, 3, 9, 7, 7, 5, 1, 2, 2, 8],
       [1, 5, 8, 4, 0, 2, 5, 5, 0, 8, 1, 1, 0, 3, 8, 8],
       [4, 4, 0, 9, 3, 7, 3, 2, 1, 1, 2, 1, 4, 2, 5, 5]])

"""

# %% SetUp

import numpy as np

result: np.ndarray

np.random.seed(0)

# English
# 1. Set random seed to zero
# 2. Define `result: np.ndarray` of size 16x16 with random integers `[0;9]` (inclusive)
# 3. Run doctests - all must succeed

# Polish
# 1. Ustaw ziarno losowości na zero
# 2. Zdefiniuj `result: np.ndarray` o rozmiarze 16x16 z losowymi liczbami całkowitymi `<0,9>` (włącznie)
# 3. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
result = np.random.randint(0, 10, size=(16, 16), dtype=np.int64)
