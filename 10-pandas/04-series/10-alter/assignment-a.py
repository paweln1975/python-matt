"""
* Assignment: Series Alter DropOne
* Complexity: easy
* Lines of code: 1 lines
* Time: 2 min

English:
    1. Define `result: pd.Series` with result of:
        a. From `DATA` drop value at index 3
    2. Run doctests - all must succeed

Polish:
    1. Zdefiniuj `result: pd.Series` z wynikiem:
        a. Z `DATA` usuń wartość na indeksie 3
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
    0       Mark
    1    Melissa
    2       Rick
    4       Beth
    5      Chris
    dtype: object
"""

import pandas as pd


DATA = pd.Series([
    'Mark',
    'Melissa',
    'Rick',
    'Alex',
    'Beth',
    'Chris',
])

# From `DATA` drop value at index 3
# type: pd.Series
result = ...


