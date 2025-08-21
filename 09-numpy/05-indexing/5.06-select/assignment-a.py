"""
Name: Numpy Select Isin
Difficulty: easy
Lines: 6
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
>>> assert type(result) is np.ndarray, \
'Variable `result` has invalid type, expected: np.ndarray'

>>> result
array([1024, 1024, 1024, 1024, 1024, 1024,  512,  512,  512,  512,  256,
        256,  256,  256,  256,  128,  128,  128,  128,  128,   64,   32,
         32,   32,   32,   32,   16,   16,   16,   16,   16,   16,    8,
          8,    4,    2,    2,    2,    2,    2])

Hints:
`np.isin(a, b)`
`np.flip(a)`

"""

# %% SetUp

import numpy as np

result: np.ndarray

np.random.seed(0)

# English
# 1. Set random seed to 0
# 2. Generate `a: np.ndarray` of size 50x50
# 3. `a` must contains random integers from 0 to 1024 inclusive
# 4. Create `result: np.ndarray` with elements selected from `a` which are power of two
# 5. Sort `result` in descending order
# 6. Run doctests - all must succeed

# Polish
# 1. Ustaw ziarno losowości na 0
# 2. Wygeneruj `a: np.ndarray` rozmiaru 50x50
# 3. `a` musi zawierać losowe liczby całkowite z zakresu od 0 do 1024 włącznie
# 4. Stwórz `result: np.ndarray` z elementami wybranymi z `a`, które są potęgami dwójki
# 5. Posortuj `result` w kolejności malejącej
# 6. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
a = np.random.randint(0, 1025, size=(50, 50))
b = 2 ** np.arange(11)
mask = np.isin(a, b)
result = a[mask]
result.sort()
result = np.flip(result).astype(np.int64)
