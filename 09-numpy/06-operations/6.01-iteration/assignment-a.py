"""
Name: Numpy Iteration
Difficulty: easy
Lines: 3
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
Terminal: `python -m doctest -v assignment-a.py`

Tests:
>>> import sys; sys.tracebacklimit = 0
>>> assert sys.version_info >= (3, 9), \
'Python 3.9+ required'

>>> assert result is not Ellipsis, \
'Assign result to variable: `result`'
>>> assert type(result) is list, \
'Variable `result` has invalid type, expected: list'
>>> assert all(type(x) is np.int64 for x in result), \
'All values in `result` must be type int'

>>> result
[np.int64(2), np.int64(4), np.int64(6), np.int64(8)]

Hints:
`number % 2 == 0`

"""

# %% SetUp

import numpy as np

result: list[int]

DATA = np.array([[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]])

# English
# 1. Use `for` to iterate over `DATA`
# 2. Define `result: list[int]` with even numbers from `DATA`
# 3. Run doctests - all must succeed

# Polish
# 1. Używając `for` iteruj po `DATA`
# 2. Zdefiniuj `result: list[int]` z liczbami parzystymi z `DATA`
# 3. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
result = [value for value in DATA.flatten() if value % 2 == 0]

arr = np.arange(10)
bool_arr = arr % 2 == 0
print(bool_arr)
