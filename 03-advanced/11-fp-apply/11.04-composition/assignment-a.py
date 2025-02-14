"""
Name: Functional Composition Sum
Difficulty: easy
Lines: 1
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
Terminal: `python -m doctest -v assignment-a.py`

Tests:
>>> import sys; sys.tracebacklimit = 0
>>> assert sys.version_info >= (3, 9), \
'Python 3.9+ required'

>>> from inspect import isfunction

>>> assert isfunction(even), \
'Object `even` must be a function'
>>> assert result is not Ellipsis, \
'Assign result to variable: `result`'
>>> assert type(result) is int, \
'Variable `result` has invalid type, should be int'

>>> result
6

Hints:
`filter()`
`sum()`

"""

# %% SetUp

result: int

def even(x):
    return x % 2 == 0

NUMBERS = (1, 2, 3, 4)
DATA = filter(even, NUMBERS)

# English
# 1. Define `result: int` with a sum of elements in `DATA`
# 2. Run doctests - all must succeed

# Polish
# 1. Zdefiniuj `result: int` z sumą elementów w `DATA`
# 2. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
result = ...