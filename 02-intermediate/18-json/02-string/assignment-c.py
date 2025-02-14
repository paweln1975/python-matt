
# region Show Doctests
"""
Doctests:
>>> import sys; sys.tracebacklimit = 0
>>> assert sys.version_info >= (3, 9), \
'Python 3.9+ required'

>>> assert result is not Ellipsis, \
'Assign result to variable: `result`'
>>> assert type(result) is str, \
'Variable `result` has invalid type, should be str'
>>> assert len(result) > 0, \
'Variable `result` should not be empty'

>>> print(result)  # doctest: +NORMALIZE_WHITESPACE
[["firstname", "lastname", "age"],
 ["Mark", "Watney", 41],
 ["Melissa", "Lewis", 40],
 ["Rick", "Martinez", 39],
 ["Alex", "Vogel", 40],
 ["Chris", "Beck", 36],
 ["Beth", "Johanssen", 29]]
"""
# endregion

# region Show Imports
import json
# endregion

# region Show Types
result: str
# endregion

DATA = [
    ('firstname', 'lastname', 'age'),
    ('Mark', 'Watney', 41),
    ('Melissa', 'Lewis', 40),
    ('Rick', 'Martinez', 39),
    ('Alex', 'Vogel', 40),
    ('Chris', 'Beck', 36),
    ('Beth', 'Johanssen', 29),
]

# English
# 1. Dump `DATA` to JSON format
# 2. Run doctests - all must succeed

# Polish
# 1. Zrzuć `DATA` do formatu JSON
# 2. Uruchom doctesty - wszystkie muszą się powieść

# region Show Hints
# - `json.dumps()`
# endregion

# %% Your code
result = json.dumps(DATA)
