"""
Name: DataFrame Select
Difficulty: easy
Lines: 5
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

>>> pd.set_option('display.width', 500)
>>> pd.set_option('display.max_columns', 10)
>>> pd.set_option('display.max_rows', 10)

>>> assert result is not Ellipsis, \
'Assign result to variable: `result`'
>>> assert type(result) is pd.DataFrame, \
'Variable `result` must be a `pd.DataFrame` type'

>>> result  # doctest: +NORMALIZE_WHITESPACE
   sepal_length  sepal_width  petal_length  petal_width     species
1           5.9          3.0           5.1          1.8   virginica
2           6.0          3.4           4.5          1.6  versicolor
3           7.3          2.9           6.3          1.8   virginica
4           5.6          2.5           3.9          1.1  versicolor
6           5.5          2.6           4.4          1.2  versicolor

"""

# %% SetUp

import pandas as pd

result: pd.DataFrame

DATA = 'https://python3.info/_static/iris-clean.csv'

# English

# Polish
# 1. Wczytaj dane z `DATA` jako `df: pd.DataFrame`
# 2. Wybierz wiersze, gdzie wartość 'petal_length' jest powyżej 2.0
# 3. Wyświetl 5 pierwszych wierszy
# 4. Użyj `.query()`
# 5. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
result = ...