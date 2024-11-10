"""
* Assignment: File Read Multiline
* Type: class assignment
* Complexity: easy
* Lines of code: 3 lines
* Time: 3 min

English:
    1. Read `FILE` to `result: list[str]`
    2. Remove whitespaces
    3. Run doctests - all must succeed

Polish:
    1. Wczytaj `FILE` do `result: list[str]`
    2. Usuń białe znaki
    3. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `with`
    * `open()`

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from os import remove; remove(FILE)

    >>> assert result is not Ellipsis, \
    'Assign your result to variable `result`'
    >>> assert type(result) is str, \
    'Variable `result` has invalid type, should be str'

    >>> result
    'Fist line\\nSecond line\\nThird line\\n'
"""

FILE = '_temporary.txt'

DATA = """Fist line
Second line
Third line
"""

with open(FILE, mode='wt') as file:
    file.write(DATA)

# Read `FILE` to `result: list[str]`
# Remove whitespaces
# type: str
result = ''
with open(FILE, mode='rt') as file:
    for line in file:
        result += line
    file.close()
