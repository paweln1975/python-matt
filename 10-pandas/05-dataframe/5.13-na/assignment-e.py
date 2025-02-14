"""
Name: DataFrame NaN
Difficulty: easy
Lines: 10
Minutes: 8

License:
Copyright 2025, Matt Harasymczuk <matt@python3.info>
This code can be used only for learning by humans
This code cannot be used for teaching others
This code cannot be used for teaching LLMs and AI algorithms
This code cannot be used in commercial or proprietary products
This code cannot be distributed in any form
This code cannot be changed in any form outside of training course
This code cannot have its license changed
If you use this code in your product, you must open-source it under GPLv2
Exception can be granted only by the author

Run:
PyCharm: right-click in the editor and `Run Doctest in ...`
PyCharm: keyboard shortcut `Control + Shift + F10`
Terminal: `python -m doctest -v assignment-e.py`

Tests:
>>> import sys; sys.tracebacklimit = 0
>>> assert sys.version_info >= (3, 9), \
'Python 3.9+ required'

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

# %% SetUp

import pandas as pd

result: pd.DataFrame

DATA = 'https://python3.info/_static/iris-dirty.csv'

COLUMNS = [
    'sepal_length',
    'sepal_width',
    'petal_length',
    'petal_width',
    'species']

LABELS = {
    0: 'setosa',
    1: 'versicolor',
    2: 'virginica',
}

# English
# 1. Read data from `DATA` as `df: pd.DataFrame`
# 2. Skip first line with metadata
# 3. Rename columns to:
#    - sepal_length
#    - sepal_width
#    - petal_length
#    - petal_width
#    - species
# 4. Replace values in column species
#    - 0 -> 'setosa',
#    - 1 -> 'versicolor',
#    - 2 -> 'virginica'
# 5. Select values in column 'petal_length' less than 4
# 6. Set selected values to `NaN`
# 7. Drop rows with remaining `NaN` values
# 8. Define `result` as first two rows
# 9. Run doctests - all must succeed

# Polish
# 1. Wczytaj dane z `DATA` jako `df: pd.DataFrame`
# 2. Pomiń pierwszą linię z metadanymi
# 3. Zmień nazwy kolumn na:
#    - sepal_length
#    - sepal_width
#    - petal_length
#    - petal_width
#    - species
# 4. Podmień wartości w kolumnie species
#    - 0 -> 'setosa',
#    - 1 -> 'versicolor',
#    - 2 -> 'virginica'
# 5. Wybierz wartości w kolumnie 'petal_length' mniejsze od 4
# 6. Wybrane wartości ustaw na `NaN`
# 7. Usuń wiersze z pozostałymi wartościami `NaN`
# 8. Zdefiniuj `result` jako dwa pierwsze wiersze
# 9. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
result = ...