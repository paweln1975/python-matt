"""
Name: Numpy Round Clip
Difficulty: medium
Lines: 2
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
>>> assert sys.version_info >= (3, 9), \
'Python 3.9+ required'

>>> assert result is not Ellipsis, \
'Assign result to variable: `result`'
>>> assert type(result) is np.ndarray, \
'Variable `result` has invalid type, expected: np.ndarray'

>>> result
array([[50, 47, 64],
       [67, 67,  9],
       [80, 21, 36],
       [80, 70, 88],
       [80, 12, 58],
       [65, 39, 87],
       [50, 88, 81]])

Hints:
`result[:, 0]`

"""

# %% SetUp

import numpy as np

result: np.ndarray

DATA = np.array([[44, 47, 64],
                 [67, 67,  9],
                 [83, 21, 36],
                 [87, 70, 88],
                 [88, 12, 58],
                 [65, 39, 87],
                 [46, 88, 81]])

# English
# 1. Create `result: np.ndarray` copy of `DATA`
# 2. Clip numbers only in first column to 50 (inclusive) to 80 (exclusive)
# 3. Print `result`
# 4. Run doctests - all must succeed

# Polish
# 1. Stwórz `result: np.ndarray` z kopią danych z `DATA`
# 2. Przytnij liczby w pierwszej kolumnie od 50 (włącznie) do 80 (rozłącznie)
# 3. Wypisz `result`
# 4. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
result = ...