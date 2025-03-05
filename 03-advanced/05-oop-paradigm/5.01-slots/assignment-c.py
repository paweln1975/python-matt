"""
Name: OOP AttributeSlots Init
Difficulty: easy
Lines: 3
Minutes: 2

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
>>> assert sys.version_info >= (3, 10), \
'Python 3.10+ required'

>>> from dataclasses import is_dataclass

>>> assert hasattr(User, '__slots__')
>>> assert 'firstname' in User.__slots__
>>> assert 'lastname' in User.__slots__

>>> assert User is not Ellipsis, \
'Assign result to variable: `User`'
>>> assert type(User) is type, \
'Result must be a type'
>>> assert not is_dataclass(User), \
'Class User cannot be dataclass'

>>> result = User(firstname='Mark', lastname='Watney')
>>> assert not hasattr(result, '__dict__')
>>> assert not hasattr(result, '__weakref__')

"""

# %% SetUp

# English
# 1. Define class `User` with slots:
#    - `firstname: str`
#    - `lastname: str`
# 2. Define `__init__()` method
# 3. Do not use dataclass
# 4. Run doctests - all must succeed

# Polish
# 1. Zdefiniuj klasę `User` z slotami:
#    - `firstname: str`
#    - `lastname: str`
# 2. Zdefiniuj metodę `__init__()`
# 3. Nie używaj dataclass
# 4. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
class User:
    __slots__ = ('firstname', 'lastname')

    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
