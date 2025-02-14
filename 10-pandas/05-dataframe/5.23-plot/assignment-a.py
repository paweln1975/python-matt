"""
Name: DataFrame Plot
Difficulty: medium
Lines: 15
Minutes: 21

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
Terminal: `python -m doctest -v assignment-a.py`

Tests:
>>> import sys; sys.tracebacklimit = 0
>>> assert sys.version_info >= (3, 9), \
'Python 3.9+ required'

>>> pd.set_option('display.width', 500)
>>> pd.set_option('display.max_columns', 10)
>>> pd.set_option('display.max_rows', 10)

>>> assert result is not Ellipsis, \
'Assign result to variable: `result`'
>>> assert type(result) is pd.Series, \
'Variable `result` must be a `pd.Series` type'

>>> result  # doctest: +NORMALIZE_WHITESPACE
datetime
2019-09-28 00:00:00+00:00    1
2019-09-28 01:00:00+00:00    1
2019-09-28 02:00:00+00:00    1
2019-09-28 03:00:00+00:00    1
2019-09-28 04:00:00+00:00    0
                            ..
2019-09-28 19:00:00+00:00    1
2019-09-28 20:00:00+00:00    1
2019-09-28 21:00:00+00:00    1
2019-09-28 22:00:00+00:00    1
2019-09-28 23:00:00+00:00    1
Freq: h, Name: value, Length: 24, dtype: int64

Hints:
`pd.Series.apply(np.sign)` :ref:`Numpy signum`
`pd.Series.resample('H').sum()`

"""

# %% SetUp

import numpy as np
import pandas as pd

result: pd.Series

DATA = 'https://python3.info/_static/aatc-mission-exp12.xlsx'
WHERE = 'Sleeping Quarters upper'
WHEN = '2019-09-28'

# English
# 1. Read data from `DATA` as `df: pd.DataFrame`
# 2. Select `Luminance` stylesheet
# 3. Parse column with dates
# 4. Select desired date and location, then resample by hour
# 5. Display chart (line) with activity hours in "Sleeping Quarters upper" location
# 6. Active is when `Luminance` is not zero
# 7. Easy: for day 2019-09-28
# 8. Advanced: for each day, as subplots
# 9. Run doctests - all must succeed

# Polish
# 1. Wczytaj dane z `DATA` jako `df: pd.DataFrame`
# 2. Wybierz arkusz `Luminance`
# 3. Sparsuj kolumny z datami
# 4. Wybierz pożądaną datę i lokację, następnie próbkuj co godzinę
# 5. Aktywność jest gdy `Luminance` jest różna od zera
# 6. Wyświetl wykres (line) z godzinami aktywności w dla lokacji "Sleeping Quarters upper"
# 7. Łatwe: dla dnia 2019-09-28
# 8. Zaawansowane: dla wszystkich dni, jako subplot
# 9. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
result = ...