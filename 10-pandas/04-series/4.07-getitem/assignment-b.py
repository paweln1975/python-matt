"""
Name: Pandas Series Getitem
Difficulty: easy
Lines: 5
Minutes: 8

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
>>> import numpy

>>> assert result is not Ellipsis, \
'Assign result to variable: `result`'
>>> assert type(result) is numpy.float64, \
'Variable `result` has invalid type, should be `numpy.float64`'

>>> result
np.float64(1.764052345967664)

Hints:
`Series.iloc[]`

"""

# %% SetUp

import pandas as pd
import numpy as np

result: np.float64

np.random.seed(0)

DATA = pd.Series(
    data=np.random.randn(10),
    index=pd.date_range('2000-01-01', freq='D', periods=10),
)

# English
# 1. Define variable `result_b` with first value in `DATA`
# 2. Use `.iloc[]` method
# 3. Run doctests - all must succeed

# Polish
# 1. Zdefiniuj zmienną `result_b` z pierwszą wartością w `DATA`
# 2. Użyj metody `.iloc[]`
# 3. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
result = ...