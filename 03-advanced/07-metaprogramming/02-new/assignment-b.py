"""
* Assignment: OOP ObjectConstructor Passwd
* Complexity: easy
* Lines of code: 21 lines
* Time: 13 min

English:
    1. Iterate over lines in `DATA` and split line by colon
    2. Create class `Account` that returns instances of `UserAccount` or `SystemAccount`
       depending on the value of UID field
    3. User ID (UID) is the third field, e.g.
       `root:x:0:0:root:/root:/bin/bash` has UID equal to `0`
    4. If UID is:
       a. below 1000, then account is system (`SystemAccount`)
       b. 1000 or more, then account is user (`UserAccount`)
    5. Run doctests - all must succeed

Polish:
    1. Iteruj po liniach w `DATA` i podziel linię po dwukropku
    2. Stwórz klasę `Account`, która zwraca instancje klas
       `UserAccount` lub `SystemAccount` w zależności od wartości pola UID
    3. User ID (UID) to trzecie pole, np.
       `root:x:0:0:root:/root:/bin/bash` to UID jest równy `0`
    4. Jeżeli UID jest:
       a. poniżej 1000, to konto jest systemowe (`SystemAccount`)
       b. 1000 lub więcej, to konto użytkownika (`UserAccount`)
    5. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `str.splitlines()`
    * `str.split()`
    * `str.strip()`
    * `map()`

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from pprint import pprint

    >>> result = list(result)
    >>> pprint(result)
    [SystemAccount(username='root', uid=0),
     SystemAccount(username='bin', uid=1),
     SystemAccount(username='daemon', uid=2),
     SystemAccount(username='adm', uid=3),
     SystemAccount(username='shutdown', uid=6),
     SystemAccount(username='halt', uid=7),
     SystemAccount(username='nobody', uid=99),
     SystemAccount(username='sshd', uid=74),
     UserAccount(username='mwatney', uid=1000),
     UserAccount(username='mlewis', uid=1001),
     UserAccount(username='rmartinez', uid=1002),
     UserAccount(username='avogel', uid=1003),
     UserAccount(username='bjohanssen', uid=1004),
     UserAccount(username='cbeck', uid=1005)]
"""

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

from dataclasses import dataclass


@dataclass
class SystemAccount:
    username: str
    uid: int

@dataclass
class UserAccount:
    username: str
    uid: int


# Parse DATA and convert to UserAccount or SystemAccount
# type: list[Account]
result = ...

