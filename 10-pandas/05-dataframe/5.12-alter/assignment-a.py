"""
Name: DataFrame Alter Categorize
Difficulty: medium
Lines: 8
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
>>> assert type(result) is pd.DataFrame, \
'Variable `result` must be a `pd.DataFrame` type'

>>> result  # doctest: +NORMALIZE_WHITESPACE
    mileage  consumption status
0    199340            2    old
1     43567            0  young
2    173685            0    old
3    117952            4    old
4    176963            5    old
..      ...          ...    ...
45    49866           16  young
46   123031           17    old
47   125603            5    old
48    11723            9  young
49   174962            3    old
<BLANKLINE>
[50 rows x 3 columns]

Hints:
`pd.NA`
`DataFrame.loc[query, column] = value`
`DataFrame.between()`

"""

# %% SetUp

import pandas as pd
import numpy as np

result: pd.DataFrame

np.random.seed(0)

df = pd.DataFrame({
    'mileage': np.random.randint(0, 200_000, size=50),
    'consumption': np.random.randint(0, 21, size=50),
})

# English
# 1. Modify `df: pd.DataFrame` (cars dataset)
# 2. Add column `status` with values:
#    - `new` if `mileage` from 0 to 10_000 km
#    - `young` if `mileage` from 10_000 km to 100_000 km
#    - `old` if `mileage` above 100_000 km
# 3. All ranges includes lower bounds and exclude upper bounds
# 4. Do not use `pd.cut()` or `pd.select()`
# 5. Run doctests - all must succeed

# Polish
# 1. Zmodyfikuj `df: pd.DataFrame` (zestaw danych o samochodach)
# 2. Dodaj kolumnę `status` o wartościach:
#    - `new` jeżeli `mileage` od 0 do 10_000 km
#    - `young` jeżeli `mileage` od 10_000 km do 100_000 km
#    - `old` jeżeli `mileage` powyżej 100_000 km
# 3. Wszystkie przedziały włączają dolny zares i wyłączają górny zakres
# 4. Nie używaj `pd.cut()` ani `pd.select()`
# 5. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
result = ...