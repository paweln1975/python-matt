"""
Name: Functional Scope Global
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

>>> from inspect import isfunction, signature

>>> assert type(SELECT) is set, \
'Define in global scope `SELECT: set[str]`'

>>> assert 'setosa' in SELECT, \
'Value setosa must be in SELECT'

>>> assert 'versicolor' in SELECT, \
'Value versicolor must be in SELECT'

>>> assert isfunction(sumselected), \
'Define function `sumselected(values, species)`'

>>> signature(sumselected)
<Signature (values, species)>

>>> sum(sumselected(X,y) for *X, y in DATA[1:])
49.1

"""

# %% SetUp

from typing import Callable
sumselected: Callable[[list[float], str], float]

DATA = [
    ('sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species'),
    (5.8, 2.7, 5.1, 1.9, 'virginica'),
    (5.1, 3.5, 1.4, 0.2, 'setosa'),
    (5.7, 2.8, 4.1, 1.3, 'versicolor'),
    (6.3, 2.9, 5.6, 1.8, 'virginica'),
    (6.4, 3.2, 4.5, 1.5, 'versicolor'),
    (4.7, 3.2, 1.3, 0.2, 'setosa'),
]

SELECT = {'setosa', 'versicolor'}

# English
# 1. Define function `sumselected(values, species)`
# 2. Function sums `values`, only when `species` is in `SELECT`
# 3. When `species` is not in `select` return `0` (zero)
# 4. Run doctests - all must succeed

# Polish
# 1. Zdefiniuj funkcję `sumselected(values, species)`
# 2. Funkcja sumuje `values`, tylko gdy `species` jest w `SELECT`
# 3. Gdy `species` nie występuje w `select` zwróć `0` (zero)
# 4. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
def sumselected():
    ...