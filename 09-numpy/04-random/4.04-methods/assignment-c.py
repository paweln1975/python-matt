"""
Name: Numpy Random Choice
Difficulty: medium
Lines: 1
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
array([30,  5, 27, 31, 33, 38])

"""

# %% SetUp

import numpy as np

result: np.ndarray

np.random.seed(0)

DATA = np.arange(1, 50)

# English
# 1. Set random seed to zero
# 2. Define `result: np.ndarray` with 6 random numbers
#    without repetition from `DATA`
# 3. Run doctests - all must succeed

# Polish
# 1. Ustaw ziarno losowości na zero
# 2. Zdefiniuj `result: np.ndarray` z 6 losowymi
#    liczbami bez powtórzeń z `DATA`
# 3. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
result = np.random.choice(DATA, size=6, replace=False)
