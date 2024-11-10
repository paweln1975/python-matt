"""
* Assignment: Exception New UserDoesNotExist
* Type: homework
* Complexity: easy
* Lines of code: 2 lines
* Time: 3 min

English:
    1. Modify function `login()`
    2. Check if combination of username and password exists in `DATA`:
        a. if yes: return `User` instance
        b. if not: raise `User.DoesNotExist` exception
    3. Run doctests - all must succeed

Polish:
    1. Zmodyfikuj funkcję `login`
    2. Sprawdź czy kombinacja username i password występuje w `DATA`:
        a. jeżeli tak: zwróć instancję klasy `User`
        b. jeżeli nie: podnieś wyjątek `User.DoesNotExist`
    3. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `class`
    * `pass`

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isclass

    >>> isclass(User.DoesNotExist)
    True
    >>> issubclass(User.DoesNotExist, Exception)
    True

    >>> try:
    ...     user = login('mwatney', 'Ares3')
    ... except User.DoesNotExist:
    ...     print('Invalid username and/or password')
    ... else:
    ...     print('User login')
    User login

    >>> try:
    ...     user = login('mwatney', 'invalid')
    ... except User.DoesNotExist:
    ...     print('Invalid username and/or password')
    ... else:
    ...     print('User login')
    Invalid username and/or password

    >>> try:
    ...     user = login('invalid', 'Ares3')
    ... except User.DoesNotExist:
    ...     print('Invalid username and/or password')
    ... else:
    ...     print('User login')
    Invalid username and/or password
"""

DATA = [
    {'username': 'mwatney', 'password': 'Ares3'},
    {'username': 'mlewis', 'password': 'Nasa69'},
    {'username': 'rmartinez', 'password': 'Saturn5'},
]


class User:
    def __init__(self, username):
        self.username = username

    def __str__(self):
        return f"User('{self.username}')"

    class DoesNotExist(Exception):
        pass


# Modify function `login()`
# Check if combination of username and password exists in `DATA`:
# - if yes: return `User` instance
# - if not: raise `User.DoesNotExist` exception
# type: Callable[[str,str], User|Exception]
def login(username, password):
    ...


