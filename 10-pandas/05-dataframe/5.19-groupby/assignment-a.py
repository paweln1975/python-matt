"""
Name: DataFrame Groupby Phones
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
>>> assert type(result) is pd.Series, \
'Variable `result` must be a `pd.Series` type'

>>> result  # doctest: +NORMALIZE_WHITESPACE
year  month
1999  10       16309.0
      11       16780.0
      12       14861.0
2000  1        18705.0
      2        11019.0
      3        14647.0
Name: duration, dtype: float64

"""

# %% SetUp

import pandas as pd

result: pd.DataFrame

DATA = 'https://python3.info/_static/phones-pl.csv'

# English
# 1. Read data from `DATA` as `df: pd.DataFrame`
# 2. Give information about total number of all phone calls for each calendar month
# 3. Run doctests - all must succeed

# Polish
# 1. Wczytaj dane z `DATA` jako `df: pd.DataFrame`
# 2. Podaj informacje o łącznej liczbie wszystkich połączeń telefonicznych dla każdego miesiąca kalendarzowego
# 3. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
result = ...