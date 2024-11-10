"""
* Assignment: Loop Unpack Startswith
* Type: class assignment
* Complexity: easy
* Lines of code: 4 lines
* Time: 5 min

English:
    1. Use `DATA: list[tuple]`
    2. Define `result: set` with:
       species names with prefix listed in `PREFIXES`
    3. Iterating over `DATA` unpack row to:
        a. `sl,sw,pl,pw` - all beside last
        b. `species` - last in the row
    3. Use unpack syntax in a for loop
    5. Run doctests - all must succeed

Polish:
    1. Użyj `DATA: list[tuple]`
    2. Zdefiniuj `result: set` z:
       nazwami gatunków z prefiksem wylistowanym w `PREFIXES`
    3. Iterując po `DATA` rozpakuj wiersz do:
        a. `sl,sw,pl,pw` - wszystkie oprócz ostatniego
        b. `species` - ostatni w wierszu
    4. Użyj składni rozpakowania w pętli for
    5. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `str.endswith()`

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
    False
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

PREFIXES = ('ver', 'vir')

# Define `result: set` with:
# species names with prefix listed in `PREFIXES`
# Iterating over `DATA` unpack row to:
# - `sl,sw,pl,pw` - all beside last
# - `species` - last in the row
# Use unpack syntax in a for loop
# type: set[str]

result = set()
rows = DATA[1:]

for sl,sw,pl,pw,species in rows:
    if species.startswith(PREFIXES):
        result.add(species)

# more advanced
result = {species
          for *values,species in rows
          if species.startswith(PREFIXES)}
