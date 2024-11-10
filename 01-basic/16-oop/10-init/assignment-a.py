"""
* Assignment: OOP Init Hello
* Type: class assignment
* Complexity: easy
* Lines of code: 2 lines
* Time: 2 min

English:
    1. Modify `User` class:
       a. Define initialization method
       b. Method should print 'hello' at object creation
    2. Non-functional requirements:
       a. Do not store any values in the class
       b. Run doctests - all must succeed

Polish:
    1. Zmodyfikuj klasę `User`:
       a. Zdefiniuj metodę inicjalizacyjną
       b. Metoda powinna wypisać 'hello' przy tworzeniu obiektu
    2. Wymagania niefunkcjonalne:
       a. Nie przechowuj żadnych wartości w klasie
       b. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isclass

    >>> assert isclass(User)
    >>> assert hasattr(User, '__init__')

    >>> result = User()
    hello
    >>> vars(result)
    {}
"""

# Define initialization method
# Method should print 'hello' at object creation
class User:
    firstname: str
    lastname: str

    def __init__(self):
        print('hello')

