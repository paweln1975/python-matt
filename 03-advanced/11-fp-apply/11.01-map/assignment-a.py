"""
Name: Functional Map Cube
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
Terminal: `python -m doctest -v assignment-a.py`

Tests:
>>> import sys; sys.tracebacklimit = 0
>>> assert sys.version_info >= (3, 9), \
'Python 3.9+ required'

>>> from inspect import isfunction

>>> assert isfunction(cube), \
'Object `cube` must be a function'
>>> assert result is not Ellipsis, \
'Assign result to variable: `result`'

>>> assert type(result) is map, \
'Variable `result` has invalid type, should be map'

>>> result = tuple(result)
>>> assert type(result) is tuple, \
'Evaluated `result` has invalid type, should be tuple'

>>> assert all(type(x) is int for x in result), \
'All rows in `result` should be int'

>>> result
(1, 8, 27, 64)

"""

# %% SetUp

result: map

DATA = (1, 2, 3, 4)

def cube(x):
    return x ** 3

# English
# 1. Use `map()` to apply function `cube()` to DATA
# 2. Define `result: map` with result
# 3. Run doctests - all must succeed

# Polish
# 1. Użyj `map()` aby zaaplikować funkcję `cube()` do DATA
# 2. Zdefiniuj `result: map` z wynikiem
# 3. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
result = map(cube, DATA)