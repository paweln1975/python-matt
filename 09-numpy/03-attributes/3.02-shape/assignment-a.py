"""
Name: Numpy Shape 1d
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
'Variable `result_a` has invalid type'

>>> assert result_b is not Ellipsis, \
'Assign result to variable: `result_b`'
>>> assert type(result_b) is np.ndarray, \
'Variable `result_b` has invalid type'

>>> assert result_c is not Ellipsis, \
'Assign result to variable: `result_c`'
>>> assert type(result_c) is np.ndarray, \
'Variable `result_c` has invalid type'

>>> result_b
array([1, 2, 3, 4, 5, 6, 7, 8, 9])

>>> result_a
array([1, 2, 3, 4, 5, 6, 7, 8, 9])

>>> result_c
array([[1, 2, 3, 4, 5, 6, 7, 8, 9]])

"""

# %% SetUp

import numpy as np

result_a: np.ndarray
result_b: np.ndarray
result_c: np.ndarray

DATA = np.array([[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]])

# English
# 1. Define `result_ravel` with result of flattening `DATA` using `.ravel()` method
# 2. Define `result_flatten` with result of flattening `DATA` using `.flatten()` method
# 3. Define `result_reshape` with result of reshaping `DATA` into 1x9
# 4. Run doctests - all must succeed

# Polish
# 1. Zdefiniuj `result_ravel` z wynikiem spłaszczenia `DATA` używając metody `.ravel()`
# 2. Zdefiniuj `result_flatten` z wynikiem spłaszczenia `DATA` używając metody `.flatten()`
# 3. Zdefiniuj `result_reshape` z wynikiem zmiany kształtu `DATA` na 1x9
# 4. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
result_a = ...
result_b = ...
result_c = ...