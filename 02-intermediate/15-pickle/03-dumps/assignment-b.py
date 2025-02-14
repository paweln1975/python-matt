
# region Show Doctests
"""
Doctests:
>>> import sys; sys.tracebacklimit = 0
>>> assert sys.version_info >= (3, 9), \
'Python 3.9+ required'

>>> result = pickle.loads(result)

>>> from pprint import pprint
>>> pprint(result)
[User(firstname='Mark', lastname='Watney', age=41, groups='1(users)'),
 User(firstname='Melissa', lastname='Lewis', age=40, groups='1(users),2(staff),3(admins)'),
 User(firstname='Rick', lastname='Martinez', age=39, groups='1(users)'),
 User(firstname='Alex', lastname='Vogel', age=40, groups=''),
 User(firstname='Beth', lastname='Johanssen', age=29, groups='1(users),2(staff)'),
 User(firstname='Chris', lastname='Beck', age=36, groups='1(users)')]
"""
# endregion

# region Show Imports
import pickle
# endregion

# region Show Types
result: bytes
# endregion

class Group:
    def __init__(self, gid, name):
        self.gid = gid
        self.name = name

    def __repr__(self):
        return f'{self.gid}({self.name})'

class User:
    def __init__(self, firstname, lastname, age, groups=None):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.groups = groups if groups else []

    def __repr__(self):
        clsname = self.__class__.__name__
        firstname = self.firstname
        lastname = self.lastname
        groups = ','.join(repr(x) for x in self.groups)
        age = self.age
        return f'{clsname}({firstname=}, {lastname=}, {age=}, {groups=})'

DATA = [
    User(firstname='Mark', lastname='Watney', age=41, groups=[
        Group(gid=1, name='users'),
    ]),

    User(firstname='Melissa', lastname='Lewis', age=40, groups=[
        Group(gid=1, name='users'),
        Group(gid=2, name='staff'),
        Group(gid=3, name='admins'),
    ]),

    User(firstname='Rick', lastname='Martinez', age=39, groups=[
        Group(gid=1, name='users'),
    ]),

    User(firstname='Alex', lastname='Vogel', age=40, groups=[]),

    User(firstname='Beth', lastname='Johanssen', age=29, groups=[
        Group(gid=1, name='users'),
        Group(gid=2, name='staff'),
    ]),

    User(firstname='Chris', lastname='Beck', age=36, groups=[
        Group(gid=1, name='users'),
    ]),
]

# English
# 1. Save `DATA` to `FILE`
# 2. Use `pickle` module
# 3. Run doctests - all must succeed

# Polish
# 1. Zapisz `DATA` do `FILE`
# 2. Użyj modułu `pickle`
# 3. Uruchom doctesty - wszystkie muszą się powieść

# %% Your code
result = pickle.dumps(DATA)
