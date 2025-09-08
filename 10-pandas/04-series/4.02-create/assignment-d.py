"""
Name: Series Create Dates
Difficulty: easy
Lines: 2
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
>>> assert type(result) is pd.Series, \
'Variable `result` has invalid type, should be `pd.Series`'

>>> result  # doctest: +NORMALIZE_WHITESPACE
0      1961-04-12
1      1961-04-13
2      1961-04-14
3      1961-04-15
4      1961-04-16
          ...
3018   1969-07-17
3019   1969-07-18
3020   1969-07-19
3021   1969-07-20
3022   1969-07-21
Length: 3023, dtype: datetime64[ns]

"""

# %% SetUp

import pandas as pd

result: pd.Series

# English
# 1. Gagarin flown to space on 1961-04-12
# 2. Armstrong set foot on the Moon on 1969-07-21
# 3. Create `result: pd.Series` with days between Gagarin's launch and Armstrong's first step
# 4. How many days passed?
# 5. Run doctests - all must succeed

# Polish
# 1. Gagarin poleciał w kosmos w 1961-04-12
# 2. Armstrong postawił stopę na Księżycu w 1969-07-21
# 3. Stwórz `result: pd.Series` z dniami pomiędzy startem Gagarina a pierwszym krokiem Armstronga
# 4. Jak wiele dni upłynęło?
# 5. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
result = pd.Series(pd.date_range(start='1961-04-12', end='1969-07-21'))
print(result)