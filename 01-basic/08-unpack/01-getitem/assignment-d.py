"""
* Assignment: Unpack Getitem Select
* Type: class assignment
* Complexity: easy
* Lines of code: 4 lines
* Time: 5 min

English:
    1. Create `result: list`
       a. Append to `result` a row from `DATA` at index 0
       b. Append to `result` a row from `DATA` at index 1
       c. Append to `result` a row from `DATA` at index -1
    2. Non-functional requirements:
       a. Use only indexes (`getitem`)
       b. Do not use `str.split()`, `slice`, `for`, `while` or any other
          control-flow statement
    3. Run doctests - all must succeed

Polish:
    1. Stwórz `result: list`
       a. Dodaj do `result` wiersz z `DATA` o indeksie 0
       b. Dodaj do `result` wiersz z `DATA` o indeksie 1
       c. Dodaj do `result` wiersz z `DATA` o indeksie -1
    2. Wymagania niefunkcjonalne:
       a. Korzystaj tylko z indeksów (`getitem`)
       b. Nie używaj `str.split()`, `slice`, `for`, `while` lub
          jakiejkolwiek innej instrukcji sterującej
    3. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `list.append()`

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from pprint import pprint

    >>> assert result is not Ellipsis, \
    'Assign your result to variable `result`'
    >>> assert type(result) is list, \
    'Variable `result` has invalid type, should be list'
    >>> assert len(result) == 3, \
    'Variable `result` length should be 6'

    >>> pprint(result)
    [('sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species'),
     (5.8, 2.7, 5.1, 1.9, 'virginica'),
     (4.9, 2.5, 4.5, 1.7, 'virginica')]
"""

DATA = [
    ('sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species'),
    (5.8, 2.7, 5.1, 1.9, 'virginica'),
    (5.1, 3.5, 1.4, 0.2, 'setosa'),
    (5.7, 2.8, 4.1, 1.3, 'versicolor'),
    (6.3, 2.9, 5.6, 1.8, 'virginica'),
    (6.4, 3.2, 4.5, 1.5, 'versicolor'),
    (4.7, 3.2, 1.3, 0.2, 'setosa'),
    (7.0, 3.2, 4.7, 1.4, 'versicolor'),
    (7.6, 3.0, 6.6, 2.1, 'virginica'),
    (4.9, 3.0, 1.4, 0.2, 'setosa'),
    (4.9, 2.5, 4.5, 1.7, 'virginica'),
]

# Empty list
# type: list[list|tuple|set]
result = list()

# Append row from DATA at index 0
result.append(DATA[0])

# Append row from DATA at index 1
result.append(DATA[1])

# Append row from DATA at index -1
result.append(DATA[-1])

