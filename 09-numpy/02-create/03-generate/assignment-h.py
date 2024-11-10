"""
* Assignment: Numpy Generate EmptyLike
* Complexity: easy
* Lines of code: 1 lines
* Time: 2 min

English:
    1. Define `result: np.ndarray` from `DATA`:
       a. dtype: int64
       b. values: leave default
       c. shape: 3 rows, 3 columns
       d. use: `np.empty_like()`
    2. Run doctests - all must succeed

Polish:
    1. Zdefiniuj `result: np.ndarray` from `DATA`:
       a. dtype: int64
       b. wartości: pozostaw domyślne
       c. shape: 3 wiersze, 3 kolumny
       d. użyj: `np.empty_like()`
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

    >>> assert result.dtype == DATA.dtype
    >>> assert result.itemsize == DATA.itemsize
    >>> assert result.shape == DATA.shape
    >>> assert result.strides == DATA.strides
"""

import numpy as np


DATA = np.array([[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]])

# dtype: int64
# values: leave default
# shape: 3 rows, 3 columns
# use: `np.empty_like()`
# type: np.ndarray
result = ...


