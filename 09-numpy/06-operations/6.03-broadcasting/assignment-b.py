"""
Name: Numpy Broadcasting Type Cast
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
Terminal: `python -m doctest -v assignment-b.py`

Tests:
>>> import sys; sys.tracebacklimit = 0
>>> assert sys.version_info >= (3, 9), \
'Python 3.9+ required'

>>> assert type(result_ab) is np.ndarray, \
'Variable `result_ab` has invalid type, expected: np.ndarray'
>>> assert type(result_ba) is np.ndarray, \
'Variable `result_ba` has invalid type, expected: np.ndarray'

>>> result_ab
array([[5, 1],
       [2, 3]])

>>> result_ba
array([[5, 1],
       [2, 3]])

"""

# %% SetUp

import numpy as np

result_ab: np.ndarray
result_ba: np.ndarray

a = np.array([[1, 0], [0, 1]])
b = [[4, 1], [2, 2]]

# English
# 1. For given: `a: np.ndarray`, `b: np.ndarray` (see below)
# 2. Add `a` and `b`
# 3. Add `b` and `a`
# 4. What happened?
# 5. Run doctests - all must succeed

# Polish
# 1. Dla danych: `a: np.ndarray`, `b: np.ndarray` (patrz sekcja input)
# 2. Dodaj `a` i `b`
# 3. Dodaj `b` i `a`
# 4. Co się stało?
# 5. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
result_ab = a + b
result_ba = b + a
