"""
Name: Pandas ReadCSV Dates
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
Terminal: `python -m doctest -v assignment-b.py`

Tests:
>>> import sys; sys.tracebacklimit = 0
>>> assert sys.version_info >= (3, 9), \
'Python 3.9+ required'

>>> assert result is not Ellipsis, \
'Assign result to variable: `result`'
>>> assert type(result) is pd.DataFrame, \
'Variable `result` must be a `pd.DataFrame` type'

>>> result[['firstname', 'lastname', 'birthdate']]
  firstname   lastname  birthdate
0      Mark     Watney 1994-10-12
1   Melissa      Lewis 1995-07-15
2      Rick   Martinez 1996-01-21
3      Alex      Vogel 1994-11-15
4      Beth  Johanssen 2006-05-09
5     Chris       Beck 1999-08-02

Hints:
`DataFrame.read_csv(parse_dates)`

"""

# %% SetUp

import pandas as pd

result: pd.DataFrame

DATA = 'https://python3.info/_static/readcsv-b.csv'

# English
# 1. Read data from `DATA` to `result: pd.DataFrame`
# 2. Parse dates in "birthdate" column
# 3. Run doctests - all must succeed

# Polish
# 1. Wczytaj dane z `DATA` do `result: pd.DataFrame`
# 2. Sparsuj daty w kolumnie "birthdate"
# 3. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
result = pd.read_csv(DATA, parse_dates=['birthdate'])
