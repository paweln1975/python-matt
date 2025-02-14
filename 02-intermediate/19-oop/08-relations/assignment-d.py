
# region Show Doctests
"""
Doctests:
>>> import sys; sys.tracebacklimit = 0
>>> assert sys.version_info >= (3, 9), \
'Python 3.9+ required'

>>> result = list(result)
>>> assert type(result) is list
>>> assert len(result) > 0
>>> assert all(type(x) is dict for x in result)

>>> from pprint import pprint
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
# endregion

# region Show Types
result: list[dict]
# endregion

class User:
    def __init__(self, firstname, lastname, groups=None):
        self.firstname = firstname
        self.lastname = lastname
        self.groups = groups if groups else []

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
# 1. Convert `DATA` to format with one column per each attribute for example:
#    - `group1_gid`, `group2_gid`,
#    - `group1_name`, `group2_name`
# 2. Note, that enumeration starts with one
# 3. Run doctests - all must succeed

# Polish
# 1. Przekonwertuj `DATA` do formatu z jedną kolumną dla każdego atrybutu, np:
#    - `group1_gid`, `group2_gid`,
#    - `group1_name`, `group2_name`
# 2. Zwróć uwagę, że enumeracja zaczyna się od jeden
# 3. Uruchom doctesty - wszystkie muszą się powieść

# region Show Hints
# - `vars(obj)` -> `dict`
# endregion

# %% Your code
def parse(user: dict) -> dict:
    user = vars(user)
    groups = map(vars, user.pop('groups'))
    group_dict = {}
    for ngroup, group in enumerate(groups, start=1):
        group_dict.update(
            {f'group{ngroup}_gid' : group['gid'],
            f'group{ngroup}_name' : group['name']}
        )
    return user | group_dict

result = map(parse, DATA)
