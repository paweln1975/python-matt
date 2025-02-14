"""
Name: Series Sample
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
Terminal: `python -m doctest -v assignment-e.py`

Tests:
>>> import sys; sys.tracebacklimit = 0
>>> pd.set_option('display.width', 250)
>>> pd.set_option('display.max_columns', 20)
>>> pd.set_option('display.max_rows', 30)

>>> assert result is not Ellipsis, \
'Assign result to variable: `result`'
>>> assert type(result) is pd.Series, \
'Variable `result` has invalid type, should be `pd.Series`'

>>> result
2000-01-07    0.950088
2000-01-08   -0.151357
2000-01-08   -0.151357
2000-01-09   -0.103219
2000-01-02    0.400157
2000-01-06   -0.977278
2000-01-10    0.410599
2000-01-09   -0.103219
2000-01-10    0.410599
2000-01-05    1.867558
2000-01-04    2.240893
2000-01-01    1.764052
dtype: float64

Hints:
`Series.sample(frac, replace)`

"""

# %% SetUp

import pandas as pd
import numpy as np

result: pd.Series

np.random.seed(0)

s = pd.Series(
    data=np.random.randn(10),
    index=pd.date_range('2000-01-01', freq='D', periods=10))

# English
# 1. Define variable `result` with 125% of random elements with replacement from `DATA`
# 2. Run doctests - all must succeed

# Polish
# 1. Zdefiniuj zmienną `result` z 125% losowych elementów z powtórzeniami z `DATA`
# 2. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
result = ...