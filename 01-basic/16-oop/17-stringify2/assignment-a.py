"""
* Assignment: OOP Stringify Repr
* Type: class assignment
* Complexity: easy
* Lines of code: 3 lines
* Time: 5 min

English:
    1. Use class `User`
    2. Define `__repr__` method for representing object
    3. Method should display class name, attributes and their values
       example: `User(firstname='Mark', lastname='Watney')`
    4. Run doctests - all must succeed

Polish:
    1. Użyj klasy `User`
    2. Zdefiniuj metodę `__repr__` do reprezentowania obiektu
    3. Metoda powinna wyświetlać nazwę klasy, atrybuty i ich wartości
       przykład: `User(firstname='Mark', lastname='Watney')`
    4. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from pprint import pprint
    >>> from inspect import isclass

    >>> assert isclass(User)
    >>> assert hasattr(User, '__init__')
    >>> assert hasattr(User, '__repr__')

    >>> mark = User('Mark', 'Watney')
    >>> result = repr(mark)
    >>> pprint(result)
    "User(firstname='Mark', lastname='Watney')"
"""

# Define `__repr__` method for representing object
# Method should display class name, attributes and their values
# example: `User(firstname='Mark', lastname='Watney')`
class User:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def __repr__(self):
        return f"User(firstname='{self.firstname}', lastname='{self.lastname}')"
