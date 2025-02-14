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
Terminal: `python -m doctest -v assignment-a.py`

Tests:
>>> import sys; sys.tracebacklimit = 0
>>> import pandas

>>> assert result is not Ellipsis, \
'Assign result to variable: `result`'
>>> assert type(result) is pandas.core.series.Series, \
'Variable `result` has invalid type, should be `pandas.core.series.Series`'

>>> result
2000-01-01    1.764052
Freq: D, dtype: float64

Hints:
`pd.Series.head(n)`

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
# 1. Define variable `result` with first element from `DATA`
# 2. Run doctests - all must succeed

# Polish
# 1. Zdefiniuj zmienną `result` z pirewszym elementem z `DATA`
# 2. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
result = ...