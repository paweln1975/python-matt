"""
* Assignment: Exception New UserDoesNotExist
* Type: homework
* Complexity: easy
* Lines of code: 2 lines
* Time: 3 min

English:
    1. Modify `User` class
    2. Add new exception `DoesNotExist` inside `User` class
    3. Run doctests - all must succeed

Polish:
    1. Zmodyfikuj klasę `User`
    2. Dodaj nowy wyjątek `DoesNotExist` wewnątrz klasy `User`
    3. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `class`
    * `pass`

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isclass

    >>> isclass(User.DoesNotExist)
    True
    >>> issubclass(User.DoesNotExist, Exception)
    True
"""

# Modify `User` class
# Add new exception `DoesNotExist` inside `User` class
# type: type[User]
class User:
    def __init__(self, username):
        self.username = username

    def __str__(self):
        return f"User('{self.username}')"


