"""
Name: Pandas Series Attributes
Difficulty: easy
Lines: 4
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
>>> import pandas
>>> import numpy

>>> assert result is not Ellipsis, \
'Assign result to variable: `result`'
>>> assert type(result) is numpy.dtypes.ObjectDType, \
'Variable `result` has invalid type, should be `numpy.dtypes.ObjectDType`'

>>> result
dtype('O')

"""

# %% SetUp

import pandas as pd
import numpy as np

result: np.dtype

DATA = pd.Series(['a', 'b', 'c'])

# English
# 1. Define variable `result` with a data type of `DATA`
# 2. Run doctests - all must succeed

# Polish
# 1. Zdefiniuj zmienną `result` z typem danych `DATA`
# 2. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
result = ...