"""
* Assignment: OOP Method Two
* Type: class assignment
* Complexity: easy
* Lines of code: 2 lines
* Time: 2 min

English:
    1. Modify class `User`
    2. Define method `logout` in class `User`
    3. Method prints 'User logout'
    3. Run doctests - all must succeed

Polish:
    1. Zmodyfikuj klasę `User`
    2. Zdefiniuj metodę `logout` w klasie `User`
    3. Metoda wypisuje 'User logout'
    4. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isclass, ismethod

    >>> assert isclass(User)
    >>> mark = User()
    >>> assert ismethod(mark.login)
    >>> assert ismethod(mark.logout)

    >>> mark.login()
    User login

    >>> mark.logout()
    User logout
"""

# Define method `logout` in class `User`
# Method prints 'User logout'
class User:
    def login(self):
        print('User login')

    def logout(self):
        print('User logout')


