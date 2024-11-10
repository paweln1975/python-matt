"""
* Assignment: File Read Passwd
* Type: homework
* Complexity: hard
* Lines of code: 77 lines
* Time: 89 min

English:
    1. In the current directory, the following files were saved:
        a. `FILE_PASSWD` with content of `etc-passwd.txt` file
        b. `FILE_SHADOW` with content of `etc-shadow.txt` file
        c. `FILE_GROUP` with content of `etc-group`.txt file
    2. Parse files and collect in `list[dict]` format with keys:
        a. account_expiration_date: int | None
        b. account_locked: bool
        c. password_algorithm: str | None
        d. password_hash: str | None
        e. password_inactivity_period: int | None
        f. password_last_changed: date | None
        g. password_max_age: int | None
        h. password_min_age: int | None
        i. password_salt: str | None
        j. password_warning_period: int | None
        k. user_comment: str | None
        l. user_gid: int
        m. user_groups: list[str]
        n. user_home: str
        o. user_login: str
        p. user_shell: str
        q. user_uid: int
    3. Define variable `result: list[dict]`
       with user data whose `UID` is greater or equal to 1000
    4. Run doctests - all must succeed

Polish:
    1. W obencym katalogu zapisano następujące pliki:
        a. `FILE_PASSWD` z zawartością pliku `etc-passwd.txt`
        b. `FILE_SHADOW` z zawartością pliku `etc-shadow.txt`
        c. `FILE_GROUP` z zawartością pliku `etc-group.txt`
    2. Sparsuj pliki i zbierz dane w formacie `list[dict]` z kluczami:
        a. account_expiration_date: int | None
        b. account_locked: bool
        c. password_algorithm: str | None
        d. password_hash: str | None
        e. password_inactivity_period: int | None
        f. password_last_changed: date | None
        g. password_max_age: int | None
        h. password_min_age: int | None
        i. password_salt: str | None
        j. password_warning_period: int | None
        k. user_comment: str | None
        l. user_gid: int
        m. user_groups: list[str]
        n. user_home: str
        o. user_login: str
        p. user_shell: str
        q. user_uid: int
    3. Zdefiniuj zmienną `result: list[dict]` z danymi
       użytkowników których `UID` jest większy lub równy niż 1000
    4. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * len()
    * open().read()
    * str.splitlines()
    * str.strip()
    * str.startswith()
    * str.split()
    * str.isspace()
    * list.append()
    * datetime.date(1970, 1, 1)
    * datetime.timedelta(days=...)
    * dict.get()
    * dict.update()
    * dict1 | dict2
    * ... if ... else ...
    * passwd['mwatney'] = {...}
    * shadow['mwatney'] = {...}
    * groups['mwatney'] = {...}
    * result['mwatney'] = dict1 | dict2 | dict3

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from pprint import pprint

    >>> pprint(result)
    [{'account_expiration_date': None,
      'account_locked': False,
      'password_algorithm': 'SHA-512',
      'password_hash': 'bXGOh7dIfOWpUb/Tuqr7yQVCqL3UkrJns9.7msfvMg4ZO/PsFC5Tbt32PXAw9qRFEBs1254aLimFeNM8YsYOv.',
      'password_inactivity_period': None,
      'password_last_changed': datetime.date(2015, 4, 25),
      'password_max_age': None,
      'password_min_age': None,
      'password_salt': '5H0QpwprRiJQR19Y',
      'password_warning_period': None,
      'user_comment': 'Mark Watney',
      'user_gid': 1000,
      'user_groups': ['user', 'staff'],
      'user_home': '/home/mwatney',
      'user_login': 'mwatney',
      'user_shell': '/bin/bash',
      'user_uid': 1000},
     {'account_expiration_date': None,
      'account_locked': False,
      'password_algorithm': 'SHA-512',
      'password_hash': 'tgfvvFWJJ5FKmoXiP5rXWOjwoEBOEoAuBi3EphRbJqqjWYvhEM2wa67L9XgQ7W591FxUNklkDIQsk4kijuhE50',
      'password_inactivity_period': None,
      'password_last_changed': datetime.date(2015, 7, 16),
      'password_max_age': 99999,
      'password_min_age': 0,
      'password_salt': 'P9zn0KwR',
      'password_warning_period': 7,
      'user_comment': 'Melissa Lewis',
      'user_gid': 1001,
      'user_groups': ['user', 'staff', 'admin'],
      'user_home': '/home/mlewis',
      'user_login': 'mlewis',
      'user_shell': '/bin/bash',
      'user_uid': 1001},
     {'account_expiration_date': datetime.date(2005, 11, 9),
      'account_locked': False,
      'password_algorithm': 'MD5',
      'password_hash': 'SWlkjRWexrXYgc98F.',
      'password_inactivity_period': 30,
      'password_last_changed': datetime.date(2005, 2, 11),
      'password_max_age': 90,
      'password_min_age': 0,
      'password_salt': '.QKDPc5E',
      'password_warning_period': 5,
      'user_comment': 'Rick Martinez',
      'user_gid': 1002,
      'user_groups': ['user', 'staff'],
      'user_home': '/home/rmartinez',
      'user_login': 'rmartinez',
      'user_shell': '/bin/bash',
      'user_uid': 1002},
     {'account_expiration_date': None,
      'account_locked': True,
      'password_algorithm': None,
      'password_hash': None,
      'password_inactivity_period': None,
      'password_last_changed': datetime.date(2014, 12, 27),
      'password_max_age': 99999,
      'password_min_age': 0,
      'password_salt': None,
      'password_warning_period': 7,
      'user_comment': 'Alex Vogel',
      'user_gid': 1003,
      'user_groups': ['user'],
      'user_home': '/home/avogel',
      'user_login': 'avogel',
      'user_shell': '/bin/bash',
      'user_uid': 1003},
     {'account_expiration_date': None,
      'account_locked': True,
      'password_algorithm': None,
      'password_hash': None,
      'password_inactivity_period': None,
      'password_last_changed': datetime.date(2014, 12, 27),
      'password_max_age': 99999,
      'password_min_age': 0,
      'password_salt': None,
      'password_warning_period': 7,
      'user_comment': 'Beth Johanssen',
      'user_gid': 1004,
      'user_groups': ['user', 'staff', 'admin'],
      'user_home': '/home/bjohanssen',
      'user_login': 'bjohanssen',
      'user_shell': '/bin/bash',
      'user_uid': 1004},
     {'account_expiration_date': None,
      'account_locked': True,
      'password_algorithm': None,
      'password_hash': None,
      'password_inactivity_period': None,
      'password_last_changed': datetime.date(2014, 12, 27),
      'password_max_age': 99999,
      'password_min_age': 0,
      'password_salt': None,
      'password_warning_period': 7,
      'user_comment': 'Chris Beck',
      'user_gid': 1005,
      'user_groups': ['user', 'staff'],
      'user_home': '/home/cbeck',
      'user_login': 'cbeck',
      'user_shell': '/bin/bash',
      'user_uid': 1005}]

      >>> from os import remove
      >>> remove(FILE_GROUP)
      >>> remove(FILE_SHADOW)
      >>> remove(FILE_PASSWD)
"""

FILE_PASSWD = 'etc_passwd.txt'
FILE_SHADOW = 'etc_shadow.txt'
FILE_GROUP = 'etc_group.txt'

with open(FILE_PASSWD, mode='wt', encoding='UTF-8') as file:
    file.write("""##
# Structure of `/etc/passwd` file:
# - user_login: username
# - user_password: 'x' indicates that shadow passwords are used (skip this field)
# - user_uid: user ID number
# - user_gid: group ID number
# - user_comment: comment ie. full name
# - user_home: path to home directory
# - user_shell: path to shell
##
root:x:0:0:root:/root:/bin/bash
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
cbeck:x:1005:1005:Chris Beck:/home/cbeck:/bin/bash
""")

with open(FILE_SHADOW, mode='wt', encoding='UTF-8') as file:
    file.write("""##
# Structure of `/etc/shadow` file:
#   - login: user login name
#   - password_encrypted: encrypted password (see below for more details)
#   - password_last_changed: days since 1970-01-01 password was last changed
#   - password_min_age: days before which password may not be changed
#   - password_max_age: days after which password must be changed
#   - password_warning_period: days before password is to expire that user is warned of pending password expiration
#   - password_inactivity_period: days after password expires that account is considered inactive and disabled
#   - account_expiration_date: days since 1970-01-01 when account will be disabled
#   - reserved: reserved for future use (skip this field)
#
# Password field (split by `$`):
#   - algorithm
#   - salt
#   - password hash
#
# Password algorithms:
#   - '1' - MD5
#   - '2a' - Blowfish
#   - '2y' - Blowfish
#   - '5' - SHA-256
#   - '6' - SHA-512
#
# Password special chars:
#   - ' '  - account unlocked, password is not required to log in
#   - '*'  - account locked, cannot be unlocked, and no password has ever been set
#   - '!!' - account locked, can be unlocked, waiting for initial password to be set by admin
#   - '!'  - account locked, can be unlocked, and no password has ever been set
#   - '!<password_hash>' - account locked, can be unlocked, but password is set
##
root:$6$Ke02nYgo.9v0SF4p$hjztYvo/M4buqO4oBX8KZTftjCn6fE4cV5o/I95QPekeQpITwFTRbDUBYBLIUx2mhorQoj9bLN8v.w6btE9xy1:16431:0:99999:7:::
bin:*:16431:0:99999:7:::
daemon:*:16431:0:99999:7:::
adm:*:16431:0:99999:7:::
shutdown:*:16431:0:99999:7:::
halt:*:16431:0:99999:7:::
nobody:*:16431:0:99999:7:::
sshd:*:16431:0:99999:7:::
mwatney:$6$5H0QpwprRiJQR19Y$bXGOh7dIfOWpUb/Tuqr7yQVCqL3UkrJns9.7msfvMg4ZO/PsFC5Tbt32PXAw9qRFEBs1254aLimFeNM8YsYOv.:16550::::::
mlewis:$6$P9zn0KwR$tgfvvFWJJ5FKmoXiP5rXWOjwoEBOEoAuBi3EphRbJqqjWYvhEM2wa67L9XgQ7W591FxUNklkDIQsk4kijuhE50:16632:0:99999:7:::
rmartinez:$1$.QKDPc5E$SWlkjRWexrXYgc98F.:12825:0:90:5:30:13096:
avogel:!!:16431:0:99999:7:::
bjohanssen:!:16431:0:99999:7:::
cbeck:*:16431:0:99999:7:::
""")

