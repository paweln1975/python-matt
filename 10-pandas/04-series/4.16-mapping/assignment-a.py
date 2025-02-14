"""
Name: Series Mapping Timedelta
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
Terminal: `python -m doctest -v assignment-a.py`

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
0    0 days 00:10:00
1    0 days 00:10:00
2    0 days 00:10:00
3    0 days 00:10:20
4    0 days 01:20:30
5    1 days 02:30:40
6    0 days 01:20:00
7    0 days 01:20:00
8    0 days 01:00:00
9    0 days 02:00:00
10   3 days 01:00:00
11               NaT
dtype: timedelta64[ns]

"""

# %% SetUp

import pandas as pd

result: pd.Series

DATA = pd.Series([
    '10 m',
    '10 min',
    '10 minutes',

    '10m 20s',
    '1h 20m 30s',
    '1d 2h 30m 40s',

    '1 hour 20 minutes',
    '1 hours 20 minutes',

    '01:00:00',
    '02:00:00',
    '3d 01:00:00',

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