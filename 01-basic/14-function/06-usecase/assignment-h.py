"""
* Assignment: Function Usecase EtcShadow
* Type: homework
* Complexity: medium
* Lines of code: 15 lines
* Time: 13 min

English:
    1. Create function `parse_passwd`:
        a. parameter: `username: str`
        b. return: user data record as a dict
    2. Run doctests - all must succeed

Polish:
    1. Stwórz funkcję `parse_passwd`:
        a. parametr: `username: str`
        b. zwraca: rekord danych użytkownika jako dict
    2. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * len()
    * int()
    * str.splitlines()
    * str.isspace()
    * str.startswith()
    * str.split()

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from pprint import pprint

    >>> pprint(parse_passwd('mwatney'), sort_dicts=False)
    {'user_login': 'mwatney',
     'user_password': 'x',
     'user_uid': 1000,
     'user_gid': 1000,
     'user_comment': 'Mark Watney',
     'user_home': '/home/mwatney',
     'user_shell': '/bin/bash'}
"""

DATA = """##
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
"""


# Create function `parse_passwd`:
# - parameter: `username: str`
# - return: user data record as a dict
# type: Callable[[int], str]
def parse_passwd(username):
    userecord = dict()
    lines = DATA.splitlines()
    for line in lines:
        if line.startswith('#'):
            continue

        user_info_line = line.split(':')
        if user_info_line[0] == str(username):
            userecord = dict(
                user_login=user_info_line[0],
                user_password=user_info_line[1],
                user_uid=int(user_info_line[2]),
                user_gid=int(user_info_line[3]),
                user_comment=user_info_line[4],
                user_home=user_info_line[5],
                user_shell=user_info_line[6],
            )
            break
    return userecord


