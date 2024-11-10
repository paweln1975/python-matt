"""
* Assignment: OOP Init Fields
* Type: class assignment
* Complexity: easy
* Lines of code: 3 lines
* Time: 2 min

English:
    1. Modify `User` class:
       a. Define initialization method
       b. Method should set `firstname` attribute to 'Mark'
       c. Method should set `lastname` attribute to 'Watney'
    2. Non-functional requirements:
       a. Run doctests - all must succeed

Polish:
    1. Zmodyfikuj klasę `User`:
       a. Zdefiniuj metodę inicjalizacyjną
       b. Metoda powinna ustawić atrybut `firstname` na 'Mark'
       c. Metoda powinna ustawić atrybut `lastname` na 'Watney'
    2. Wymagania niefunkcjonalne:
       a. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isclass

    >>> assert isclass(User)
    >>> assert hasattr(User, '__init__')

    >>> result = User()
    >>> vars(result)
    {'firstname': 'Mark', 'lastname': 'Watney'}
"""

# Define initialization method
# Method should set `firstname` attribute to 'Mark'
# Method should set `lastname` attribute to 'Watney'
class User:
    firstname: str
    lastname: str
    age: int | float | None

    def __init__(self):
        self.firstname = 'Mark'
        self.lastname = 'Watney'



