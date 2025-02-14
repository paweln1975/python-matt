"""
Name: Pandas Read JSON OpenAPI
Difficulty: easy
Lines: 5
Minutes: 5

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

>>> list(result.columns)
['put', 'post', 'get', 'delete']

>>> list(result.index)  # doctest: +NORMALIZE_WHITESPACE
['/pet', '/pet/findByStatus', '/pet/findByTags', '/pet/{petId}', '/pet/{petId}/uploadImage',
 '/store/inventory', '/store/order', '/store/order/{orderId}',
 '/user', '/user/createWithList', '/user/login', '/user/logout', '/user/{username}']

Hints:
`pandas.DataFrame()`
`DataFrame.map()`
`DataFrame.transpose()`

"""

# %% SetUp

import pandas as pd
import requests

result: pd.DataFrame

DATA = 'https://python3.info/_static/openapi.json'
data = requests.get(DATA).json()['paths']

# English
# 1. Read data from `DATA` as `df: pd.DataFrame`
# 2. Use `requests` library
# 3. Transpose data
# 4. If cell is a `dict`, then extract value for `summary`
# 5. If cell is empty, leave `pd.NA`
# 6. Run doctests - all must succeed

# Polish
# 1. Wczytaj dane z `DATA` jako `df: pd.DataFrame`
# 2. Użyj biblioteki `requests`
# 3. Transponuj dane
# 4. Jeżeli komórka jest `dict`, to wyciągnij wartość dla `summary`
# 5. Jeżeli komórka jest pusta, pozostaw `pd.NA`
# 6. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
result = ...