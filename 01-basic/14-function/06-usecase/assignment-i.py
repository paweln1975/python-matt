"""
* Assignment: Function Scope EtcShadow
* Type: homework
* Complexity: medium
* Lines of code: 35 lines
* Time: 34 min

English:
    1. Create function `parse_shadow`:
        a. parameter: `username: str`
        b. return: user password record as a dict
    2. Split password field by `$`:
        a. algorithm (algorithm number, e.g. `6` is SHA-512)
        b. salt (value added to password)
        c. password hash (encoded password)
    3. Run doctests - all must succeed

Polish:
    1. Stwórz funkcję `parse_shadow`:
        a. parametr: `username: str`
        b. zwraca: dane hasła użytkownika jako dict
    2. Podziel pole hasła po znaku `$`:
        a. algorytm (nr algorytmu, np. `6` to SHA-512)
        b. sól (wartość dodawana do hasła)
        c. hash hasła (zakodowane hasło)
    3. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * len()
    * list[...]
    * ... in tuple
    * str.splitlines()
    * str.isspace()
    * str.startswith()
    * str.split()
    * dict.get(...)

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from pprint import pprint

    >>> result = parse_shadow('mwatney')
    >>> pprint(result, sort_dicts=True)
    {'account_expiration_date': '',
     'account_locked': False,
     'login': 'mwatney',
     'password_algorithm': 'SHA-512',
     'password_hash': 'bXGOh7dIfOWpUb/Tuqr7yQVCqL3UkrJns9.7msfvMg4ZO/PsFC5Tbt32PXAw9qRFEBs1254aLimFeNM8YsYOv.',
     'password_inactivity_period': '',
     'password_last_changed': '16550',
     'password_max_age': '',
     'password_min_age': '',
     'password_salt': '5H0QpwprRiJQR19Y',
     'password_warning_period': '',
     'reserved': ''}

    >>> result = parse_shadow('mlewis')
    >>> pprint(result, sort_dicts=True)
    {'account_expiration_date': '',
     'account_locked': False,
     'login': 'mlewis',
     'password_algorithm': 'SHA-512',
     'password_hash': 'tgfvvFWJJ5FKmoXiP5rXWOjwoEBOEoAuBi3EphRbJqqjWYvhEM2wa67L9XgQ7W591FxUNklkDIQsk4kijuhE50',
     'password_inactivity_period': '',
     'password_last_changed': '16632',
     'password_max_age': '99999',
     'password_min_age': '0',
     'password_salt': 'P9zn0KwR',
     'password_warning_period': '7',
     'reserved': ''}
"""

DATA = """##
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
"""

ALGORITHMS = {
    '1': 'MD5',
    '2a': 'Blowfish',
    '2y': 'Blowfish',
    '5': 'SHA-256',
    '6': 'SHA-512',
}


# Create function `parse_shadow`:
# - parameter: `username: str`
# - return: user password record as a dict
#
# Split password field by `$`:
# - algorithm (algorithm number, e.g. `6` is SHA-512)
# - salt (value added to password)
# - password hash (encoded password)
#
# type: Callable[[int], str]
def parse_shadow(username):
    password_record = dict()
    account_locked = False
    password_special_chars = [' ', '*', '!', '!']
    lines = DATA.splitlines()
    for line in lines:
        if line.startswith('#'):
            continue

        user_info_line = line.split(':')
        if user_info_line[0] == str(username):
            password_record = user_info_line[1]
            if password_record[0] in password_special_chars:
                account_locked = True
            else:
                password_data = password_record.split('$')
                password_algorithm = ALGORITHMS[str(password_data[1])]
                password_salt = password_data[2]
                password_hash = password_data[3]

            password_record = dict(
                account_expiration_date = user_info_line[7],
                account_locked = account_locked,
                login=user_info_line[0],
                password_algorithm=password_algorithm,
                password_hash=password_hash,
                password_inactivity_period=user_info_line[8],
                password_last_changed=user_info_line[2],
                password_min_age=user_info_line[3],
                password_max_age=user_info_line[4],
                password_salt=password_salt,
                password_warning_period=user_info_line[5],
                reserved = ''
            )
            break
    return password_record


