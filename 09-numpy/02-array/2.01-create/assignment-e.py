"""
Name: Numpy Create ArangeDtype
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
Terminal: `python -m doctest -v assignment-e.py`

Tests:
>>> import sys; sys.tracebacklimit = 0
>>> assert sys.version_info >= (3, 9), \
'Python 3.9+ required'

>>> assert result is not Ellipsis, \
'Assign result to variable: `result`'
>>> assert type(result) is np.ndarray, \
'Variable `result` has invalid type, expected: np.ndarray'

>>> result
array([0., 2., 4., 6., 8.])

"""

# %% SetUp

import numpy as np

result: np.ndarray

# English
# 1. Define `result: np.ndarray`:
#    - dtype: float
#    - values: from 0 to 10 step 2 (even numbers)
#    - use: `np.arange()`
# 2. Run doctests - all must succeed

# Polish
# 1. Zdefiniuj `result: np.ndarray`:
#    - dtype: float
#    - wartości: od 0 do 10 krok 2 (liczby parzyste)
#    - użyj: `np.arange()`
# 2. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
result = ...