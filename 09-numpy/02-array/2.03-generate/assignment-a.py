"""
Name: Numpy Generate Zeros
Difficulty: easy
Lines: 1
Minutes: 2

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

>>> assert result is not Ellipsis, \
'Assign result to variable: `result`'
>>> assert type(result) is np.ndarray, \
'Variable `result` has invalid type, expected: np.ndarray'

>>> assert result.dtype == np.dtype('int64')
>>> assert result.itemsize == 8
>>> assert result.shape == (3, 3)
>>> assert result.strides == (24, 8)

>>> result
array([[0, 0, 0],
       [0, 0, 0],
       [0, 0, 0]])

"""

# %% SetUp

import numpy as np

result: np.ndarray

# English
# 1. Define `result: np.ndarray`:
#    - dtype: int64
#    - values: 0
#    - shape: 3 rows, 3 columns
#    - use: `np.zeros()`
# 2. Run doctests - all must succeed

# Polish
# 1. Zdefiniuj `result: np.ndarray`:
#    - dtype: int64
#    - wartości: 0
#    - shape: 3 wiersze, 3 kolumny
#    - użyj: `np.zeros()`
# 2. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
result = ...