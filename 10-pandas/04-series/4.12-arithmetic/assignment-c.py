"""
Name: Series Arithmetic
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
Terminal: `python -m doctest -v assignment-c.py`

Tests:
>>> import sys; sys.tracebacklimit = 0
>>> assert sys.version_info >= (3, 9), \
'Python 3.9+ required'

>>> assert result is not Ellipsis, \
'Assign result to variable: `result`'
>>> assert type(result) is pd.Series, \
'Variable `result` has invalid type, should be `pd.Series`'

>>> result
0    11.0
1    12.0
2    10.0
3    14.0
4    15.0
dtype: float64

Hints:
`Series.add(fill_value)`

"""

# %% SetUp

import pandas as pd

result: pd.Series

DATA = pd.Series([1.0, 2.0, None, 4.0, 5.0])

# English
# 1. Define variable `result` with result of
#    add 10 to each element of `DATA`
#    if value is not-a-number then treat it as zero
# 2. Use `.add()` method
# 3. Run doctests - all must succeed

# Polish
# 1. Zdefiniuj zmienną `result` z wynikiem
#    dodania 10 to każdego elementu z `DATA`
#    jeżeli wartość nie jest liczbą, to potraktuj ją jak zero
# 2. Użyj metodę `.add()`
# 3. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
result = ...