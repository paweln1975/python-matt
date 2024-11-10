"""
* Assignment: Slicing Slice Str
* Complexity: easy
* Lines of code: 2 lines
* Time: 5 min

English:
    1. Find middle element `s: pd.Series`
    2. Slice from series 5 elements:
        a. two elements before middle
        b. one middle element
        c. two elements after middle
    3. Run doctests - all must succeed

Polish:
    1. Znajdź środkowy element `s: pd.Series`
    2. Wytnij z serii 5 elementów:
        a. dwa elementy przed środkowym
        b. jeden środkowy element
        c. dwa elementy za środkowym
    3. Uruchom doctesty - wszystkie muszą się powieść

Run:
    * PyCharm: right-click in the editor and pick `Run Doctest in myfile`
    * PyCharm: `Control + Shift + R`
    * Terminal: `python -m doctest -v myfile.py`

Hints:
    * `pd.Series.iloc[]`

Tests:
    >>> import sys; sys.tracebacklimit = 0

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
"""

import pandas as pd
import numpy as np
np.random.seed(0)


s = pd.Series(
    data=np.random.randint(10, 100, size=26),
    index=['a', 'b', 'c', 'd', 'e', 'f', 'g',
           'h', 'i', 'j', 'k', 'l', 'm', 'n',
           'o', 'p', 'q', 'r', 's', 't', 'u',
           'v', 'w', 'x', 'y', 'z']
)


# type: pd.Series
result = ...

