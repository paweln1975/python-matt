
# region Show Doctests
"""
Doctests:
>>> import sys; sys.tracebacklimit = 0
>>> assert sys.version_info >= (3, 9), \
'Python 3.9+ required'

>>> assert result is not Ellipsis, \
'Assign result to variable: `result`'
>>> assert type(result) is list, \
'Variable `result` has invalid type, should be list'
>>> assert len(result) > 0, \
'Variable `result` should not be empty'

>>> from pprint import pprint
>>> pprint(result, width=80, sort_dicts=False)
[{'firstname': 'Mark', 'lastname': 'Watney', 'age': 41},
 {'firstname': 'Melissa', 'lastname': 'Lewis', 'age': 40},
 {'firstname': 'Rick', 'lastname': 'Martinez', 'age': 39},
 {'firstname': 'Alex', 'lastname': 'Vogel', 'age': 40},
 {'firstname': 'Chris', 'lastname': 'Beck', 'age': 36},
 {'firstname': 'Beth', 'lastname': 'Johanssen', 'age': 29}]
"""
# endregion

# region Show Imports
import json
# endregion

# region Show Types
result: list[dict[str, str|int]]
# endregion

DATA = """
[
    {"firstname": "Mark", "lastname": "Watney", "age": 41},
    {"firstname": "Melissa", "lastname": "Lewis", "age": 40},
    {"firstname": "Rick", "lastname": "Martinez", "age": 39},
    {"firstname": "Alex", "lastname": "Vogel", "age": 40},
    {"firstname": "Chris", "lastname": "Beck", "age": 36},
    {"firstname": "Beth", "lastname": "Johanssen", "age": 29}
]
"""

# English
# 1. Load `DATA` from JSON format
# 2. Convert data to `result: list[dict]`
# 3. Run doctests - all must succeed

# Polish
# 1. Wczytaj `DATA` z formatu JSON
# 2. Przekonwertuj dane do `result: list[dict]`
# 3. Uruchom doctesty - wszystkie muszą się powieść

# region Show Hints
# - `json.loads()`
# endregion

# %% Your code
result = json.loads(DATA)
