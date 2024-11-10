"""
* Assignment: DataFrame Groupby FemaleTop
* Complexity: medium
* Lines of code: 5 lines
* Time: 8 min

English:
    1. Read data from `DATA` as `df: pd.DataFrame`
    2. Which nationality has the most flight time of a female in space?
    3. Sort the result in descending order
    4. Run doctests - all must succeed

Polish:
    1. Wczytaj dane z `DATA` jako `df: pd.DataFrame`
    2. Który kraj ma największy nalot kobiet w kosmosie?
    3. Posortuj wynik malejąco
    4. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> pd.set_option('display.width', 500)
    >>> pd.set_option('display.max_columns', 10)
    >>> pd.set_option('display.max_rows', 10)

    >>> assert result is not Ellipsis, \
    'Assign result to variable: `result`'
    >>> assert type(result) is pd.Series, \
    'Variable `result` must be a `pd.DataFrame` type'

    >>> result  # doctest: +NORMALIZE_WHITESPACE
    Nationality
    American        124
    Russian           6
    Canadian          3
    Japanese          3
    Chinese           2
    French            2
    British           1
    Italian           1
    South Korean      1
    Name: Flights, dtype: int64
"""

import pandas as pd

DATA = 'https://python3.info/_static/astro-gender.csv'

# type: pd.Series
result = ...

