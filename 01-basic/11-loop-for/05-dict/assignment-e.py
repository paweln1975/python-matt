"""
* Assignment: Loop Dict UniqueKeys
* Type: class assignment
* Complexity: easy
* Lines of code: 4 lines
* Time: 5 min

English:
    1. Define `result: set` with unique keys from `DATA`
    2. Run doctests - all must succeed

Polish:
    1. Zdefiniuj `result: set` z unikalnymi kluczami z `DATA`
    2. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from pprint import pprint

    >>> assert result is not Ellipsis, \
    'Assign your result to variable `result`'
    >>> assert type(result) is set, \
    'Variable `result` has invalid type, should be set'

    >>> assert all(type(x) is str for x in result)

    >>> result = sorted(result)
    >>> pprint(result, width=120, sort_dicts=False)
    ['petal_length', 'petal_width', 'sepal_length', 'sepal_width', 'species']
"""

DATA = [
    {'sepal_length': 5.1, 'sepal_width': 3.5, 'species': 'setosa'},
    {'petal_length': 4.1, 'petal_width': 1.3, 'species': 'versicolor'},
    {'sepal_length': 6.3, 'petal_width': 1.8, 'species': 'virginica'},
    {'sepal_length': 5.0, 'petal_width': 0.2, 'species': 'setosa'},
    {'sepal_width': 2.8, 'petal_length': 4.1, 'species': 'versicolor'},
    {'sepal_width': 2.9, 'petal_width': 1.8, 'species': 'virginica'},
]

# Define variable `result` with converted DATA
# type: set
result = set()
for row in DATA:
    result.update(row.keys())

