"""
* Assignment: OOP AbstractInterface Define
* Complexity: easy
* Lines of code: 9 lines
* Time: 5 min

English:
    1. Define interface `Account` with:
        a. Methods: `__init__()`, `login()`, `logout()`
        b. Init parameters: `username`, `password`
    2. All methods must raise exception `NotImplementedError`
    3. Run doctests - all must succeed

Polish:
    1. Zdefiniuj interfejs `Account` z:
        a. Metody: `__init__()`, `login()`, `logout()`
        b. Parametry init: `username`, `password`
    2. Wszystkie metody muszą podnosić wyjątek `NotImplementedError`
    3. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isfunction

    >>> assert hasattr(Account, '__init__')
    >>> assert hasattr(Account, 'login')
    >>> assert hasattr(Account, 'logout')

    >>> assert isfunction(Account.__init__)
    >>> assert isfunction(Account.login)
    >>> assert isfunction(Account.logout)

    >>> mark = Account(username='mwatney', password='Ares3')
    Traceback (most recent call last):
    NotImplementedError

    >>> Account.login(None)
    Traceback (most recent call last):
    NotImplementedError

    >>> Account.logout(None)
    Traceback (most recent call last):
    NotImplementedError
"""

# Define interface `Account` with:
#  a. Methods: `__init__()`, `login()`, `logout()`
#  b. Init parameters: `username`, `password`
# All methods must raise exception `NotImplementedError`
# type: type[Account]
...


