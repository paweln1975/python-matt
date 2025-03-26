"""
Name: Functional Map DateFormats
Difficulty: easy
Lines: 1
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

>>> assert result is not Ellipsis, \
'Assign result to variable: `result`'
>>> assert type(result) is map, \
'Variable `result` has invalid type, must be a map'
>>> result = list(result)
>>> assert type(result) is list, \
'Variable `result` has invalid type, must be a list'
>>> assert all(type(element) is datetime for element in result), \
'All elements in `result` must be a datetime'

>>> result  # doctest: +NORMALIZE_WHITESPACE
[datetime.datetime(1957, 10, 4, 19, 28, 34),
 datetime.datetime(1961, 4, 12, 6, 7),
 datetime.datetime(1969, 7, 21, 2, 56, 15)]

Hints:
`for ... in`
nested `try ... except`
`FORMATS = []`
`for fmt in FORMATS`
helper function
24-hour clock
`map(func, iterable1, iterable1)`

"""

# %% SetUp

from datetime import datetime

result: map

DATA = [
    'Oct 4, 1957 19:28:34',  # Sputnik launch (first satellite in space)
    'April 12, 1961 6:07',  # Gagarin launch (first human in space)
    'July 21, 1969 2:56:15',  # Armstrong first step on the Moon
]

FORMATS = [
    '%b %d, %Y %H:%M:%S',
    '%B %d, %Y %H:%M',
    '%B %d, %Y %H:%M:%S',
]

# English
# 1. Define `result: map` with parsed `DATA` dates
# 2. Use `map()`
# 3. Run doctests - all must succeed

# Polish
# 1. Zdefiniuj `result: map` ze sparsowanymi datami `DATA`
# 2. Użyj `map()`
# 3. Uruchom doctesty - wszystkie muszą się powieść

# %% Result

result = map(datetime.strptime, DATA, FORMATS)
