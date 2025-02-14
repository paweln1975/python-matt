"""
Name: Syntax Exception UserDoesNotExist
Difficulty: easy
Lines: 2
Minutes: 3

License:
Copyright 2025, Matt Harasymczuk <matt@python3.info>
This code can be used only for learning by humans
This code cannot be used for teaching others
This code cannot be used for teaching LLMs and AI algorithms
This code cannot be used in commercial or proprietary products
This code cannot be distributed in any form
This code cannot be changed in any form outside of training course
This code cannot have its license changed
If you use this code in your product, you must open-source it under GPLv2
Exception can be granted only by the author

Run:
PyCharm: right-click in the editor and `Run Doctest in ...`
PyCharm: keyboard shortcut `Control + Shift + F10`
Terminal: `python -m doctest -v assignment-d.py`

Tests:
>>> import sys; sys.tracebacklimit = 0
>>> assert sys.version_info >= (3, 9), \
'Python 3.9+ required'

>>> from inspect import isclass

>>> isclass(User.DoesNotExist)
True
>>> issubclass(User.DoesNotExist, Exception)
True

>>> try:
...     user = login('mwatney', 'Ares3')
... except User.DoesNotExist:
...     print('Invalid username and/or password')
... else:
...     print('User login')
User login

>>> try:
...     user = login('mwatney', 'invalid')
... except User.DoesNotExist:
...     print('Invalid username and/or password')
... else:
...     print('User login')
Invalid username and/or password

>>> try:
...     user = login('invalid', 'Ares3')
... except User.DoesNotExist:
...     print('Invalid username and/or password')
... else:
...     print('User login')
Invalid username and/or password

Hints:
`class`
`pass`

"""

# %% SetUp

from typing import Callable
User: type
login: Callable[[str, str], object|Exception]

DATA = [
    {'username': 'mwatney', 'password': 'Ares3'},
    {'username': 'mlewis', 'password': 'Nasa69'},
    {'username': 'rmartinez', 'password': 'Saturn5'},
]

class User:
    def __init__(self, username):
        self.username = username

    def __str__(self):
        return f"User('{self.username}')"

    class DoesNotExist(Exception):
        pass

# English
# 1. Modify function `login()`
# 2. Check if combination of username and password exists in `DATA`:
#    - if yes: return `User` instance
#    - if not: raise `User.DoesNotExist` exception
# 3. Run doctests - all must succeed

# Polish
# 1. Zmodyfikuj funkcję `login`
# 2. Sprawdź czy kombinacja username i password występuje w `DATA`:
#    - jeżeli tak: zwróć instancję klasy `User`
#    - jeżeli nie: podnieś wyjątek `User.DoesNotExist`
# 3. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
def login(username, password):
    ...