"""
* Assignment: OOP State EditProfile
* Type: class assignment
* Complexity: easy
* Lines of code: 5 lines
* Time: 5 min

English:
    1. Modify class `User`
    2. Add method `edit_profile()`:
       a. Arguments: `firstname`, `lastname`
       b. Method checks if user is authenticated
       c. If so, set instance fields values
       d. If not, raise `PermissionError` with message `User is not authenticated`
    3. Run doctests - all must succeed

Polish:
    1. Zmodyfikuj klasę `User`
    2. Dodaj metodę `edit_profile()`:
       a. Argumenty: `firstname`, `lastname`
       b. Metoda sprawdza czy użytkownik jest uwierzytelniony
       c. Jeśli tak, to ustawia wartości pól instancji
       d. Jeśli nie, to rzuć wyjątek `PermissionError`
          z komunikatem `User is not authenticated`
    3. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isclass, ismethod, signature
    >>> assert isclass(User)
    >>> assert hasattr(User, '__init__')

    >>> mark = User('Mark', 'Watney')
    >>> assert ismethod(mark.login)
    >>> assert ismethod(mark.logout)
    >>> assert ismethod(mark.is_authenticated)
    >>> assert ismethod(mark.edit_profile)

    >>> mark.edit_profile('Melisa', 'Lewis')
    Traceback (most recent call last):
    PermissionError: User is not authenticated
"""

# Add method `edit_profile()`:
# a. Arguments: `firstname`, `lastname`
# b. Method checks if user is authenticated
# c. If so, set instance fields values
# d. If not, raise `PermissionError` with message `User is not authenticated`
# type: type
class User:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self._authenticated = False

    def login(self):
        self._authenticated = True

    def logout(self):
        self._authenticated = False

    def is_authenticated(self):
        return self._authenticated

    def edit_profile(self, firstname, lastname):
        if self._authenticated:
            self.firstname = firstname
            self.lastname = lastname
        else:
            raise PermissionError('User is not authenticated')
