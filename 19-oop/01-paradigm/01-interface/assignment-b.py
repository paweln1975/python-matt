"""
* Assignment: OOP AbstractInterface Implement
* Complexity: easy
* Lines of code: 10 lines
* Time: 5 min

English:
    1. Define class `User` implementing `Account`
    2. Implement methods:
        a. `__init__()` sets fields
        b. `login()` returns 'User login'
        c. `logout()` returns 'User logout'
    3. Run doctests - all must succeed

Polish:
    1. Stwórz klasę `User` implementującą `Account`
    2. Zaimplementuj metody:
        a. `__init__` ustawia pola klasy
        b. `login()` zwraca 'User login'
        c. `logout()` zwraca 'User logout'
    3. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `vars(self).values()`

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isfunction

    >>> assert issubclass(User, Account)
    >>> assert hasattr(User, '__init__')
    >>> assert hasattr(User, 'login')
    >>> assert hasattr(User, 'logout')

    >>> assert isfunction(User.__init__)
    >>> assert isfunction(User.login)
    >>> assert isfunction(User.logout)

    >>> User.__annotations__  # doctest: +NORMALIZE_WHITESPACE
    {'username': <class 'str'>,
     'password': <class 'str'>}

    >>> mark = User(username='mwatney', password='Ares3')
    >>> mark.login()
    'User login'
    >>> mark.logout()
    'User logout'
"""

class Account:
    def __init__(self, username: str, password: str) -> None:
        raise NotImplementedError

    def login(self) -> str:
        raise NotImplementedError

    def logout(self) -> str:
        raise NotImplementedError


# Define class `User` implementing `Account`
# Implement methods:
#  a. `__init__()` sets fields
#  b. `login()` returns 'User login'
#  c. `logout()` returns 'User logout'
# type: type[Account]
class User:
    ...


