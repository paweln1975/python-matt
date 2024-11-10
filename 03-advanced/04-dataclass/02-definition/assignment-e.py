"""
* Assignment: Dataclass Definition ClassVar
* Complexity: easy
* Lines of code: 3 lines
* Time: 2 min

English:
    1. Define class User with:
        a. instance variable `age: int` (no default value)
        b. class variable `AGE_MIN: int` with default value `18`
        c. class variable `AGE_MAX: int` with default value `65`
    2. Use `dataclass`
    3. Use `typing`
    4. Run doctests - all must succeed

Polish:
    1. Zdefiniuj klasę User z polami klasowymi:
        a. zmienną instancji `age: int` (bez domyślnej wartości)
        b. zmienną klasy `AGE_MIN: int` z domyślną wartością `18`
        c. zmienną klasy `AGE_MAX: int` z domyślną wartością `65`
    2. Użyj `dataclass`
    3. Użyj `typing`
    4. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isclass
    >>> from dataclasses import _FIELD_CLASSVAR

    >>> assert isclass(User)
    >>> assert hasattr(User, '__annotations__')
    >>> assert hasattr(User, '__dataclass_fields__')

    >>> fields = User.__dataclass_fields__
    >>> assert 'age' in fields
    >>> assert 'AGE_MIN' in fields
    >>> assert 'AGE_MAX' in fields

    >>> assert fields['AGE_MIN']._field_type is _FIELD_CLASSVAR
    >>> assert fields['AGE_MAX']._field_type is _FIELD_CLASSVAR
"""
from dataclasses import dataclass
from typing import ClassVar


# Define class User with class variables:
# - instance variable `age: int` (no default value)
# - class variable `AGE_MIN: int` with default value `18`
# - class variable `AGE_MAX: int` with default value `65`
# Use `dataclass` and `typing`
# type: type[User]
@dataclass
class User:
    firstname: str
    lastname: str
    ...


