"""
Name: OOP ObjectConstructor Passwd
Difficulty: easy
Lines: 8
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
Terminal: `python -m doctest -v assignment-b.py`

Tests:
>>> import sys; sys.tracebacklimit = 0
>>> assert sys.version_info >= (3, 9), \
'Python 3.9+ required'

>>> from pprint import pprint

>>> result = list(result)
>>> pprint(result)
[SystemAccount(username='root'),
 SystemAccount(username='bin'),
 SystemAccount(username='daemon'),
 SystemAccount(username='adm'),
 SystemAccount(username='shutdown'),
 SystemAccount(username='halt'),
 SystemAccount(username='nobody'),
 SystemAccount(username='sshd'),
 UserAccount(username='mwatney'),
 UserAccount(username='mlewis'),
 UserAccount(username='rmartinez'),
 UserAccount(username='avogel'),
 UserAccount(username='bjohanssen'),
 UserAccount(username='cbeck')]

Hints:
`str.splitlines()`
`str.split()`
`str.strip()`
`map()`

"""

# %% SetUp

from dataclasses import dataclass

SystemAccount: type
UserAccount: type
Account: type
result: list['Account']

DATA = """root:x:0:0:root:/root:/bin/bash
bin:x:1:1:bin:/bin:/sbin/nologin
daemon:x:2:2:daemon:/sbin:/sbin/nologin
adm:x:3:4:adm:/var/adm:/sbin/nologin
shutdown:x:6:0:shutdown:/sbin:/sbin/shutdown
halt:x:7:0:halt:/sbin:/sbin/halt
nobody:x:99:99:Nobody:/:/sbin/nologin
sshd:x:74:74:Privilege-separated SSH:/var/empty/sshd:/sbin/nologin
mwatney:x:1000:1000:Mark Watney:/home/mwatney:/bin/bash
mlewis:x:1001:1001:Melissa Lewis:/home/mlewis:/bin/bash
rmartinez:x:1002:1002:Rick Martinez:/home/rmartinez:/bin/bash
avogel:x:1003:1003:Alex Vogel:/home/avogel:/bin/bash
bjohanssen:x:1004:1004:Beth Johanssen:/home/bjohanssen:/bin/bash
cbeck:x:1005:1005:Chris Beck:/home/cbeck:/bin/bash"""

@dataclass
class SystemAccount:
    username: str

@dataclass
class UserAccount:
    username: str

# English
# 1. Iterate over lines in `DATA` and split line by colon
# 2. Create class `Account` that returns instances of `UserAccount` or `SystemAccount`
#    depending on the value of UID field
# 3. User ID (UID) is the third field, e.g.
#    `root:x:0:0:root:/root:/bin/bash` has UID equal to `0`
# 4. If UID is:
#    - below 1000, then account is system (`SystemAccount`)
#    - 1000 or more, then account is user (`UserAccount`)
# 5. Run doctests - all must succeed

# Polish
# 1. Iteruj po liniach w `DATA` i podziel linię po dwukropku
# 2. Stwórz klasę `Account`, która zwraca instancje klas
#    `UserAccount` lub `SystemAccount` w zależności od wartości pola UID
# 3. User ID (UID) to trzecie pole, np.
#    `root:x:0:0:root:/root:/bin/bash` to UID jest równy `0`
# 4. Jeżeli UID jest:
#    - poniżej 1000, to konto jest systemowe (`SystemAccount`)
#    - 1000 lub więcej, to konto użytkownika (`UserAccount`)
# 5. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
result = ...