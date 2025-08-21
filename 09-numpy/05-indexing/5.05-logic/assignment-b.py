"""
Name: Numpy Logic Isin
Difficulty: easy
Lines: 1
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
Terminal: `python -m doctest -v assignment-b.py`

Tests:
>>> import sys; sys.tracebacklimit = 0
>>> assert sys.version_info >= (3, 9), \
'Python 3.9+ required'

>>> assert result is not Ellipsis, \
'Assign result to variable: `result`'
>>> assert type(result) is np.ndarray, \
'Variable `result` has invalid type, expected: np.ndarray'

>>> result
array([False, False,  True, False, False, False, False, False, False,
       False, False, False, False, False, False, False, False, False,
       False, False, False, False, False, False, False, False, False,
       False, False, False, False,  True, False, False, False, False,
       False, False, False, False, False,  True, False, False, False,
        True, False, False, False, False])

"""

# %% SetUp

import numpy as np

result: np.ndarray

np.random.seed(0)

a = np.random.randint(0, 100, size=50)
b = 2 ** np.arange(7)

# English
# 1. Check which elements from `a` are present in `b`
# 2. Result assign to `result`
# 3. Run doctests - all must succeed

# Polish
# 1. Sprawdź, które elementy z `a` są obecne w `b`
# 2. Wynik przypisz do `result`
# 3. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
result = np.isin(a, b)
