"""
* Assignment: File Read Multiline
* Type: class assignment
* Complexity: easy
* Lines of code: 6 lines
* Time: 3 min

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
    * Comprehension
    * `str.strip()`
    * `str.split()`
    * `float()`
    * `tuple()`

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from os import remove; remove(FILE)

    >>> assert result is not Ellipsis, \
    'Assign your result to variable `result`'
    >>> assert type(result) is tuple, \
    'Variable `result` has invalid type, should be tuple'
    >>> assert all(type(x) in (float, str) for x in result), \
    'All rows in `result` should be float or str'

    >>> result
    (5.1, 3.5, 1.4, 0.2, 'setosa')
"""

FILE = '_temporary.txt'

with open(FILE, mode='wt') as file:
    file.write('5.1,3.5,1.4,0.2,setosa\n')

# Read `FILE` to `result: tuple`
# Remove whitespaces
# Split line by comma
# Convert numeric values to float
# type: tuple[float, float, float, float, str]
result = ''
with open(FILE, mode='rt') as file:
    result = file.read().strip().split(',')
    file.close()

numbers = [float(x) for x in result[:-1]]
full_list = numbers + result[4:]

result = tuple(full_list)

