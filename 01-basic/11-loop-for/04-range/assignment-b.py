"""
* Assignment: Loop Dict To List
* Type: class assignment
* Complexity: medium
* Lines of code: 4 lines
* Time: 5 min

English:
    1. Define `result: list[dict]`:
        a. key - name from the header
        b. value - measurement or species
    2. Run doctests - all must succeed

Polish:
    1. Zdefiniuj `result: list[dict]`:
        a. klucz - nazwa z nagłówka
        b. wartość - wyniki pomiarów lub gatunek
    2. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from pprint import pprint

    >>> assert result is not Ellipsis, \
    'Assign your result to variable `result`'
    >>> assert type(result) is list, \
    'Variable `result` has invalid type, should be list'

    >>> assert all(type(x) is dict for x in result)

    >>> pprint(result, width=120, sort_dicts=False)
    [{'sepal_length': 5.8, 'sepal_width': 2.7, 'petal_length': 5.1, 'petal_width': 1.9, 'species': 'virginica'},
     {'sepal_length': 5.1, 'sepal_width': 3.5, 'petal_length': 1.4, 'petal_width': 0.2, 'species': 'setosa'},
     {'sepal_length': 5.7, 'sepal_width': 2.8, 'petal_length': 4.1, 'petal_width': 1.3, 'species': 'versicolor'},
     {'sepal_length': 6.3, 'sepal_width': 2.9, 'petal_length': 5.6, 'petal_width': 1.8, 'species': 'virginica'},
     {'sepal_length': 6.4, 'sepal_width': 3.2, 'petal_length': 4.5, 'petal_width': 1.5, 'species': 'versicolor'},
     {'sepal_length': 4.7, 'sepal_width': 3.2, 'petal_length': 1.3, 'petal_width': 0.2, 'species': 'setosa'}]
"""

DATA = [
    ('sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species'),
    (5.8, 2.7, 5.1, 1.9, 'virginica'),
    (5.1, 3.5, 1.4, 0.2, 'setosa'),
    (5.7, 2.8, 4.1, 1.3, 'versicolor'),
    (6.3, 2.9, 5.6, 1.8, 'virginica'),
    (6.4, 3.2, 4.5, 1.5, 'versicolor'),
    (4.7, 3.2, 1.3, 0.2, 'setosa'),
]

# Define variable `result` with converted DATA
# type: list[dict]

result = []
header = DATA[0]
rows = DATA[1:]

for sepal_length, sepal_width, petal_length, petal_width, species in rows:
    result.append(
        dict(sepal_length=sepal_length,
             sepal_width=sepal_width,
             petal_length=petal_length,
             petal_width=petal_width,
             species=species)
    )

# advanced
result = [{'sepal_length': sl,
           'sepal_width': sw,
           'petal_length': pl,
           'petal_width': pw,
           'species': species}
          for sl, sw, pl, pw, species in rows]
