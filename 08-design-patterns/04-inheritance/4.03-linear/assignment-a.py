"""
Name: Inheritance Linear A
Difficulty: easy
Lines: 6
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
Terminal: `python -m doctest -v assignment-a.py`

Tests:
>>> import sys; sys.tracebacklimit = 0
>>> assert sys.version_info >= (3, 9), \
'Python 3.9+ required'

>>> from inspect import isclass

>>> assert isclass(Account)
>>> assert isclass(User)
>>> assert isclass(Admin)

>>> assert issubclass(User, Account)
>>> assert issubclass(Admin, User)
>>> assert issubclass(Admin, Account)

>>> assert len(Account.__subclasses__()) == 1
>>> assert len(User.__subclasses__()) == 1
>>> assert len(Admin.__subclasses__()) == 0

"""

# %% SetUp

Account: type
User: type
Admin: type

# English
# 1. Define class `Account`
# 2. Define class `User` inheriting from `Account`
# 3. Define class `Admin` inheriting from `User`
# 4. Use linear inheritance
# 5. Run doctests - all must succeed

# Polish
# 1. Zdefiniuj klasę `Account`
# 2. Zdefiniuj klasę `User` dziedziczącą po `Account`
# 3. Zdefiniuj klasę `Admin` dziedziczącą po `User`
# 4. Użyj liniowego dziedziczenia
# 5. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
