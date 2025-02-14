"""
Name: Numpy Dtype Astype
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
>>> assert result_b is not Ellipsis, \
'Assign result to variable: `result_b`'
>>> assert type(result_a) is np.ndarray, \
'Variable `result_a` has invalid type'
>>> assert type(result_b) is np.ndarray, \
'Variable `result_b` has invalid type'

>>> result_a
array([[-1,  0,  1],
       [ 2,  3,  4]])

>>> result_b
array([[ True, False,  True],
       [ True,  True,  True]])

"""

# %% SetUp

import numpy as np

result_a: np.ndarray
result_b: np.ndarray

DATA = np.array([[-1.1, 0.0, 1.1],
                 [2.2, 3.3, 4.4]])

# English
# 1. Given `DATA: np.ndarray` (see below)
# 2. Convert to `int` and save result as `result_int`
# 3. Convert to `bool` and save result as `result_bool`
# 4. What happened in each of those steps?
# 5. Run doctests - all must succeed

# Polish
# 1. Dany `DATA: np.ndarray` (patrz sekcja input)
# 2. Przekonwertuj do typu `int` i wynik zapisz jako `result_int`
# 3. Przekonwertuj do typu `bool` i wynik zapisz jako `result_bool`
# 4. Co się stało w każdym z tych kroków?
# 5. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
result_a = ...
result_b = ...