"""
Name: OOP ObjectRelations FlattenDicts
Difficulty: medium
Lines: 7
Minutes: 13

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
>>> from pprint import pprint

>>> result = list(result)
>>> assert type(result) is list
>>> assert len(result) > 0
>>> assert all(type(x) is dict for x in result)

>>> pprint(result, width=30, sort_dicts=False)
[{'firstname': 'Mark',
  'lastname': 'Watney',
  'group1_gid': 1,
  'group1_name': 'staff'},
 {'firstname': 'Melissa',
  'lastname': 'Lewis',
  'group1_gid': 1,
  'group1_name': 'staff',
  'group2_gid': 2,
  'group2_name': 'admins'},
 {'firstname': 'Rick',
  'lastname': 'Martinez'}]

"""

# %% SetUp

result: list[dict]

DATA = [
    {"firstname": "Mark", "lastname": "Watney", "groups": [
        {"gid": 1, "name": "staff"}]},

    {"firstname": "Melissa", "lastname": "Lewis", "groups": [
        {"gid": 1, "name": "staff"},
        {"gid": 2, "name": "admins"}]},

    {"firstname": "Rick", "lastname": "Martinez", "groups": []},
]

# English
# 1. Convert `DATA` to format with one column per each attrbute for example:
#    - `group1_gid`, `group2_gid`
#    - `group1_name`, `group2_name`
# 2. Note, that enumeration starts with one
# 3. Collect data to `result: map`
# 4. Run doctests - all must succeed

# Polish
# 1. Przekonweruj `DATA` do formatu z jedną kolumną dla każdego atrybutu, np:
#    - `group1_gid`, `group2_gid`
#    - `group1_name`, `group2_name`
# 2. Zwróć uwagę, że enumeracja zaczyna się od jeden
# 3. Zbierz dane do `result: map`
# 4. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
result = ...