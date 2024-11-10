"""
* Assignment: JSON File Load
* Complexity: medium
* Lines of code: 7 lines
* Time: 8 min

English:
    1. Read data from `FILE`
    2. Convert data to `result: list[tuple]`
    3. Add header as a first line
    4. Run doctests - all must succeed

Polish:
    1. Odczytaj dane z pliku `FILE`
    2. Przekonwertuj dane do `result: list[tuple]`
    3. Dodaj nagłówek jako pierwszą linię
    4. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * with open(mode='rt') as file:
    * json.load()
    * dict.keys()
    * dict.values()
    * tuple()
    * list.append()
    * list.extend()

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from pprint import pprint
    >>> from os import remove
    >>> remove(FILE)

    >>> assert result is not Ellipsis, \
    'Assign result to variable: `result`'
    >>> assert type(result) is list, \
    'Variable `result` has invalid type, should be list'
    >>> assert len(result) > 0, \
    'Variable `result` should not be empty'
    >>> assert all(type(row) is tuple for row in result), \
    'Variable `result` should be a list[tuple]'

    >>> pprint(result)
    [('sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species'),
     (5.8, 2.7, 5.1, 1.9, 'virginica'),
     (5.1, 3.5, 1.4, 0.2, 'setosa'),
     (5.7, 2.8, 4.1, 1.3, 'versicolor'),
     (6.3, 2.9, 5.6, 1.8, 'virginica'),
     (6.4, 3.2, 4.5, 1.5, 'versicolor'),
     (4.7, 3.2, 1.3, 0.2, 'setosa'),
     (7.0, 3.2, 4.7, 1.4, 'versicolor'),
     (7.6, 3.0, 6.6, 2.1, 'virginica'),
     (4.9, 3.0, 1.4, 0.2, 'setosa')]
"""

import json


FILE = r'_temporary.json'

with open(FILE, mode='wt') as file:
    file.write("""[
{"sepal_length": 5.8, "sepal_width": 2.7, "petal_length": 5.1, "petal_width": 1.9, "species": "virginica"},
{"sepal_length": 5.1, "sepal_width": 3.5, "petal_length": 1.4, "petal_width": 0.2, "species": "setosa"},
{"sepal_length": 5.7, "sepal_width": 2.8, "petal_length": 4.1, "petal_width": 1.3, "species": "versicolor"},
{"sepal_length": 6.3, "sepal_width": 2.9, "petal_length": 5.6, "petal_width": 1.8, "species": "virginica"},
{"sepal_length": 6.4, "sepal_width": 3.2, "petal_length": 4.5, "petal_width": 1.5, "species": "versicolor"},
{"sepal_length": 4.7, "sepal_width": 3.2, "petal_length": 1.3, "petal_width": 0.2, "species": "setosa"},
{"sepal_length": 7.0, "sepal_width": 3.2, "petal_length": 4.7, "petal_width": 1.4, "species": "versicolor"},
{"sepal_length": 7.6, "sepal_width": 3.0, "petal_length": 6.6, "petal_width": 2.1, "species": "virginica"},
{"sepal_length": 4.9, "sepal_width": 3.0, "petal_length": 1.4, "petal_width": 0.2, "species": "setosa"}
]""")

# type: list[tuple]
result = ...

