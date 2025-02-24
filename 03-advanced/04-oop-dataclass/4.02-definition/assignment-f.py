"""
Name: Dataclass Definition ClassVar
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
Terminal: `python -m doctest -v assignment-f.py`

Tests:
>>> import sys; sys.tracebacklimit = 0
>>> assert sys.version_info >= (3, 9), \
'Python 3.9+ required'

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

# %% SetUp

from typing import ClassVar
from dataclasses import dataclass

result: type

# English
# 1. Define class User with:
#    - instance variable `age: int` (no default value)
#    - class variable `AGE_MIN: int` with default value `18`
#    - class variable `AGE_MAX: int` with default value `65`
# 2. Use `dataclass`
# 3. Use `typing`
# 4. Run doctests - all must succeed

# Polish
# 1. Zdefiniuj klasę User z polami klasowymi:
#    - zmienną instancji `age: int` (bez domyślnej wartości)
#    - zmienną klasy `AGE_MIN: int` z domyślną wartością `18`
#    - zmienną klasy `AGE_MAX: int` z domyślną wartością `65`
# 2. Użyj `dataclass`
# 3. Użyj `typing`
# 4. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
@dataclass
class User:
    firstname: str
    lastname: str
    age: int
    AGE_MIN: ClassVar[int] = 18
    AGE_MAX: ClassVar[int] = 65
