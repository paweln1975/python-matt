"""
Name: DataFrame NaN
Difficulty: easy
Lines: 10
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
Terminal: `python -m doctest -v assignment-d.py`

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

>>> result
  firstname   lastname       role agency
0      Mark     Watney   botanist   NASA
1   Melissa      Lewis  commander   NASA
2      Rick   Martinez      pilot   NASA
3      Alex      Vogel    chemist    ESA
4      Beth  Johanssen   engineer   NASA
5     Chris       Back      medic   NASA

"""

# %% SetUp

import pandas as pd

result: pd.DataFrame

DATA = pd.DataFrame([
    {'firstname': 'Mark', 'lastname': 'Watney', 'role': 'botanist', 'agency': 'NASA'},
    {'firstname': 'Melissa', 'lastname': 'Lewis', 'role': 'commander', 'agency': pd.NA},
    {'firstname': 'Rick', 'lastname': 'Martinez', 'role': 'pilot', 'agency': pd.NA},
    {'firstname': 'Alex', 'lastname': 'Vogel', 'role': 'chemist', 'agency': 'ESA'},
    {'firstname': 'Beth', 'lastname': 'Johanssen', 'role': 'engineer', 'agency': 'NASA'},
    {'firstname': 'Chris', 'lastname': 'Back', 'role': 'medic', 'agency': pd.NA},
])

# English
# 1. Define variable `result` with
#    dataframe `DATA` with values in column `mission` forward filled
# 2. Run doctests - all must succeed

# Polish
# 1. Zdefiniuj zmienną `result` z
#    dataframe `DATA` z wartościami w kolumnie `mission` wypełnionymi w przód
# 2. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
result = ...