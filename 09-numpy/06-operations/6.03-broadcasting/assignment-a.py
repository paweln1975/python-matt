"""
Name: Numpy Broadcasting Arithmetic
Difficulty: easy
Lines: 4
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

>>> assert result is not Ellipsis, \
'Assign result to variable: `result`'
>>> assert type(result) is np.ndarray, \
'Variable `result` has invalid type, expected: np.ndarray'

>>> result
array([[ 1.41421356,  2.73205081],
       [45.254834  ,  0.        ]])

"""

# %% SetUp

import numpy as np

a: np.ndarray
b: np.ndarray
c: np.ndarray
result: np.ndarray

A = np.array([[0, 1], [2, 3]], dtype='float')
B = np.array([2, 3], dtype='float')
C = np.array([[1, 1], [4, 0]], dtype='float')

# English
# 1. Define `a: np.ndarray` with square root of each element in `A`
# 2. Define `b: np.ndarray` with square root of each element in `B`
# 3. Define `c: np.ndarray` with second power (square) of each element in `C`
# 4. Add elements from `a` to `b`
# 5. Multiply the result by `c`
# 6. Run doctests - all must succeed

# Polish
# 1. Zdefiniuj `a: np.ndarray` z pierwiastkiem kwadratowym każdego elementu `A`
# 2. Zdefiniuj `b: np.ndarray` z pierwiastkiem kwadratowym każdego elementu `B`
# 3. Zdefiniu `c: np.ndarray` z drugą potęgą (kwadratem) każdego z elementu w `C`
# 4. Dodaj elementy z `a` do `b`
# 5. Przemnóż wynik przez `c`
# 6. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
a = ...
b = ...
c = ...
result = ...