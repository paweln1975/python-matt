"""
Name: DataFrame Statistics
Difficulty: medium
Lines: 1
Minutes: 2

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

>>> pd.set_option('display.width', 500)
>>> pd.set_option('display.max_columns', 10)
>>> pd.set_option('display.max_rows', 10)

>>> assert result is not Ellipsis, \
'Assign result to variable: `result`'
>>> assert type(result) is pd.DataFrame, \
'Variable `result` must be a `pd.DataFrame` type'

>>> result  # doctest: +NORMALIZE_WHITESPACE
            mileage  consumption
count      50.00000    50.000000
mean   110421.02000     9.320000
std     53170.24328     6.244802
min      7877.00000     0.000000
25%     71239.75000     4.000000
50%    115186.00000     9.000000
75%    154889.00000    14.750000
max    199827.00000    20.000000

Hints:
`DataFrame.describe()`

"""

# %% SetUp

import pandas as pd
import numpy as np

result: pd.DataFrame

np.random.seed(0)

df = pd.DataFrame({
    'mileage': np.random.randint(0, 200_000, size=50),
    'consumption': np.random.randint(0, 21, size=50),
})

# English
# 1. Save basic descriptive statistics to `result: pd.DataFrame`
# 2. Run doctests - all must succeed

# Polish
# 1. Zapisz podstawowe statystyki opisowe do `result: pd.DataFrame`
# 2. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
result = ...