
"""
* Assignment: DataFrame Create
* Complexity: easy
* Lines of code: 5 lines
* Time: 3 min

English:
    1. Define `result: pd.DataFrame`:
        a. Name columns: `role`, `firstname`, `lastname`
    3. Run doctests - all must succeed

Polish:
    1. Zdefiniuj `result: pd.DataFrame`
        a. Nazwij kolumny: `role`, `firstname`, `lastname`
    3. Uruchom doctesty - wszystkie muszą się powieść

Run:
    * PyCharm: right-click in the editor and pick `Run Doctest in myfile`
    * PyCharm: `Control + Shift + R`
    * Terminal: `python -m doctest -v myfile.py`

Hints:
    * Use selection with `alt` key in your IDE

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> pd.set_option('display.width', 500)
    >>> pd.set_option('display.max_columns', 10)
    >>> pd.set_option('display.max_rows', 10)

    >>> assert result is not Ellipsis, \
    'Assign result to variable: `result`'
    >>> assert type(result) is pd.DataFrame, \
    'Variable `result` must be a `pd.DataFrame` type'

    >>> result  # doctest: +NORMALIZE_WHITESPACE
      firstname   lastname       role
    0      Mark     Watney   botanist
    1   Melissa      Lewis  commander
    2      Rick   Martinez      pilot
    3      Alex      Vogel    chemist
    4      Beth  Johanssen   engineer
    5     Chris       Back      medic
"""

import pandas as pd


# firstname   lastname       role
#      Mark     Watney   botanist
#   Melissa      Lewis  commander
#      Rick   Martinez      pilot
#      Alex      Vogel    chemist
#      Beth  Johanssen   engineer
#     Chris       Back      medic

# type: pd.DataFrame
result = ...


