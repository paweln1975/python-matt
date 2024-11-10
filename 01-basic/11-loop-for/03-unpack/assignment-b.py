"""
* Assignment: Loop Unpack Unique
* Type: class assignment
* Complexity: easy
* Lines of code: 3 lines
* Time: 5 min

English:
    1. Use `DATA: list[tuple]`
    2. Define `result: set` with unique species names from `DATA`
    3. Use unpack syntax in a for loop
    5. Run doctests - all must succeed

Polish:
    1. Użyj `DATA: list[tuple]`
    2. Zdefiniuj `result: set` z unikalnymi nazwami gatunków z `DATA`
    3. Użyj składni rozpakowania w pętli for
    4. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert result is not Ellipsis, \
    'Assign your result to variable `result`'
    >>> assert type(result) is set, \
    'Result must be a set'
    >>> assert len(result) > 0, \
    'Result cannot be empty'
    >>> assert all(type(element) is str for element in result), \
    'All elements in result must be a str'

    >>> 'virginica' in result
    True
    >>> 'setosa' in result
    True
    >>> 'versicolor' in result
    True
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
    (4.6, 3.1, 1.5, 0.2, 'setosa'),
]

# Define `result: set` with unique species names from `DATA`
# Use unpack syntax in a for loop
# type: set[str]

result = set()
rows = DATA[1:]

for sepal_length, sepal_width, petal_length, petal_width, species in rows:
    result.add(species)

result = set()
rows = DATA[1:]

for *values, species in rows:
    result.add(species)

result = set()
result.update(species for *values, species in rows)


result = set()
result.update(y for *X,y in rows)
