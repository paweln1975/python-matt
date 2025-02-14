"""
Name: Django Setup Version
Difficulty: easy
Lines: 2
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
Terminal: `python -m doctest -v assignment-b.py`

Tests:
>>> import sys; sys.tracebacklimit = 0
>>> assert sys.version_info >= (3, 10), \
'Python 3.10+ required'

>>> from pprint import pprint

>>> assert type(result) is not Ellipsis, \
'Assign result to variable `result`'
>>> assert type(result) is str, \
'Variable `result` has invalid type, should be str'

>>> result.startswith('5.1')
True

"""

# %% SetUp

result: str

# English
# 1. Define variable `result: str` with Django version
# 2. Version has to be in format `X.Y.Z`
# 3. Run doctests - all must succeed

# Polish
# 1. Zdefiniuj zmienną `result: str` z wersją Django
# 2. Wersja musi być w formacie `X.Y.Z`
# 3. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
result = ...