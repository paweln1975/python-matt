"""
Name: DataFrame Mapping Month
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
Terminal: `python -m doctest -v assignment-c.py`

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
      id   period          datetime   network  item           type  duration  year     month
0      0  1999-11  1999-10-15 06:58  T-Mobile  data           data      34.5  1999  November
1      1  1999-11  1999-10-15 06:58    Orange  call         mobile      13.0  1999  November
2      2  1999-11  1999-10-15 14:46      Play  call         mobile      23.0  1999  November
3      3  1999-11  1999-10-15 14:48      Plus  call         mobile       4.0  1999  November
4      4  1999-11  1999-10-15 17:27  T-Mobile  call         mobile       4.0  1999  November
..   ...      ...               ...       ...   ...            ...       ...   ...       ...
825  825  2000-03  2000-03-13 00:38      AT&T   sms  international       1.0  2000     March
826  826  2000-03  2000-03-13 00:39    Orange   sms         mobile       1.0  2000     March
827  827  2000-03  2000-03-13 06:58    Orange  data           data      34.5  2000     March
828  828  2000-03  2000-03-14 00:13      AT&T   sms  international       1.0  2000     March
829  829  2000-03  2000-03-14 00:16      AT&T   sms  international       1.0  2000     March
<BLANKLINE>
[830 rows x 9 columns]

Hints:
`Series.str.split(expand=True)`
`df[ ['A', 'B'] ] = ...`

"""

# %% SetUp

import pandas as pd

result: pd.DataFrame

DATA = 'https://python3.info/_static/phones-pl.csv'

MONTHS_EN = ['January', 'February', 'March', 'April',
             'May', 'June', 'July', 'August', 'September',
             'October', 'November', 'December']

MONTHS = dict(enumerate(MONTHS_EN, start=1))

# English
# 1. Read data from `DATA` as `df: pd.DataFrame`
# 2. Add column `year` and `month` by parsing `period` column
# 3. Month name must be a string month name, not a number (i.e.: 'January', 'May')
# 4. Example: if `period` column is "2015-01", then `year`: 2015, `month`: January
# 5. Run doctests - all must succeed

# Polish
# 1. Wczytaj dane z `DATA` jako `df: pd.DataFrame`
# 2. Dodaj kolumnę `year` i `month` poprzez sparsowanie kolumny `period`
# 3. Nazwa miesiąca musi być ciągiem znaków, a nie liczbą (i.e. 'January', 'May')
# 4. Example: jeżeli kolumna `period` jest "2015-01", to `year`: 2015, `month`: January
# 5. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
result = ...