"""
Name: Pandas ReadPython ListList
Difficulty: easy
Lines: 1
Minutes: 2

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
Terminal: `python -m doctest -v assignment-c.py`

Tests:
>>> import sys; sys.tracebacklimit = 0
>>> assert sys.version_info >= (3, 9), \
'Python 3.9+ required'

>>> assert result is not Ellipsis, \
'Assign result to variable: `result`'
>>> assert type(result) is pd.DataFrame, \
'Variable `result` has invalid type, should be `pd.DataFrame`'

>>> result  # doctest: +NORMALIZE_WHITESPACE
  firstname  lastname       role
0      Mark    Watney   botanist
1   Melissa     Lewis  commander
2      Rick  Martinez      pilot

Hints:
`pd.DataFrame()`

"""

# %% SetUp

import pandas as pd

result: pd.DataFrame

DATA = [
    ('Mark', 'Watney', 'botanist'),
    ('Melissa', 'Lewis', 'commander'),
    ('Rick', 'Martinez', 'pilot'),
]

COLUMNS = ['firstname', 'lastname', 'role']

# English
# 1. Define `result: pd.DataFrame` with `DATA`
# 2. Run doctests - all must succeed

# Polish
# 1. Zdefiniuj `result: pd.DataFrame` z `DATA`
# 2. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
result = ...