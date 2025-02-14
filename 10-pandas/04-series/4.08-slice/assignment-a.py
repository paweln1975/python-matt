"""
Name: Series Slice Datetime
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

>>> pd.set_option('display.width', 500)
>>> pd.set_option('display.max_columns', 10)
>>> pd.set_option('display.max_rows', 10)

>>> assert result is not Ellipsis, \
'Assign result to variable: `result`'
>>> assert type(result) is pd.Series, \
'Variable `result` has invalid type, should be `pd.Series`'

>>> result  # doctest: +NORMALIZE_WHITESPACE
2000-02-14   -0.509652
2000-02-15   -0.438074
2000-02-16   -1.252795
2000-02-17    0.777490
2000-02-18   -1.613898
                ...
2000-02-25    0.428332
2000-02-26    0.066517
2000-02-27    0.302472
2000-02-28   -0.634322
2000-02-29   -0.362741
Freq: D, Length: 16, dtype: float64

Hints:
`pd.Series.loc[]`

"""

# %% SetUp

import pandas as pd
import numpy as np

result: pd.Series

np.random.seed(0)

s = pd.Series(
    data=np.random.randn(100),
    index=pd.date_range('2000-01-01', freq='D', periods=100))

# English
# 1. Given is `s: pd.Series` with dates since 2000
# 2. Define `result: pd.Series` with values for dates between 2000-02-14 and end of February 2000
# 3. Run doctests - all must succeed

# Polish
# 1. Dany jest `s: pd.Series` z datami od 2000 roku
# 2. Zdefiniuj `result: pd.Series` z wartościami pomiędzy datami od 2000-02-14 do końca lutego 2000
# 3. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
result = ...