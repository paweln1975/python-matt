
# region Show Doctests
"""
Doctests:
>>> import sys; sys.tracebacklimit = 0
>>> assert sys.version_info >= (3, 9), \
'Python 3.9+ required'

>>> result = User('Mark', 'Watney')
>>> print(result)
Mark Watney
>>> result = User('Melissa', 'Lewis')
>>> print(result)
Melissa Lewis
>>> result = User('Rick', 'Martinez')
>>> print(result)
Rick Martinez

>>> Group(gid=1, name='admins')
1(admins)
>>> Group(gid=2, name='staff')
2(staff)
>>> Group(gid=3, name='users')
3(users)

>>> result = Accounts(users=[])
>>> print(result)
<BLANKLINE>

>>> result = User('Mark', 'Watney', groups=[
...     Group(gid=2, name='staff'),
... ])
>>> print(result)
Mark Watney member of [2(staff)]

>>> result = User('Melissa', 'Lewis', groups=[
...     Group(gid=1, name='admins'),
...     Group(gid=2, name='staff'),
... ])
>>> print(result)
Melissa Lewis member of [1(admins), 2(staff)]

>>> result = Accounts([
...     User('Mark', 'Watney', groups=[
...         Group(gid=2, name='staff'),
...     ]),
...     User('Melissa', 'Lewis', groups=[
...         Group(gid=1, name='admins'),
...         Group(gid=2, name='staff'),
...     ]),
...     User('Rick', 'Martinez'),
... ])
>>>
>>> print(result)  # doctest: +NORMALIZE_WHITESPACE
Mark Watney member of [2(staff)]
Melissa Lewis member of [1(admins), 2(staff)]
Rick Martinez
"""
# endregion

# region Show Types
from typing import Callable
Accounts: type
User: type
Group: type
__repr__: Callable[[object], str]
__str__: Callable[[object], str]
# endregion

# English
# 1. Modify classes to overwrite `__str__()` and `__repr__()` methods
# 2. Run doctests - all must succeed

# Polish
# 1. Zmodyfikuj klasy aby nadpisać metody `__str__()` and `__repr__()`
# 2. Uruchom doctesty - wszystkie muszą się powieść

# region Show Hints
# - Define `Accounts.__str__()`
# - Define `User.__str__()`
# - Define `Group.__repr__()`
# - Printing list will call repr on all elements
# endregion

# %% Your code
class Accounts:
    def __init__(self, users):
        self.users = users
    def __repr__(self):
        return f'Accounts({self.users})'

    def __str__(self):
        return '\n'.join(map(str, self.users))

class User:
    def __init__(self, firstname, lastname, groups=None):
        self.firstname = firstname
        self.lastname = lastname
        self.groups = groups if groups else []

    def __repr__(self):
        return f'User({self.firstname}, {self.lastname})'

    def __str__(self):
        if self.groups:
            return f'{self.firstname} {self.lastname} member of {self.groups}'
        else:
            return f'{self.firstname} {self.lastname}'

class Group:
    def __init__(self, gid, name):
        self.gid = gid
        self.name = name

    def __repr__(self):
        return f'{self.gid}({self.name})'

    def __str__(self):
        return f'{self.gid}({self.name})'
