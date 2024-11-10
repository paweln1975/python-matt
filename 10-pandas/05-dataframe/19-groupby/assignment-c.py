"""
* Assignment: DataFrame Groupby AstronautTop10
* Complexity: medium
* Lines of code: 5 lines
* Time: 13 min

English:
    1. Read data from `DATA`
    2. Create ranking of astronauts with most fligts
    3. Define `result: pd.Dataframe` with top 10
    4. Run doctests - all must succeed

Polish:
    1. Wczytaj dane z `DATA`
    2. Stwórz ranking astronautów z największą liczbą lotów
    3. Zdefiniuj `result: pd.Dataframe` z top 10
    4. Uruchom doctesty - wszystkie muszą się powieść

Run:
    * PyCharm: right-click in the editor and pick `Run Doctest in myfile`
    * PyCharm: `Control + Shift + R`
    * Terminal: `python -m doctest -v myfile.py`

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> pd.set_option('display.width', 500)
    >>> pd.set_option('display.max_columns', 10)
    >>> pd.set_option('display.max_rows', 10)

    >>> assert result is not Ellipsis, \
    'Assign result to variable: `result`'
    >>> assert type(result) is pd.Series, \
    'Variable `result` must be a `pd.Series` type'

    >>> result  # doctest: +NORMALIZE_WHITESPACE
    name
    Chang-Diaz, Franklin R.     7
    Ross, Jerry L.              7
    Malenchenko, Yuri           6
    Krikalev, Sergei            6
    Musgrave, Franklin Story    6
    Young, John W.              6
    Brown, Curtis L., Jr.       6
    Wetherbee, James D.         6
    Foale, C. Michael           6
    Halsell, James D., Jr.      5
    Name: name, dtype: int64
"""

import pandas as pd

DATA = 'https://python3.info/_static/astro-selection.csv'

# type: pd.Series
result = ...

