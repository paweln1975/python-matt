
# region Show Doctests
"""
Doctests:
>>> import sys; sys.tracebacklimit = 0
>>> assert sys.version_info >= (3, 9), \
'Python 3.9+ required'

>>> result = pickle.loads(result)

>>> from pprint import pprint
>>> pprint(result)
[User(firstname='Mark', lastname='Watney', group=1),
 User(firstname='Melissa', lastname='Lewis', group=3),
 User(firstname='Rick', lastname='Martinez', group=1),
 User(firstname='Alex', lastname='Vogel', group=None),
 User(firstname='Chris', lastname='Beck', group=1),
 User(firstname='Beth', lastname='Johanssen', group=2)]
"""
# endregion

# region Show Imports
import pickle
# endregion

# region Show Types
result: bytes
# endregion

class User:
    def __init__(self, firstname, lastname, group):
        self.firstname = firstname
        self.lastname = lastname
        self.group = group

    def __repr__(self):
        clsname = self.__class__.__name__
        firstname = self.firstname
        lastname = self.lastname
        group = self.group
        return f'{clsname}({firstname=}, {lastname=}, {group=})'

DATA = [
    User(firstname='Mark', lastname='Watney', group=1),
    User(firstname='Melissa', lastname='Lewis', group=3),
    User(firstname='Rick', lastname='Martinez', group=1),
    User(firstname='Alex', lastname='Vogel', group=None),
    User(firstname='Chris', lastname='Beck', group=1),
    User(firstname='Beth', lastname='Johanssen', group=2),
]

# English
# 1. Define `result: bytes` with dumped `DATA`
# 2. Use `pickle` module
# 3. Run doctests - all must succeed

# Polish
# 1. Zdefiniuj `result: bytes` ze zrzuconym `DATA`
# 2. Użyj modułu `pickle`
# 3. Uruchom doctesty - wszystkie muszą się powieść

# %% Your code
result = pickle.dumps(DATA)