with open(FILE_GROUP, mode='wt', encoding='UTF-8') as file:
    file.write("""##
# Structure of `/etc/group` file:
#   - group_name: group name
#   - group_password: 'x' indicates that shadow passwords are used
#   - group_gid: group id
#   - group_members: comma-separated logins from `/etc/passwd`
##
root::0:root
other::1:
bin::2:root,bin,daemon
sys::3:root,bin,sys,adm
adm::4:root,adm,daemon
mail::6:root
daemon::12:root,daemon
sysadmin::14:root
user::1001:mwatney,mlewis,rmartinez,avogel,bjohanssen,cbeck
staff::1002:mwatney,mlewis,rmartinez,bjohanssen,cbeck
admin::1003:mlewis,bjohanssen
nobody::60001:
noaccess::60002:
nogroup::65534:
""")

ALGORITHMS = {
    '1': 'MD5',
    '2a': 'Blowfish',
    '2y': 'Blowfish',
    '5': 'SHA-256',
    '6': 'SHA-512',
}

# In the current directory, the following files were saved:
# - `FILE_PASSWD` with content of `etc-passwd.txt` file
# - `FILE_SHADOW` with content of `etc-shadow.txt` file
# - `FILE_GROUP` with content of `etc-group.txt` file
# Parse all files and collect in `list[dict]` format:
# - account_expiration_date: int | None
# - account_locked: bool
# - password_algorithm: str | None
# - password_hash: str | None
# - password_inactivity_period: int | None
# - password_last_changed: date | None
# - password_max_age: int | None
# - password_min_age: int | None
# - password_salt: str | None
# - password_warning_period: int | None
# - user_comment: str | None
# - user_gid: int
# - user_groups: list[str]
# - user_home: str
# - user_login: str
# - user_shell: str
# - user_uid: int
# Define variable `result: list[dict]`
# with user data whose `UID` is greater or equal to 1000
# type: list[dict]
result = ...

