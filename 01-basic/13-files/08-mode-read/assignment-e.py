"""
* Assignment: File Read CSV
* Type: class assignment
* Complexity: easy
* Lines of code: 15 lines
* Time: 8 min

English:
    1. Read `FILE` to `result: tuple`
    2. Remove whitespaces
    3. Split line by comma
    4. Convert numeric values to float
    5. Run doctests - all must succeed

Polish:
    1. Wczytaj `FILE` do `result: tuple`
    2. Usuń białe znaki
    3. Podziel linię po przecinku
    4. Przekonwertuj wartości numeryczne do float
    5. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `with`
    * `open()`
    * `str.split()`
    * `str.strip()`
    * Comprehension
    * `float()`
    * `(1,2,3) + ('abc',)`
    * `list.append()`

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from pprint import pprint
    >>> from os import remove; remove(FILE)

    >>> assert result is not Ellipsis, \
    'Assign your result to variable `result`'
    >>> assert type(result) is list, \
    'Variable `result` has invalid type, should be list'
    >>> assert all(type(x) is tuple for x in result), \
    'All rows in `result` should be tuple'

    >>> pprint(result)
    [('sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species'),
     (5.4, 3.9, 1.3, 0.4, 'setosa'),
     (5.9, 3.0, 5.1, 1.8, 'virginica'),
     (6.0, 3.4, 4.5, 1.6, 'versicolor'),
     (7.3, 2.9, 6.3, 1.8, 'virginica'),
     (5.6, 2.5, 3.9, 1.1, 'versicolor'),
     (5.4, 3.9, 1.3, 0.4, 'setosa')]
"""

FILE = '_temporary.csv'

DATA = """sepal_length,sepal_width,petal_length,petal_width,species
5.4,3.9,1.3,0.4,setosa
5.9,3.0,5.1,1.8,virginica
6.0,3.4,4.5,1.6,versicolor
7.3,2.9,6.3,1.8,virginica
5.6,2.5,3.9,1.1,versicolor
5.4,3.9,1.3,0.4,setosa
"""

with open(FILE, mode='w') as file:
    file.write(DATA)

# Read `FILE` to `result: tuple`
# Remove whitespaces
# Split line by comma
# Convert numeric values to float
# type: list[tuple]

result = []
with open(FILE, mode='rt') as file:
    header = file.readline().strip().split(',')
    result.append(tuple(header))
    for line in file:
        single_line = line.strip().split(',')
        numbers = [float(x) for x in single_line[:-1]]
        full_list = numbers + single_line[4:]
        result.append(tuple(full_list))
    file.close()

