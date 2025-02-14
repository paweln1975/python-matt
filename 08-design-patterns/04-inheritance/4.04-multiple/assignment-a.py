"""
Name: Inheritance Multiple A
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
>>> assert isclass(UserPermissions)
>>> assert isclass(AdminPermissions)

>>> assert issubclass(Account, Account)
>>> assert issubclass(Account, UserPermissions)
>>> assert issubclass(Account, AdminPermissions)

>>> assert len(Account.__subclasses__()) == 0
>>> assert len(UserPermissions.__subclasses__()) == 1
>>> assert len(AdminPermissions.__subclasses__()) == 1

"""

# %% SetUp

UserPermissions: type
AdminPermissions: type
Account: type

# English
# 1. Define class `UserPermissions`
# 2. Define class `AdminPermissions`
# 3. Compose `Account` from `UserPermissions`, `AdminPermissions`
# 4. Use mixins classes
# 5. Run doctests - all must succeed

# Polish
# 1. Zdefiniuj klasę `UserPermissions`
# 2. Zdefiniuj klasę `AdminPermissions`
# 3. Skomponuj `Account` z klas `UserPermissions`, `AdminPermissions`
# 4. Użyj klas domieszkowych (mixin)
# 5. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
