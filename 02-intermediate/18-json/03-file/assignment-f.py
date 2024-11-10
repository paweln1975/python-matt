"""
* Assignment: JSON File Blanks
* Complexity: medium
* Lines of code: 13 lines
* Time: 13 min

English:
    1. Read data from `FILE`
    2. Convert data to `result: list[tuple]`
    3. Add sorted header as a first line
    4. Replace empty values with `None`
    5. Run doctests - all must succeed

Polish:
    1. Odczytaj dane z pliku `FILE`
    2. Przekonwertuj dane do `result: list[tuple]`
    3. Dodaj posortowany nagłówek jako pierwszą linia
    4. Zamień wartości puste na `None`
    5. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * with open(mode='rt') as file:
    * json.load()
    * dict.keys()
    * dict.values()
    * dict.get(default=None)
    * dict comprehension
    * tuple()
    * set()
    * set.update()
    * set.add()
    * sorted()
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
    [('petal_length', 'petal_width', 'sepal_length', 'sepal_width', 'species'),
     (None, None, None, None, 'virginica'),
     (1.4, 0.2, None, 3.5, 'setosa'),
     (4.1, 1.3, 5.7, None, 'versicolor'),
     (None, 1.8, 6.3, 2.9, 'virginica'),
     (4.5, None, 6.4, 3.2, 'versicolor'),
     (None, None, 4.7, 3.2, 'setosa'),
     (4.7, 1.4, None, None, 'versicolor'),
     (None, 2.1, 7.6, None, 'virginica'),
     (1.4, None, None, 3.0, 'setosa')]
"""

import json


FILE = r'_temporary.json'

with open(FILE, mode='wt') as file:
    file.write("""[
{"species": "virginica"},
{"sepal_width": 3.5, "petal_length": 1.4, "petal_width": 0.2, "species": "setosa"},
{"sepal_length": 5.7, "petal_length": 4.1, "petal_width": 1.3, "species": "versicolor"},
{"sepal_length": 6.3, "sepal_width": 2.9, "petal_width": 1.8, "species": "virginica"},
{"sepal_length": 6.4, "sepal_width": 3.2, "petal_length": 4.5, "species": "versicolor"},
{"sepal_length": 4.7, "sepal_width": 3.2, "species": "setosa"},
{"petal_length": 4.7, "petal_width": 1.4, "species": "versicolor"},
{"sepal_length": 7.6, "petal_width": 2.1, "species": "virginica"},
{"sepal_width": 3.0, "petal_length": 1.4, "species": "setosa"}
]""")

# type: list[tuple]
result = ...

