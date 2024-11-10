
"""
* Assignment: DataFrame Groupby Astro EVA
* Complexity: medium
* Lines of code: 13 lines
* Time: 21 min

English:
    1. Read data from `DATA` as `df: pd.DataFrame`
    2. Create top 10 ranking of astronauts with the most time spent on EVA (ExtraVehicular Activity)
    3. Run doctests - all must succeed

Polish:
    1. Wczytaj dane z `DATA` jako `df: pd.DataFrame`
    2. Stwórz ranking top 10 astronautów z największym czasem EVA (Spacerów kosmicznych)
    3. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * Note, that file delimiter is semicolon ";" (not comma)
    * Parse CSV and replace newlines inside fields with `","`
    * Split names into separate columns for each spacewalker (first, second, third)
    * Split names into separate rows for each spacewalker (use ffill)
    * Split times into separate columns (hours, minutes)
    * pd.Series.str.split() with expand=True
    * pd.DataFrame.melt()
    * pd.DataFrame.set_index()
    * pd.Series.astype()

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
    >>> assert type(result) is pd.DataFrame, \
    'Variable `result` must be a `pd.DataFrame` type'

    >>> result  # doctest: +NORMALIZE_WHITESPACE
                                 Duration
    Astronaut
    Anatoliy Solovyov     3 days 06:48:00
    Michael Lopez-Alegria 2 days 19:40:00
    Peggy Whitson         2 days 12:21:00
    Fyodor Yurchikhin     2 days 11:29:00
    Jerry Ross            2 days 10:38:00
    John Grunsfeld        2 days 10:30:00
    Richard Mastracchio   2 days 05:04:00
    Sunita Williams       2 days 02:40:00
    Stephen Smith         2 days 01:48:00
    Edward Fincke         2 days 00:36:00
"""

import pandas as pd


DATA = 'https://python3.info/_static/astro-eva.csv'

# type: pd.DataFrame
result = ...


