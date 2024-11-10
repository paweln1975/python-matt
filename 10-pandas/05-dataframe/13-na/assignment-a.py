"""
* Assignment: DataFrame NaN
* Complexity: easy
* Lines of code: 10 lines
* Time: 8 min

English:
    1. Read data from `DATA` as `df: pd.DataFrame`
    2. Skip first line with metadata
    3. Rename columns to:
        a. sepal_length
        b. sepal_width
        c. petal_length
        d. petal_width
        e. species
    4. Replace values in column species
        a. 0 -> 'setosa',
        b. 1 -> 'versicolor',
        c. 2 -> 'virginica'
    5. Select values in column 'petal_length' less than 4
    6. Set selected values to `NaN`
    7. Interpolate linearly all `NaN` values
    8. Drop rows with remaining `NaN` values
    9. Define `result` as first two rows
    10. Run doctests - all must succeed

Polish:
    1. Wczytaj dane z `DATA` jako `df: pd.DataFrame`
    2. Pomiń pierwszą linię z metadanymi
    3. Zmień nazwy kolumn na:
        a. sepal_length
        b. sepal_width
        c. petal_length
        d. petal_width
        e. species
    4. Podmień wartości w kolumnie species
        a. 0 -> 'setosa',
        b. 1 -> 'versicolor',
        c. 2 -> 'virginica'
    5. Wybierz wartości w kolumnie 'petal_length' mniejsze od 4
    6. Wybrane wartości ustaw na `NaN`
    7. Interpoluj liniowo wszystkie wartości `NaN`
    8. Usuń wiersze z pozostałymi wartościami `NaN`
    9. Zdefiniuj `result` jako dwa pierwsze wiersze
    10. Uruchom doctesty - wszystkie muszą się powieść

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
       sepal_length  sepal_width  petal_length  petal_width     species
    1           5.9          3.0           5.1          1.8   virginica
    2           6.0          3.4           4.5          1.6  versicolor
"""

import pandas as pd
import numpy as np


DATA = 'https://python3.info/_static/iris-dirty.csv'
COLUMNS = [
    'sepal_length',
    'sepal_width',
    'petal_length',
    'petal_width',
    'species']

# type: pd.DataFrame
result = ...


