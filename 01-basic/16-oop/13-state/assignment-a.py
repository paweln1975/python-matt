"""
* Assignment: OOP State Auth
* Type: class assignment
* Complexity: easy
* Lines of code: 10 lines
* Time: 8 min

English:
    1. Modify class `User`
    2. Add method `__init__`:
         a. Arguments: `firstname`, `lastname`
         b. Method should set arguments as instance fields
         c. Method should set field `_authenticated` to `False`
         d. It's not an error, field name starts with underscore `_`
    3. Add method `login`, setting field `_authenticated` to `True`
    4. Add method `logout`, setting field `_authenticated` to `False`
    5. Add method `is_authenticated`, returning value of field `_authenticated`
    6. Run doctests - all must succeed

Polish:
    1. Zmodyfikuj klasę `User`
    2. Dodaj metodę `__init__`:
       a. Argumenty: `firstname`, `lastname`
       b. Metoda ma ustawiać argumenty jako pola instancji
       c. Metoda ma ustawiać pole `_authenticated` na `False`
       d. To nie błąd, nazwa pola zaczyna się od podkreślenia `_`
    3. Dodaj metodę `login`, ustawiającą pole `_authenticated` na `True`
    4. Dodaj metodę `logout`, ustawiającą pole `_authenticated` na `False`
    5. Dodaj metodę `is_authenticated`, zwracającą wartość pola `_authenticated`
    6. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isclass, ismethod
    >>> assert isclass(User)
    >>> assert hasattr(User, '__init__')
    >>> mark = User('Mark', 'Watney')
    >>> assert ismethod(mark.login)
    >>> assert ismethod(mark.logout)
    >>> assert ismethod(mark.is_authenticated)
"""

# Add method `__init__`:
# - Arguments: `firstname`, `lastname`
# - Method should set arguments as instance fields
# - Method should set field `_authenticated` to `False`
# - It's not an error, field name starts with underscore `_`
# Add method `login`, setting field `_authenticated` to `True`
# Add method `logout`, setting field `_authenticated` to `False`
# Add method `is_authenticated`, returning value of field `_authenticated`
# type: type
class User:
    def __init__(self, firstname, lastname):
        self.lastname = lastname
        self.firstname = firstname
        self._authenticated = False
    def login(self):
        self._authenticated = True

    def logout(self):
        self._authenticated = False

    def is_authenticated(self):
        return self._authenticated
