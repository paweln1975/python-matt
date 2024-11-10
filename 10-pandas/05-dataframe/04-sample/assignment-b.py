"""
* Assignment: DataFrame Sample
* Complexity: easy
* Lines of code: 5 lines
* Time: 5 min

English:
    1. Read data from `DATA` as `df: pd.DataFrame`
    2. In data column "Order":
        a. determines the order of the astronaut/cosmonaut in space
        b. Sometimes several people flew on the same ship and their numbers should be the same, and in the data there is `NaN`.
        c. Fill in the missing indexes using `df.ffill()`
    3. Set all rows in random order
    4. Reset index without leaving a backup copy of the old one
    5. Run doctests - all must succeed

Polish:
    1. Wczytaj dane z `DATA` jako `df: pd.DataFrame`
    2. W danych kolumna "Order":
        a. określa kolejność astronauty/kosmonauty w kosmosie
        b. Czasami kilka osób leciało tym samym statkiem i ich numery powinny być takie same, a w danych jest `NaN`.
        c. Wypełnij brakujące indeksy stosując `df.ffill()`
    3. Ustaw wszystkie wiersze w losowej kolejności
    4. Zresetuj index nie pozostawiając kopii zapasowej starego
    5. Uruchom doctesty - wszystkie muszą się powieść

Run:
    * PyCharm: right-click in the editor and pick `Run Doctest in myfile`
    * PyCharm: `Control + Shift + R`
    * Terminal: `python -m doctest -v myfile.py`

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert result is not Ellipsis, \
    'Assign result to variable: `result`'
    >>> assert type(result) is pd.DataFrame, \
    'Variable `result` must be a `pd.DataFrame` type'

    >>> pd.set_option('display.width', 500)
    >>> pd.set_option('display.max_columns', 10)
    >>> pd.set_option('display.max_rows', 10)

    >>> result  # doctest: +NORMALIZE_WHITESPACE
         Order            Astronaut     Type              Date   Spacecraft
    0      244     Donald McMonagle  Orbital     28 April 1991       STS-39
    1       93        Georgi Ivanov  Orbital     10 April 1979     Soyuz 33
    2      387         Rick Husband  Orbital       27 May 1999       STS-96
    3      185       William Pailes  Orbital    3 October 1985         51-J
    4      390        Jeffrey Ashby  Orbital      23 July 1999       STS-93
    ..     ...                  ...      ...               ...          ...
    578    277       Franco Malerba  Orbital      31 July 1992       STS-46
    579     10         Leroy Cooper  Orbital       15 May 1963      Faith 7
    580    359       Carlos Noriega  Orbital       15 May 1997       STS-84
    581    192    Rodolfo Neri Vela  Orbital  27 November 1985         61-B
    582    559  David Saint-Jacques  Orbital   3 December 2018  Soyuz MS-11
    <BLANKLINE>
    [583 rows x 5 columns]
"""

import pandas as pd
import numpy as np
np.random.seed(0)


DATA = 'https://python3.info/_static/astro-order.csv'

# type: pd.DataFrame
result = ...


