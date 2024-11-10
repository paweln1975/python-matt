"""
* Assignment: File Read List[str]
* Type: class assignment
* Complexity: easy
* Lines of code: 2 lines
* Time: 3 min

English:
    1. Read `FILE` to `result: list[str]`
    2. Remove whitespaces
    3. Split line by comma
    4. Run doctests - all must succeed

Polish:
    1. Wczytaj `FILE` do `result: list[str]`
    2. Usuń białe znaki
    3. Podziel linię po przecinku
    4. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `with`
    * `open()`
    * `str.strip()`
    * `str.split()`

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from os import remove; remove(FILE)

    >>> assert result is not Ellipsis, \
    'Assign your result to variable `result`'
    >>> assert type(result) is list, \
    'Variable `result` has invalid type, should be list'
    >>> assert all(type(x) is str for x in result), \
    'All rows in `result` should be str'

    >>> result
    ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']
"""

FILE = '_temporary.txt'
DATA = 'sepal_length,sepal_width,petal_length,petal_width,species'

with open(FILE, mode='wt') as file:
    file.write(DATA)

# Read `FILE` to `result: list[str]`
# Remove whitespaces
# Split line by comma
# type: str
result = ''
with open(FILE, mode='rt') as file:
    result = file.read().split(',')
    file.close()

