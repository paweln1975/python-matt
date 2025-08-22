"""
Name: Numpy Methods
Difficulty: easy
Lines: 4
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
array([[nan, nan, nan],
       [47.,  9., 87.],
       [64., 83., 70.],
       [ 0.,  0.,  0.]])

"""

# %% SetUp

import numpy as np

DATA = np.array([[44, 47, 64, 67],
                 [67,  9, 83, 21],
                 [36, 87, 70, 88]])

# English
# 1. Reshape `result` to 3x4
# 2. Fill last column with zeros (0)
# 3. Transpose `result`
# 4. Convert `result` to float
# 5. Fill first row with `np.nan`
# 6. Run doctests - all must succeed

# Polish
# 1. Zmień kształt na 3x4
# 2. Wypełnij ostatnią kolumnę zerami (0)
# 3. Transponuj `result`
# 4. Przekonwertuj `result` do float
# 5. Wypełnij pierwszy wiersz `np.nan`
# 6. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
result = DATA.reshape(3, 4)
result[:, -1] = 0
result = result.T.astype(float)
result[0, :] = np.nan
