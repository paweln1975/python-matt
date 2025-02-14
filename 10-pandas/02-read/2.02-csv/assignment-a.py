"""
Name: Pandas ReadCSV Simple
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

>>> result
  firstname   lastname                email
0      Mark     Watney     mwatney@nasa.gov
1   Melissa      Lewis      mlewis@nasa.gov
2      Rick   Martinez   rmartinez@nasa.gov
3      Alex      Vogel       avogel@esa.int
4      Beth  Johanssen  bjohanssen@nasa.gov
5     Chris       Beck       cbeck@nasa.gov

Hints:
`DataFrame.read_csv()`

"""

# %% SetUp

import pandas as pd

result: pd.DataFrame

DATA = 'https://python3.info/_static/readcsv-a.csv'

# English
# 1. Read data from `DATA` to `result: pd.DataFrame`
# 2. Run doctests - all must succeed

# Polish
# 1. Wczytaj dane z `DATA` do `result: pd.DataFrame`
# 2. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
result = ...