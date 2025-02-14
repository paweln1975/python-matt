"""
Name: OOP MethodClassmethod FromString
Difficulty: easy
Lines: 4
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
Terminal: `python -m doctest -v assignment-c.py`

Tests:
>>> import sys; sys.tracebacklimit = 0
>>> assert sys.version_info >= (3, 9), \
'Python 3.9+ required'

>>> from inspect import isclass

>>> assert isclass(Account)
>>> assert isclass(SystemAccount)
>>> assert isclass(UserAccount)

>>> data = 'root:x:0:0:root:/root:/bin/bash'
>>> admin = SystemAccount.from_passwd(data)
>>> assert type(admin.username) is str
>>> assert type(admin.password) is str
>>> assert type(admin.uid) is int
>>> assert type(admin.gid) is int
>>> assert type(admin.gecos) is str
>>> assert type(admin.home) is str
>>> assert type(admin.shell) is str
>>> assert admin.username == 'root'
>>> assert admin.password == 'x'
>>> assert admin.uid == 0
>>> assert admin.gid == 0
>>> assert admin.gecos == 'root'
>>> assert admin.home == '/root'
>>> assert admin.shell == '/bin/bash'

>>> data = 'watney:x:1000:1000:Mark Watney:/home/watney:/bin/bash'
>>> user = UserAccount.from_passwd(data)
>>> assert type(user.username) is str
>>> assert type(user.password) is str
>>> assert type(user.uid) is int
>>> assert type(user.gid) is int
>>> assert type(user.gecos) is str
>>> assert type(user.home) is str
>>> assert type(user.shell) is str
>>> assert user.username == 'watney'
>>> assert user.password == 'x'
>>> assert user.uid == 1000
>>> assert user.gid == 1000
>>> assert user.gecos == 'Mark Watney'
>>> assert user.home == '/home/watney'
>>> assert user.shell == '/bin/bash'

Hints:
`str.split()`
`int()`

"""

# %% SetUp

from typing import Callable
Account: type
from_passwd: Callable[[type, str], object]

# English
# 1. Modify class `Account`
# 2. Define classmethod `from_passwd()`:
#    - parameter `data: str`, example: 'root:x:0:0:root:/root:/bin/bash'
#    - returns instance of a class on which was called
# 3. Attributes `uid` and `gid` must be int
# 4. Run doctests - all must succeed

# Polish
# 1. Zmodyfikuj klasę `Account`
# 2. Zdefiniuj classmethod `from_passwd()`:
#    - parametr `line: str`, przykład: 'root:x:0:0:root:/root:/bin/bash'
#    - zwraca instancję klasy na której została wykonana
# 3. Atrybuty `uid` i `gid` muszą być int
# 4. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
class Account:
    def __init__(self, username, password, uid, gid, gecos, home, shell):
        self.username = username
        self.password = password
        self.uid = uid
        self.gid = gid
        self.gecos = gecos
        self.home = home
        self.shell = shell

    @classmethod
    def from_passwd(cls, line: str):
        ...

class SystemAccount(Account):
    pass

class UserAccount(Account):
    pass