"""
* Assignment: CSV DictReader Iris
* Complexity: easy
* Lines of code: 5 lines
* Time: 5 min

English:
    1. Define `result: list[dict]`
    2. To `result` add data read from `FILE`
    3. Use `csv.DictReader` to parse file
    4. Convert values to float
    5. Run doctests - all must succeed

Polish:
    1. Zdefiniuj `result: list[dict]`
    2. Do `result` dodaj wczytane dane z pliku `FILE`
    3. Użyj `csv.DictReader` do sparsowania pliku
    4. Skonwertuj wartości na floaty
    5. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from pprint import pprint
    >>> from os import remove
    >>> remove(FILE)

    >>> assert result is not Ellipsis, \
    'Assign result to variable: `result`'
    >>> assert type(result) is list, \
    'Variable `result` has invalid type, should be list'
    >>> assert all(type(x) is dict for x in result), \
    'All rows in `result` should be dict'

    >>> pprint(result, sort_dicts=False)
    [{'sepal_length': 5.8,
      'sepal_width': 2.7,
      'petal_length': 5.1,
      'petal_width': 1.9,
      'species': 'virginica'},
     {'sepal_length': 5.1,
      'sepal_width': 3.5,
      'petal_length': 1.4,
      'petal_width': 0.2,
      'species': 'setosa'},
     {'sepal_length': 5.7,
      'sepal_width': 2.8,
      'petal_length': 4.1,
      'petal_width': 1.3,
      'species': 'versicolor'}]
"""

import csv


DATA = """sepal_length,sepal_width,petal_length,petal_width,species
5.8,2.7,5.1,1.9,virginica
5.1,3.5,1.4,0.2,setosa
5.7,2.8,4.1,1.3,versicolor"""

FILE = r'_temporary.csv'

with open(FILE, mode='wt', encoding='utf-8') as file:
    file.write(DATA)

# Define `result: list[dict]`
# To `result` add data read from `FILE`
# Use `csv.DictReader` to parse file
# Convert values to float
# type: list[dict]
result = ...

with open(FILE, mode='rt', encoding='utf-8') as file:
    ...

