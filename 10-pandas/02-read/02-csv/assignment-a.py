"""
* Assignment: Pandas Read CSV Dates
* Complexity: easy
* Lines of code: 1 lines
* Time: 3 min

English:
    1. Read data from `DATA` to `result: pd.DataFrame`
    2. Parse dates in "birthdate" column
    3. Run doctests - all must succeed

Polish:
    1. Wczytaj dane z `DATA` do `result: pd.DataFrame`
    2. Sparsuj daty w kolumnie "birthdate"
    3. Uruchom doctesty - wszystkie muszą się powieść

Run:
    * PyCharm: right-click in the editor and pick `Run Doctest in myfile`
    * PyCharm: `Control + Shift + R`
    * Terminal: `python -m doctest -v myfile.py`

Hints:
    * `parse_dates`

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert result is not Ellipsis, \
    'Assign result to variable: `result`'
    >>> assert type(result) is pd.DataFrame, \
    'Variable `result` must be a `pd.DataFrame` type'

    >>> result[['firstname', 'lastname', 'birthdate']]
      firstname   lastname  birthdate
    0      Mark     Watney 1994-10-12
    1   Melissa      Lewis 1995-07-15
    2      Rick   Martinez 1996-01-21
    3      Alex      Vogel 1994-11-15
    4      Beth  Johanssen 2006-05-09
    5     Chris       Beck 1999-08-02
"""

import pandas as pd


DATA = 'https://python3.info/_static/martian-en.csv'


# Read DATA and parse dates in "birthdate" column
# type: pd.DataFrame
result = ...


