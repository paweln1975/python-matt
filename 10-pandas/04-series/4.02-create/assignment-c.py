"""
Name: Series Create Randint
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
Terminal: `python -m doctest -v assignment-c.py`

Tests:
>>> import sys; sys.tracebacklimit = 0
>>> assert sys.version_info >= (3, 9), \
'Python 3.9+ required'

>>> assert result is not Ellipsis, \
'Assign result to variable: `result`'
>>> assert type(result) is pd.Series, \
'Variable `result` has invalid type, should be `pd.Series`'

>>> result
0    5
1    0
2    3
3    3
4    7
5    9
6    3
7    5
8    2
9    4
dtype: int64

"""

# %% SetUp

import pandas as pd
import numpy as np

result: pd.Series

np.random.seed(0)

# English
# 1. Set random seed to zero
# 2. Create `result: pd.Series` with 10 random digits (`int` from `0` to `9`)
# 3. Run doctests - all must succeed

# Polish
# 1. Ustaw ziarno losowości na zero
# 2. Stwórz `result: pd.Series` z 10 losowymi cyframi  (`int` from `0` to `9`)
# 3. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
result = ...