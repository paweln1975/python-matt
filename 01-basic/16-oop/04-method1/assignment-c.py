"""
* Assignment: OOP Method Parameters
* Type: class assignment
* Complexity: easy
* Lines of code: 4 lines
* Time: 3 min

English:
    1. Modify class `User`
    2. Modify method `login` in class `User`:
       a. Method takes `username` and `password` as arguments
       b. Method checks if username is 'mwatney' and password is 'Ares3'
       c. If true: method prints 'User login'
       d. If false: raise PermissionError with 'Invalid username or password'
    3. Run doctests - all must succeed

Polish:
    1. Zmodyfikuj klasę `User`
    2. Zmodyfikuj metodę `login` w klasie `User`:
        a. Metoda przyjmuje `username` i `password` jako argumenty
        b. Metoda sprawdza czy username to 'mwatney' i password to 'Ares3'
        c. Jeżeli prawda: metoda wypisuje 'User login'
        d. Jeżeli fałsz: rzuć PermissionError z 'Invalid username or password'
    3. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isclass, ismethod

    >>> assert isclass(User)
    >>> mark = User()
    >>> assert ismethod(mark.login)
    >>> assert ismethod(mark.logout)

    >>> mark.login('mwatney', 'Ares3')
    User login

    >>> mark.login(username='mwatney', password='Ares3')
    User login

    >>> mark.login(username='mwatney', password='invalid')
    Traceback (most recent call last):
    PermissionError: Invalid username or password

    >>> mark.login(username='invalid', password='Ares3')
    Traceback (most recent call last):
    PermissionError: Invalid username or password

    >>> mark.login()
    Traceback (most recent call last):
    TypeError: User.login() missing 2 required positional arguments: 'username' and 'password'

    >>> mark.logout()
    User logout
"""

# Modify method `login` in class `User`:
# - Method takes `username` and `password` as arguments
# - Method checks if username is 'mwatney' and password is 'Ares3'
# - If true: method prints 'User login'
# - If false: raise PermissionError with 'Invalid username or password'
class User:
    def login(self, username, password):
        if username == 'mwatney' and password == 'Ares3':
            print('User login')
        else:
            raise PermissionError('Invalid username or password')

    def logout(self):
        print('User logout')



