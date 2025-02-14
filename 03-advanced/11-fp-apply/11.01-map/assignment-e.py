"""
Name: Functional Map CSV
Difficulty: easy
Lines: 5
Minutes: 5

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
Terminal: `python -m doctest -v assignment-e.py`

Tests:
>>> import sys; sys.tracebacklimit = 0
>>> assert sys.version_info >= (3, 9), \
'Python 3.9+ required'

>>> assert result is not Ellipsis, \
'Assign result to variable: `result`'
>>> assert type(result) is map, \
'Variable `result` has invalid type, must be a map'

>>> result = list(result)  # expand map object
>>> assert type(result) is list, \
'Variable `result` has invalid type, should be list'
>>> assert all(type(x) is tuple for x in result), \
'All rows in `result` should be tuple'

>>> result  # doctest: +NORMALIZE_WHITESPACE
[(5.8, 2.7, 5.1, 1.9, 'virginica'),
 (5.1, 3.5, 1.4, 0.2, 'setosa'),
 (5.7, 2.8, 4.1, 1.3, 'versicolor')]

Hints:
`str.strip()`
`str.split()`
`map()`
`list() + list()`
`list.append()`
`tuple()`

"""

# %% SetUp

result: map

DATA = """5.8,2.7,5.1,1.9,virginica
5.1,3.5,1.4,0.2,setosa
5.7,2.8,4.1,1.3,versicolor"""

# English
# 1. Convert `DATA` to `result: map`
# 2. Convert numeric values to `float`
# 3. Run doctests - all must succeed

# Polish
# 1. Przekonwertuj `DATA` to `result: map`
# 2. Przekonwertuj wartości numeryczne do `float`
# 3. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
result = ...