"""
* Assignment: Series Arithmetic
* Complexity: easy
* Lines of code: 5 lines
* Time: 3 min

English:
    1. Define `result: pd.Series` with result of operations:
        a. Multiply `s` by 10
        b. Add to `s` values from `s` (from before multiplication)
    2. Run doctests - all must succeed

Polish:
    1. Zdefiniuj `result: pd.Series` z wynikiem operacji:
        a. Pomnóż `s` przez 10
        b. Dodaj do `s` wartości z `s` (z przed mnożenia)
    2. Uruchom doctesty - wszystkie muszą się powieść

Run:
    * PyCharm: right-click in the editor and pick `Run Doctest in myfile`
    * PyCharm: `Control + Shift + R`
    * Terminal: `python -m doctest -v myfile.py`

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert result is not Ellipsis, \
    'Assign result to variable: `result`'
    >>> assert type(result) is pd.Series, \
    'Variable `result` has invalid type, should be `pd.Series`'

    >>> result
    a    55
    b     0
    c    33
    d    33
    e    77
    dtype: int64
"""

import pandas as pd
import numpy as np
np.random.seed(0)

s = pd.Series(
    data=np.random.randint(0, 10, size=5),
    index=['a', 'b', 'c', 'd', 'e'],
)

# Multiply `s` by 10
# Add to `s` values from `s` (from before multiplication)
# type: pd.Series
result = ...


