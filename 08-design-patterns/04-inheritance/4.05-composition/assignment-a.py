"""
Name: Inheritance Composition A
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
Terminal: `python -m doctest -v assignment-a.py`

Tests:
>>> import sys; sys.tracebacklimit = 0
>>> assert sys.version_info >= (3, 9), \
'Python 3.9+ required'

>>> from inspect import isclass

>>> assert isclass(UserPermissions)
>>> assert isclass(AdminPermissions)
>>> assert isclass(Account)

>>> result = Account()
Traceback (most recent call last):
TypeError: Account.__init__() missing 1 required positional argument: 'permissions'

>>> result = Account(UserPermissions())
>>> assert hasattr(result, 'permissions'), \
'Account instance must have `permissions` attribute'
>>> assert type(result.permissions) is UserPermissions

>>> result = Account(AdminPermissions())
>>> assert hasattr(result, 'permissions'), \
'Account instance must have `permissions` attribute'
>>> assert type(result.permissions) is AdminPermissions

"""

# %% SetUp

UserPermissions: type
AdminPermissions: type
Account: type

# English
# 1. Define class `UserPermissions`
# 2. Define class `AdminPermissions`
# 3. Compose `Account` from `UserPermissions`, `AdminPermissions`
# 4. Use composition
# 5. Run doctests - all must succeed

# Polish
# 1. Zdefiniuj klasę `UserPermissions`
# 2. Zdefiniuj klasę `AdminPermissions`
# 3. Skomponuj `Account` z klas `UserPermissions`, `AdminPermissions`
# 4. Użyj kompozycji
# 5. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
