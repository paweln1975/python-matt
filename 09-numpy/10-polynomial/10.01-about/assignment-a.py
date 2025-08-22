"""
Name: Numpy Polyfit
Difficulty: easy
Lines: 4
Minutes: 8

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
array([ 0.25,  0.75, -1.5 , -2.  ])

"""

# %% SetUp

import numpy as np

result: np.ndarray

DATA = [
    ('x', 'y'),
    (-4.0, 0.0),
    (-3.0, 2.5),
    (-2.0, 2.0),
    (0.0, -2.0),
    (2.0, 0.0),
    (3.0, 7.0),
]

# English
# 1. Given are points coordinates in Cartesian system
# 2. Separate first row (header) from data
# 3. Calculate coefficients of best approximating polynomial of 3rd degree
# 4. Run doctests - all must succeed

# Polish
# 1. Dane są koordynaty punktów w układzie kartezjańskim
# 2. Odseparuj pierwszy wiersz (nagłówek) do danych
# 3. Oblicz współczynniki najlepiej dopasowanego wielomianu 3 stopnia
# 4. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
data = np.array(DATA[1:])
x = data[:, 0]
y = data[:, 1]
result = np.polyfit(x, y, deg=3)

