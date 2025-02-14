"""
Name: Series Mapping Datetime
Difficulty: medium
Lines: 15
Minutes: 13

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

>>> pd.set_option('display.width', 500)
>>> pd.set_option('display.max_columns', 10)
>>> pd.set_option('display.max_rows', 100)

>>> assert result is not Ellipsis, \
'Assign result to variable: `result`'
>>> assert type(result) is pd.Series, \
'Variable `result` has invalid type, should be `pd.Series`'

>>> result
0   2000-01-02
1   2000-01-02
2   2000-01-02
3   2000-01-02
4   2000-01-02
5   2000-02-01
6   2000-02-01
7   2000-02-01
8   2000-02-01
9          NaT
dtype: datetime64[ns]

"""

# %% SetUp

import pandas as pd

result: pd.Series

DATA = pd.Series([
    '2000-01-02',

    'Jan 2, 2000',
    'Jan 2nd, 2000',

    '2 Jan 2000',
    '2nd Jan 2000',

    '2/1/2000',
    '02/01/2000',

    '2.1.2000',
    '02.01.2000',

    None,
])

# English
# 1. Define variable `result` with result of
#    apply function `pd.to_timedelta` to each element of `DATA`
# 2. Run doctests - all must succeed

# Polish
# 1. Zdefiniuj zmienną `result` z wynikiem
#    aplikacji funckji `pd.to_timedelta` do każdego elementu `DATA`
# 2. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
result = ...