"""
Name: Pandas Read PythonDict
Difficulty: medium
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
Terminal: `python -m doctest -v assignment-d.py`

Tests:
>>> import sys; sys.tracebacklimit = 0
>>> pd.set_option('display.width', 250)
>>> pd.set_option('display.max_columns', 20)
>>> pd.set_option('display.max_rows', 30)

>>> assert result is not Ellipsis, \
'Assign result to variable: `result`'
>>> assert type(result) is pd.DataFrame, \
'Variable `result` has invalid type, should be `pd.DataFrame`'

>>> result.convert_dtypes()  # doctest: +NORMALIZE_WHITESPACE
  firstname   lastname  group1_gid group1_name  group2_gid group2_name  group3_gid group3_name
0      Mark     Watney           1       users        <NA>        <NA>        <NA>        <NA>
1   Melissa      Lewis           1       users           2       staff           3      admins
2      Rick   Martinez           1       users        <NA>        <NA>        <NA>        <NA>
3      Alex      Vogel        <NA>        <NA>        <NA>        <NA>        <NA>        <NA>
4      Beth  Johanssen           1       users           2       staff        <NA>        <NA>
5     Chris       Beck           1       users        <NA>        <NA>        <NA>        <NA>

Hints:
`dict.pop()`
`enumerate(start=1)`
`column_name = f'group{i}_{field}'`
`pd.DataFrame()`

"""

# %% SetUp

import pandas as pd

result: pd.DataFrame

DATA = [
    {"firstname": "Mark", "lastname": "Watney", "groups": [
        {"gid": 1, "name": "users"}]},

    {"firstname": "Melissa", "lastname": "Lewis", "groups": [
        {"gid": 1, "name": "users"},
        {"gid": 2, "name": "staff"},
        {"gid": 3, "name": "admins"}]},

    {"firstname": "Rick", "lastname": "Martinez", "groups": [
        {"gid": 1, "name": "users"}]},

    {"firstname": "Alex", "lastname": "Vogel", "groups": []},

    {"firstname": "Beth", "lastname": "Johanssen", "groups": [
        {"gid": 1, "name": "users"},
        {"gid": 2, "name": "staff"}]},

    {"firstname": "Chris", "lastname": "Beck", "groups": [
        {"gid": 1, "name": "users"}]},
]

# English
# 1. Convert `DATA` to format with one column per each attrbute for example:
#    - `group1_year`, `group2_year`,
#    - `group1_name`, `group2_name`
# 2. Note, that enumeration starts with one
# 3. Convert data to `result: pd.DataFrame`
# 4. Convert data in `group1_gid` and `group2_gid` to `int`
# 5. Run doctests - all must succeed

# Polish
# 1. Przekonweruj `DATA` do formatu z jedną kolumną dla każdego atrybutu, np:
#    - `group1_year`, `group2_year`,
#    - `group1_name`, `group2_name`
# 2. Zwróć uwagę, że enumeracja zaczyna się od jeden
# 3. Przekonwertuj dane do `result: pd.DataFrame`
# 4. Przekonwertuj dane w `group1_gid` i `group2_gid` do `int`
# 5. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
data = []
for entry in DATA:
    d = {}
    d['firstname'] = entry['firstname']
    d['lastname'] = entry['lastname']
    for index, group in enumerate(entry['groups']):
        d['group{}_gid'.format(index + 1)] = group['gid']
        d['group{}_name'.format(index + 1)] = group['name']
    data.append(d)
print(data)
result = pd.DataFrame(data)
print(result)
