"""
Name: Functional Recap FlattenClasses
Difficulty: hard
Lines: 15
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
Terminal: `python -m doctest -v assignment-d.py`

Tests:
>>> import sys; sys.tracebacklimit = 0
>>> assert sys.version_info >= (3, 9), \
'Python 3.9+ required'

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

Hints:
`vars(obj)` -> `dict`

"""

# %% SetUp

from itertools import starmap
from functools import reduce
from operator import or_

result: map

class User:
    def __init__(self, firstname, lastname, groups=()):
        self.firstname = firstname
        self.lastname = lastname
        self.groups = list(groups)

class Group:
    def __init__(self, gid, name):
        self.gid = gid
        self.name = name

DATA = [
    User('Mark', 'Watney', groups=[
        Group(gid=1, name='staff')]),

    User('Melissa', 'Lewis', groups=[
        Group(gid=1, name='staff'),
        Group(gid=2, name='admins')]),

    User('Rick', 'Martinez'),
]

# English
# 1. Convert `DATA` to format with one column per each attrbute for example:
#    - `Group1_year`, `Group2_year`,
#    - `Group1_name`, `Group2_name`
# 2. Note, that enumeration starts with one
# 3. Run doctests - all must succeed

# Polish
# 1. Przekonweruj `DATA` do formatu z jedną kolumną dla każdego atrybutu, np:
#    - `Group1_year`, `Group2_year`,
#    - `Group1_name`, `Group2_name`
# 2. Zwróć uwagę, że enumeracja zaczyna się od jeden
# 3. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
def flat(i, groupobj):
    group = groupobj
    gid = group.get('gid')
    name = group.get('name')
    return {f'group{i}_gid': gid, f'group{i}_name': name}

def flatten(groups):
    dicts = starmap(flat, enumerate(groups, start=1))
    return reduce(or_, dicts, {})

def convert(userobj):
    user = userobj
    firstname = user.get('firstname')
    lastname = user.get('lastname')
    groups = flatten(user.get('groups'))
    return {'firstname': firstname, 'lastname': lastname} | groups

result = map(convert, DATA)