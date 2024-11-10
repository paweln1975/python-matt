"""
* Assignment: Numpy Generate Identity
* Complexity: easy
* Lines of code: 1 lines
* Time: 2 min

English:
    1. Define `result: np.ndarray`:
       a. dtype: int64
       b. values: all zeros with ones across
       c. shape: 3 rows, 3 columns
       d. use: `np.identity()`
    2. Run doctests - all must succeed

Polish:
    1. Zdefiniuj `result: np.ndarray`:
       a. dtype: int64
       b. wartości: same zera z jedynkami na skos
       c. shape: 3 wiersze, 3 kolumny
       d. użyj: `np.identity()`
    2. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert result is not Ellipsis, \
    'Assign result to variable: `result`'
    >>> assert type(result) is np.ndarray, \
    'Variable `result` has invalid type, expected: np.ndarray'

    >>> assert result.dtype == np.dtype('int64')
    >>> assert result.itemsize == 8
    >>> assert result.shape == (3, 3)
    >>> assert result.strides == (24, 8)

    >>> result
    array([[1, 0, 0],
           [0, 1, 0],
           [0, 0, 1]])
"""

import numpy as np


# dtype: int64
# values: all zeros with ones across
# shape: 3 rows, 3 columns
# use: `np.identity()`
# type: np.ndarray
result = ...


