"""
* Assignment: OOP Init Parameters
* Type: class assignment
* Complexity: easy
* Lines of code: 3 lines
* Time: 2 min

English:
    1. Modify `User` class:
       a. Define initialization method with parameters `firstname` and `lastname`
       b. Method should set `firstname` attribute to the value of `firstname` parameter
       c. Method should set `lastname` attribute to the value of `lastname` parameter
    2. Non-functional requirements:
       a. Run doctests - all must succeed

Polish:
    1. Zmodyfikuj klasę `User`:
       a. Zdefiniuj metodę inicjalizacyjną z parametrami `firstname` i `lastname`
       b. Metoda powinna ustawić atrybut `firstname` na wartość parametru `firstname`
       c. Metoda powinna ustawić atrybut `lastname` na wartość parametru `lastname`
    2. Wymagania niefunkcjonalne:
       a. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isclass

    >>> assert isclass(User)
    >>> assert hasattr(User, '__init__')

    >>> mark = User('Mark', 'Watney')
    >>> vars(mark)
    {'firstname': 'Mark', 'lastname': 'Watney'}

    >>> mark = User(firstname='Melissa', lastname='Lewis')
    >>> vars(mark)
    {'firstname': 'Melissa', 'lastname': 'Lewis'}
"""

# Define initialization method with parameters `firstname` and `lastname`
# Method should set `firstname` attribute to the value of `firstname` parameter
# Method should set `lastname` attribute to the value of `lastname` parameter
class User:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname


