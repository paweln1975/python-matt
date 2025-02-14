"""
Name: Syntax Exception Embed
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
Terminal: `python -m doctest -v assignment-c.py`

Tests:
>>> import sys; sys.tracebacklimit = 0
>>> assert sys.version_info >= (3, 9), \
'Python 3.9+ required'

>>> from inspect import isclass

>>> isclass(User.DoesNotExist)
True
>>> issubclass(User.DoesNotExist, Exception)
True

Hints:
`class`
`pass`

"""

# %% SetUp

User: type
DoesNotExist: type[Exception]

# English
# 1. Modify `User` class
# 2. Add new exception `DoesNotExist` inside `User` class
# 3. Run doctests - all must succeed

# Polish
# 1. Zmodyfikuj klasę `User`
# 2. Dodaj nowy wyjątek `DoesNotExist` wewnątrz klasy `User`
# 3. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
class User:
    def __init__(self, username):
        self.username = username

    def __str__(self):
        return f"User('{self.username}')"