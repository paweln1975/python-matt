"""
Name: Pandas Read JSON OpenAPI
Difficulty: medium
Lines: 3
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
Terminal: `python -m doctest -v assignment-b.py`

Tests:
>>> import sys; sys.tracebacklimit = 0
>>> assert sys.version_info >= (3, 9), \
'Python 3.9+ required'

>>> assert result is not Ellipsis, \
'Assign result to variable: `result`'
>>> assert type(result) is pd.DataFrame, \
'Variable `result` must be a `pd.DataFrame` type'

>>> list(result.index)
['put', 'post', 'get', 'delete']

>>> list(result.columns)  # doctest: +NORMALIZE_WHITESPACE
['/pet', '/pet/findByStatus', '/pet/findByTags', '/pet/{petId}', '/pet/{petId}/uploadImage',
 '/store/inventory', '/store/order', '/store/order/{orderId}',
 '/user', '/user/createWithList', '/user/login', '/user/logout', '/user/{username}']

Hints:
`pd.DataFrame(data)`

"""

# %% SetUp

import pandas as pd
import requests

resp: requests.models.Response
data: dict
result: pd.DataFrame

DATA = 'https://python3.info/_static/openapi.json'

# English
# 1. Import `requests` module
# 2. Define `resp` with result of `requests.get()` for `DATA`
# 3. Define `data` with conversion of `resp` from JSON to Python dict by calling `.json()` on `resp`
# 4. Define `result: pd.DataFrame` from value for key `paths` in `data` dict
# 5. Run doctests - all must succeed

# Polish
# 1. Zaimportuj moduł `requests`
# 2. Zdefiniuj `resp` z resultatem `requests.get()` dla `DATA`
# 3. Zdefiniuj `data` z przekształceniem `resp` z JSON do Python dict wywołując `.json()` na `resp`
# 4. Zdefiniuj `result: pd.DataFrame` dla wartości z klucza `paths` w słowniku `data`
# 5. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
resp = ...
data = ...
result = ...