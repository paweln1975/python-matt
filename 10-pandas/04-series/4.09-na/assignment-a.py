"""
Name: Series NA
Difficulty: easy
Lines: 4
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
Terminal: `python -m doctest -v assignment-a.py`

Tests:
>>> import sys; sys.tracebacklimit = 0
>>> assert sys.version_info >= (3, 9), \
'Python 3.9+ required'

>>> assert result is not Ellipsis, \
'Assign result to variable: `result`'
>>> assert type(result) is pd.Series, \
'Variable `result` has invalid type, should be `pd.Series`'

>>> result
0    1.0
1    0.0
2    5.0
3    1.0
4    2.0
5    1.0
dtype: float64

Hints:
`pd.Series.fillna(limit)`

"""

# %% SetUp

import pandas as pd

result: pd.Series

DATA = [1, None, 5, None, 1, 2, 1]

# English
# 1. From input data create `pd.Series`
# 2. Fill only first missing value with zero
# 3. Drop missing values
# 4. Reindex series (without old copy)
# 5. Run doctests - all must succeed

# Polish
# 1. Z danych wejściowych stwórz `pd.Series`
# 2. Wypełnij tylko pierwszą brakującą wartość zerem
# 3. Usuń brakujące wartości
# 4. Zresetuj indeks (bez kopii starego)
# 5. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
result = ...