"""
Name: Functional Reduce Chain
Difficulty: easy
Lines: 4
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

>>> from inspect import isfunction

>>> assert isfunction(even), \
'Object `even` must be a function'
>>> assert isfunction(square), \
'Object `square` must be a function'
>>> assert result is not Ellipsis, \
'Assign result to variable: `result`'
>>> assert type(result) is int, \
'Variable `result` has invalid type, should be int'

>>> result
147456

Hints:
`range()`
`map()`
`filter()`
`reduce()`

"""

# %% SetUp

from functools import reduce

result: int

def even(x):
    return x % 2 == 0

def square(x):
    return x ** 2

def product(x, y):
    return x * y

# English
# 1. Define `result` as a `range()` from 1 (inclusive) to 10 (exclusive)
# 2. Map `results` using `square` function
# 3. Filter `results` using `even` function
# 4. Reduce `results` using `product` function
# 5. Run doctests - all must succeed

# Polish
# 1. Zdefiniuj `result` jako `range()` od 1 (włącznie) do 10 (rozłącznie)
# 2. Przemapuj `result` używając funkcji `square`
# 3. Przefiltruj `result` używając funkcji `even`
# 4. Zredukuj `result` używając funkcji `product`
# 5. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
result = ...