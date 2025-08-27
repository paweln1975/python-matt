"""
Name: Pandas Read JSON
Difficulty: easy
Lines: 1
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
>>> assert type(result) is pd.DataFrame, \
'Variable `result` must be a `pd.DataFrame` type'

>>> result.loc[[0,10,20]]
    sepal_length  sepal_width  petal_length  petal_width     species
0            5.1          3.5           1.4          0.2      setosa
10           7.0          3.2           4.7          1.4  versicolor
20           6.3          3.3           6.0          2.5   virginica

"""

# %% SetUp

import pandas as pd

result: pd.DataFrame

DATA = 'https://python3.info/_static/iris.json'

# English
# 1. Read data from `DATA` as `result: pd.DataFrame`
# 2. Run doctests - all must succeed

# Polish
# 1. Wczytaj dane z DATA jako `result: pd.DataFrame`
# 2. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
result = pd.read_json(DATA)
print(result)
print(type(result))
