"""
Name: Numpy Round Floor and Ceil
Difficulty: medium
Lines: 3
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

>>> assert result_a is not Ellipsis, \
'Assign result to variable: `result_a`'
>>> assert type(result_a) is np.ndarray, \
'Variable `result_a` has invalid type, expected: np.ndarray'

>>> assert result_b is not Ellipsis, \
'Assign result to variable: `result_b`'
>>> assert type(result_b) is np.ndarray, \
'Variable `result_b` has invalid type, expected: np.ndarray'

>>> assert result_c is not Ellipsis, \
'Assign result to variable: `result_c`'
>>> assert type(result_c) is np.ndarray, \
'Variable `result_c` has invalid type, expected: np.ndarray'

>>> result_a
array([1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1.,
       1., 1., 1., 1.])

>>> result_b
array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
       0., 0., 0., 0.])

>>> result_c
array([1., 1., 1., 1., 0., 1., 0., 1., 1., 0., 1., 1., 1., 1., 0., 0., 0.,
       1., 1., 1., 1.])

"""

# %% SetUp

import numpy as np

result_a: np.ndarray
result_b: np.ndarray
result_c: np.ndarray

np.random.seed(0)

DATA = np.array([0.5488135 , 0.71518937, 0.60276338, 0.54488318, 0.4236548 ,
                 0.64589411, 0.43758721, 0.891773  , 0.96366276, 0.38344152,
                 0.79172504, 0.52889492, 0.56804456, 0.92559664, 0.07103606,
                 0.0871293 , 0.0202184 , 0.83261985, 0.77815675, 0.87001215,
                 0.97861834])

# English
# 1. Ceil round `data` values and assign to `result_a`
# 2. Floor round `data` values and assign to `result_b`
# 3. Round `data` values and assign to `result_c`
# 4. Run doctests - all must succeed

# Polish
# 1. Zaokrąglij wartości `data` w górę (ceil) i przypisz do `result_a`
# 2. Zaokrąglij wartości `data` w dół (floor) i przypisz do `result_b`
# 3. Zaokrąglij wartości `data` i przypisz do `result_c`
# 4. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
result_a = ...
result_b = ...
result_c = ...