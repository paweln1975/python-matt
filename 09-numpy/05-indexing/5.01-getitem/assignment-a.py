"""
Name: Numpy Indexing
Difficulty: easy
Lines: 5
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

>>> assert result is not Ellipsis, \
'Assign result to variable: `result`'
>>> assert type(result) is np.ndarray, \
'Variable `result` has invalid type, expected: np.ndarray'

>>> result
array([[3., 9.],
       [1., 4.]])

Hints:
`np.zeros(shape, dtype)`

"""

# %% SetUp

import numpy as np

result: np.ndarray

DATA = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

# English
# 1. Create `result: np.ndarray`
# 2. Add to `result` elements from `DATA` at indexes:
#    - row 0, column 2
#    - row 2, column 2
#    - row 0, column 0
#    - row 1, column 0
# 3. `result` size must be 2x2
# 4. `result` type must be float
# 5. Run doctests - all must succeed

# Polish
# 1. Stwórz `result: np.ndarray`
# 2. Dodaj do `result` elementy z `DATA` o indeksach:
#    - wiersz 0, kolumna 2
#    - wiersz 2, kolumna 2
#    - wiersz 0, kolumna 0
#    - wiersz 1, kolumna 0
# 3. Rozmiar `result` musi być 2x2
# 4. Typ `result` musi być float
# 5. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
result = ...