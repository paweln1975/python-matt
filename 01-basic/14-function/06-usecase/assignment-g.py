"""
* Assignment: Function Usecase EtcPasswdUsername
* Type: homework
* Complexity: medium
* Lines of code: 11 lines
* Time: 13 min

English:
    1. Create function `get_username`:
        a. parameter: `uid` (user ID)
        b. return: `username`
    2. Run doctests - all must succeed

Polish:
    1. Stwórz funkcję `get_username`:
        a. parametr: `uid` (user ID)
        b. zwraca: `username`
    2. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> get_username(0)
    'root'
    >>> get_username(1000)
    'mwatney'
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

# Create function `get_username`:
# - parameter: `uid` (user ID)
# - return: `username`
# type: Callable[[int], str]
def get_username(user_uid, newline='\n', comment='#', sep=':'):
    username = None
    lines = DATA.split(newline)
    for line in lines:
        if line.startswith(comment):
            continue

        user_info_line = line.split(sep)
        if user_info_line[2] == str(user_uid):
            username = user_info_line[0]
            break
    return username


