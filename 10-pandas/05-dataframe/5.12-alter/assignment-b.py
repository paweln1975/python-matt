"""
Name: DataFrame Alter Cut
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
Terminal: `python -m doctest -v assignment-b.py`

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

>>> result
    mileage  consumption      type
0    199340            2       car
1     43567            0  electric
2    173685            0  electric
3    117952            4       car
4    176963            5       car
..      ...          ...       ...
45    49866           16     truck
46   123031           17     truck
47   125603            5       car
48    11723            9       car
49   174962            3       car
<BLANKLINE>
[50 rows x 3 columns]

Hints:
`pd.DataFrame()`

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
# 2. Using `pd.cut` add column `type`:
#    - if `consumption` from 0 to 1 then `type` is `electric`
#    - if `consumption` from 1 to 10 then `type` is `car`
#    - if `consumption` from 10 to 100 then `type` is `truck`
# 3. All ranges includes lower bounds and exclude upper bounds
# 4. Use `pd.cut()` function
# 5. Run doctests - all must succeed

# Polish
# 1. Zmodyfikuj `df: pd.DataFrame` (zestaw danych o samochodach)
# 2. Używając `pd.cut` dodaj kolumnę `type`:
#    - jeżeli `consumption` od 0 do 1 to `type` jest `electric`
#    - jeżeli `consumption` od 2 do 10 to `type` jest `car`
#    - jeżeli `consumption` od 10 do 100 to `type` jest `truck`
# 3. Wszystkie przedziały włączają dolny zares i wyłączają górny zakres
# 4. Użyj funkcji `pd.cut()`
# 5. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
result = ...