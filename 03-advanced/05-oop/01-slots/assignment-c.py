"""
* Assignment: OOP AttributeSlots Init
* Complexity: easy
* Lines of code: 3 lines
* Time: 2 min

English:
    1. Define class `User` with slots:
       a. `firstname: str`
       b. `lastname: str`
    2. Define `__init__()` method
    3. Do not use dataclass
    4. Run doctests - all must succeed

Polish:
    1. Zdefiniuj klasę `User` z slotami:
       a. `firstname: str`
       b. `lastname: str`
    2. Zdefiniuj metodę `__init__()`
    3. Nie używaj dataclass
    4. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
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

# Define class `User` with slots:
# - `firstname: str`
# - `lastname: str`
# Define `__init__()` method
# type: type[User]
class User:
    __slots__ = ('firstname', 'lastname')


