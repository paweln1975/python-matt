
"""
* Assignment: DataFrame Export SQL
* Complexity: easy
* Lines of code: 4 lines
* Time: 3 min

English:
    1. Read data from `DATA` as `result: pd.DataFrame`
    2. While reading use `header=0` parameter
    3. Select 146 head rows, and last 11 from it
    4. Export data from column `Event` to database `FILE` to table `apollo11`
    5. Run doctests - all must succeed

Polish:
    1. Wczytaj dane z `DATA` jako `result: pd.DataFrame`
    2. Przy wczytywaniu użyj parametru `header=0`
    3. Wybierz pierwszych 146 wierszy, a z nich ostatnie 11
    4. Wyeksportuj dane z kolumny `Event` do bazy danych `FILE` do tabeli `apollo11`
    5. Uruchom doctesty - wszystkie muszą się powieść

Run:
    * PyCharm: right-click in the editor and pick `Run Doctest in myfile`
    * PyCharm: `Control + Shift + R`
    * Terminal: `python -m doctest -v myfile.py`

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from os import remove

    >>> db = sqlite3.connect(FILE)
    >>> data = db.execute('SELECT * FROM apollo11')
    >>> result = list(data)
    >>> db.close()

    >>> assert result is not Ellipsis, \
    'Assign result to variable: `result`'

    >>> list(result)  # doctest: +NORMALIZE_WHITESPACE
    [(135, 'LM lunar landing.'),
     (136, 'LM powered descent  engine cutoff.'),
     (137, 'Decision made to  proceed with EVA prior to first rest period.'),
     (138, 'Preparation for EVA  started.'),
     (139, 'EVA started (hatch  open).'),
     (140, 'CDR completely outside  LM on porch.'),
     (141, 'Modular equipment  stowage assembly deployed (CDR).'),
     (142, 'First clear TV picture  received.'),
     (143, 'CDR at foot of ladder  (starts to report, then pauses to listen).'),
     (144, 'CDR at foot of ladder  and described surface as almost like a powder.'),
     (145, "1st step  taken lunar surface (CDR). That's one small step for a man...one giant leap  for mankind.")]

    >>> remove(FILE)
"""

import sqlite3
import pandas as pd

DATA = 'https://python3.info/_static/apollo11.html'
FILE = r'_temporary.sqlite3'


# Dump DATA to FILE in SQLite3 format
# type: pd.DataFrame
result = ...

