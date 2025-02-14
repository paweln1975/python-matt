"""
Name: DataFrame Groupby FemaleTop
Difficulty: medium
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
>>> assert sys.version_info >= (3, 9), \
'Python 3.9+ required'

>>> pd.set_option('display.width', 500)
>>> pd.set_option('display.max_columns', 10)
>>> pd.set_option('display.max_rows', 10)

>>> assert result is not Ellipsis, \
'Assign result to variable: `result`'
>>> assert type(result) is pd.Series, \
'Variable `result` must be a `pd.DataFrame` type'

>>> result  # doctest: +NORMALIZE_WHITESPACE
Nationality
American        124
Russian           6
Canadian          3
Japanese          3
Chinese           2
French            2
British           1
Italian           1
South Korean      1
Name: Flights, dtype: int64

"""

# %% SetUp

import pandas as pd

result: pd.Series

DATA = 'https://python3.info/_static/astro-gender.csv'

# English
# 1. Read data from `DATA` as `df: pd.DataFrame`
# 2. Which nationality has the most flight time of a female in space?
# 3. Sort the result in descending order
# 4. Run doctests - all must succeed

# Polish
# 1. Wczytaj dane z `DATA` jako `df: pd.DataFrame`
# 2. Który kraj ma największy nalot kobiet w kosmosie?
# 3. Posortuj wynik malejąco
# 4. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
result = ...