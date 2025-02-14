"""
Name: Slicing Slice Str
Difficulty: easy
Lines: 2
Minutes: 5

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
>>> assert type(result) is pd.Series, \
'Variable `result` has invalid type, should be `pd.Series`'

>>> result
l    98
m    98
n    22
o    68
p    75
dtype: int64

Hints:
`pd.Series.iloc[]`

"""

# %% SetUp

import pandas as pd
import numpy as np

result: pd.Series

np.random.seed(0)

s = pd.Series(
    data=np.random.randint(10, 100, size=26),
    index=['a', 'b', 'c', 'd', 'e', 'f', 'g',
           'h', 'i', 'j', 'k', 'l', 'm', 'n',
           'o', 'p', 'q', 'r', 's', 't', 'u',
           'v', 'w', 'x', 'y', 'z']
)

# English
# 1. Find middle element `s: pd.Series`
# 2. Slice from series 5 elements:
#    - two elements before middle
#    - one middle element
#    - two elements after middle
# 3. Run doctests - all must succeed

# Polish
# 1. Znajdź środkowy element `s: pd.Series`
# 2. Wytnij z serii 5 elementów:
#    - dwa elementy przed środkowym
#    - jeden środkowy element
#    - dwa elementy za środkowym
# 3. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
result = ...