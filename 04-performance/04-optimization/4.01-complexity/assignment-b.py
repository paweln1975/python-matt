"""
Name: Performance Compexity UniqueKeys
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
Terminal: `python -m doctest -v assignment-b.py`

Tests:
>>> import sys; sys.tracebacklimit = 0
>>> assert sys.version_info >= (3, 9), \
'Python 3.9+ required'

>>> result is not Ellipsis
True
>>> type(result) in (set, list, tuple, frozenset)
True
>>> sorted(result)
['petal_length', 'petal_width', 'sepal_length', 'sepal_width', 'species']

Hints:
`row.keys()`
Compare solutions with `Micro-benchmarking`

"""

# %% SetUp

result: set[str]

DATA = [
    {'sepal_length': 5.1, 'sepal_width': 3.5, 'species': 'setosa'},
    {'petal_length': 4.1, 'petal_width': 1.3, 'species': 'versicolor'},
    {'sepal_length': 6.3, 'petal_width': 1.8, 'species': 'virginica'},
    {'sepal_length': 5.0, 'petal_width': 0.2, 'species': 'setosa'},
    {'sepal_width': 2.8, 'petal_length': 4.1, 'species': 'versicolor'},
    {'sepal_width': 2.9, 'petal_width': 1.8, 'species': 'virginica'},
]

# English
# 1. Collect unique keys from all rows in one sequence `result`
# 2. Run doctests - all must succeed

# Polish
# 1. Zbierz unikalne klucze z wszystkich wierszy w jednej sekwencji `result`
# 2. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
result = ...