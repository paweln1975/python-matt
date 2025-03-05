"""
Name: OOP AttributeSlots Init
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
>>> assert sys.version_info >= (3, 10), \
'Python 3.10+ required'

>>> from dataclasses import is_dataclass

>>> class User:
...     __slots__ = ('firstname', 'lastname')
...
...     def __init__(self, firstname, lastname):
...         self.firstname = firstname
...         self.lastname = lastname
>>>
>>>
>>> mark = User(firstname='Mark', lastname='Watney')
>>> result = dump(mark)

>>> assert result is not Ellipsis, \
'Assign result to variable: `result`'
>>> assert type(result) is dict, \
'Result must be a type'
>>> assert len(result) == 2, \
'Result length must be 2'
>>> assert all(type(x) is str for x in result.keys()), \
'All keys in result must be a str'
>>> assert all(type(x) is str for x in result.values()), \
'All values in result must be a str'

>>> result
{'firstname': 'Mark', 'lastname': 'Watney'}

"""

# %% SetUp

from typing import Callable, Any
dump: Callable[[object], dict[str,Any]]

# English
# 1. Define function `dump(obj) -> dict` accepting instance with slots
# 2. Function should return similar output to `vars()`, i.e.:
#    {'firstname':'mwatney', 'lastname':'Ares3'}
# 3. Run doctests - all must succeed

# Polish
# 1. Zdefiniuj funkcję `dump(obj) -> dict` przyjmującą instancję ze slotami
# 2. Funkcja powinna zwracać podobny wynik do `vars()`, np:
#    {'firstname':'mwatney', 'lastname':'Ares3'}
# 3. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
def dump(obj) -> dict:
    return {k: getattr(obj, k) for k in obj.__slots__}

