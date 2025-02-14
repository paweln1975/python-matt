"""
Name: Numpy Loadtext
Difficulty: easy
Lines: 4
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

>>> assert species is not Ellipsis, \
'Assign result to variable: `species`'
>>> assert labels is not Ellipsis, \
'Assign result to variable: `labels`'
>>> assert features is not Ellipsis, \
'Assign result to variable: `features`'

>>> assert type(species) is np.ndarray, \
'Variable `species` has invalid type, expected: np.ndarray'
>>> assert type(features) is np.ndarray, \
'Variable `features` has invalid type, expected: np.ndarray'
>>> assert type(labels) is np.ndarray, \
'Variable `labels` has invalid type, expected: np.ndarray'

>>> assert species.dtype == np.dtype('<U10'), \
'Variable `species` has invalid type, expected: str'
>>> assert features.dtype is np.dtype('float64'), \
'Variable `features` has invalid type, expected: float'
>>> assert labels.dtype is np.dtype('int64'), \
'Variable `labels` has invalid type, expected: int'

>>> assert len(species) == 3, \
'Variable `species` length should be 3'
>>> assert len(features) == 151, \
'Variable `features` length should be 151'
>>> assert len(labels) == 151, \
'Variable `labels` length should be 151'

>>> species
array(['setosa', 'versicolor', 'virginica'], dtype='<U10')

>>> features[:3]
array([[5.4, 3.9, 1.3, 0.4],
       [5.9, 3. , 5.1, 1.8],
       [6. , 3.4, 4.5, 1.6]])

>>> features[-3:]
array([[4.9, 2.5, 4.5, 1.7],
       [6.3, 2.8, 5.1, 1.5],
       [6.8, 3.2, 5.9, 2.3]])

>>> labels
array([0, 2, 1, 2, 1, 0, 1, 1, 0, 2, 2, 0, 0, 2, 2, 1, 2, 2, 2, 1, 0, 1,
       1, 0, 0, 0, 2, 2, 0, 2, 2, 0, 1, 1, 2, 2, 0, 1, 2, 1, 1, 1, 2, 2,
       0, 1, 1, 1, 1, 1, 2, 0, 2, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 2, 0, 0,
       0, 0, 0, 0, 1, 0, 2, 0, 0, 1, 1, 2, 2, 1, 0, 2, 1, 0, 1, 0, 2, 1,
       0, 2, 0, 2, 1, 0, 2, 1, 1, 0, 0, 1, 2, 2, 2, 1, 0, 1, 1, 1, 2, 2,
       0, 2, 2, 0, 2, 1, 2, 0, 0, 1, 0, 2, 0, 2, 1, 2, 2, 2, 1, 0, 2, 1,
       0, 0, 2, 0, 2, 1, 1, 1, 0, 1, 1, 2, 0, 1, 1, 0, 2, 2, 2])

"""

# %% SetUp

import numpy as np

species: np.ndarray
features: np.ndarray
labels: np.ndarray

DATA = 'https://python3.info/_static/iris-dirty.csv'

# English
# 1. Load text from `DATA`
# 2. Define variables:
#    - `species: np.ndarray[str]` - first row, columns 2, 3, 4
#    - `features: np.ndarray[float]` - all rows except the first one, columns 0, 1, 2, 3
#    - `labels: np.ndarray[int]` - all rows except the first one, column 4
# 3. Run doctests - all must succeed

# Polish
# 1. Wczytaj tekst z `DATA`
# 2. Zdefiniuj zmienne:
#    - `species: np.ndarray[str]` - pierwszy wiersz, kolumny 2, 3, 4
#    - `features: np.ndarray[float]` - wszystkie wiersze poza pierwszym, kolumny 0, 1, 2, 3
#    - `labels: np.ndarray[int]` - wszystkie wiersze poza pierwszym, kolumna 4
# 3. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
species = ...
features = ...
labels = ...